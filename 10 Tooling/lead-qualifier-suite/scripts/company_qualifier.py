from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse


LABELS = ["priority_now", "good_fit", "maybe", "skip"]

QUALIFICATION_CORE_COLUMNS = [
    "normalized_website",
    "normalized_domain",
    "normalized_company_name",
    "company_description",
    "research_status",
    "research_failure_reason",
    "qualification_label",
    "qualification_reason",
    "evidence_summary",
    "evidence_source_url",
]

GAMMA_CORE_COLUMNS = [
    "gamma_cover_line",
    "gamma_video_1_title",
    "gamma_video_1_brief",
    "gamma_video_2_title",
    "gamma_video_2_brief",
    "gamma_video_3_title",
    "gamma_video_3_brief",
    "gamma_deck_status",
    "gamma_deck_failure_reason",
    "gamma_deck_url",
]

FIELD_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_ -]*$")


def normalize_website(value: str) -> tuple[str, str]:
    raw = (value or "").strip()
    if not raw:
        return "", ""
    candidate = raw if re.match(r"^https?://", raw, re.I) else f"https://{raw}"
    parsed = urlparse(candidate)
    domain = (parsed.hostname or "").lower()
    if domain.startswith("www."):
        domain = domain[4:]
    if not domain or "." not in domain:
        return "", ""
    return f"https://{domain}", domain


def normalize_company_name(value: str) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    cleaned = re.sub(r"\s+", " ", raw).encode("ascii", "ignore").decode("ascii")
    cleaned = re.sub(r"\(.*?\)", " ", cleaned)
    cleaned = re.sub(r"\s*[-|:]\s*.*$", " ", cleaned)
    cleaned = re.sub(r"\.(?:ai|io|com|co|app|net|org)\b", " ", cleaned, flags=re.I)
    cleaned = re.sub(r"[^A-Za-z0-9 ]+", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    if not cleaned:
        return ""
    return " ".join(token[:1].upper() + token[1:].lower() for token in cleaned.split())


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def output_paths(output_dir: Path) -> dict[str, Path]:
    return {
        "state": output_dir / "run-state.json",
        "personalization_spec": output_dir / "personalization-spec.json",
        "gamma_spec": output_dir / "gamma-deck-spec.json",
        "domain_cache": output_dir / "domain-cache.json",
    }


def load_state(paths: dict[str, Path]) -> dict:
    if not paths["state"].exists():
        raise ValueError("Run is not initialized. Run the qualification skill's 'init' first.")
    return load_json(paths["state"])


def save_state(paths: dict[str, Path], state: dict) -> None:
    paths["state"].write_text(json.dumps(state, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Cross-row domain cache: lets a company with multiple contact rows reuse one
# row's qualification/personalization/gamma output instead of redoing the
# work (and, for gamma, re-calling the paid Gamma API) for every row.
# ---------------------------------------------------------------------------

def load_domain_cache(paths: dict[str, Path]) -> dict:
    path = paths["domain_cache"]
    if not path.exists():
        return {}
    return load_json(path)


def save_domain_cache(paths: dict[str, Path], cache: dict) -> None:
    paths["domain_cache"].write_text(json.dumps(cache, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def command_lookup_domain(args: argparse.Namespace) -> None:
    output_dir = Path(args.output_dir).resolve()
    paths = output_paths(output_dir)
    load_state(paths)
    domain = (args.domain or "").strip().lower()
    if not domain and args.website:
        _, domain = normalize_website(args.website)
    if not domain:
        raise ValueError("Provide --domain (already-normalized) or --website (raw value to normalize).")
    cache = load_domain_cache(paths)
    stage_data = cache.get(domain, {}).get(args.stage)
    if stage_data:
        print(json.dumps({"cached": True, "normalized_domain": domain, "sheet_row": stage_data}, indent=2, ensure_ascii=True))
    else:
        print(json.dumps({"cached": False, "normalized_domain": domain}, indent=2, ensure_ascii=True))


# ---------------------------------------------------------------------------
# Stage 1/2: qualification
# ---------------------------------------------------------------------------

def command_init(args: argparse.Namespace) -> None:
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = output_paths(output_dir)
    state = {
        "sheet_id": args.sheet_id,
        "website_column": args.website_column,
        "company_column": args.company_column or "",
        "personalization_fields": [],
        "output_columns": list(QUALIFICATION_CORE_COLUMNS),
    }
    if paths["state"].exists():
        existing_state = load_json(paths["state"])
        if existing_state.get("sheet_id") == state["sheet_id"] and \
           existing_state.get("website_column") == state["website_column"] and \
           existing_state.get("company_column") == state["company_column"]:
            print(json.dumps({"status": "resumed", "sheet_id": args.sheet_id, "output_columns": existing_state["output_columns"]}, indent=2))
            return
        raise ValueError("Output directory belongs to a different sheet/column mapping. Use a new output directory.")
    save_state(paths, state)
    print(json.dumps({"status": "initialized", "sheet_id": args.sheet_id, "output_columns": state["output_columns"]}, indent=2))


def validate_qualification_result(result: dict) -> list[str]:
    errors = []
    status = result.get("research_status")
    if status not in {"success", "failed"}:
        errors.append("research_status must be 'success' or 'failed'.")
    if status == "success":
        for field in ["company_description", "qualification_reason", "evidence_summary", "evidence_source_url"]:
            if not str(result.get(field, "")).strip():
                errors.append(f"Successful result requires {field}.")
        label = result.get("qualification_label")
        if label not in LABELS:
            errors.append("Successful result requires a valid qualification_label.")
        source = str(result.get("evidence_source_url", ""))
        if source and not re.match(r"^https?://", source, re.I):
            errors.append("evidence_source_url must be an HTTP(S) URL.")
    if status == "failed" and not str(result.get("research_failure_reason", "")).strip():
        errors.append("Failed result requires research_failure_reason.")
    return errors


def command_validate_qualification_result(args: argparse.Namespace) -> None:
    output_dir = Path(args.output_dir).resolve()
    paths = output_paths(output_dir)
    state = load_state(paths)
    result = load_json(Path(args.result))
    errors = validate_qualification_result(result)
    if errors:
        raise ValueError("Invalid result:\n- " + "\n- ".join(errors))
    website, domain = normalize_website(result.get("_raw_website", ""))
    normalized_company = normalize_company_name(result.get("_raw_company", ""))
    sheet_row = {col: "" for col in state["output_columns"]}
    sheet_row.update({k: v for k, v in result.items() if not k.startswith("_")})
    sheet_row["normalized_website"] = website
    sheet_row["normalized_domain"] = domain
    sheet_row["normalized_company_name"] = normalized_company
    if domain:
        cache = load_domain_cache(paths)
        cache.setdefault(domain, {})["qualification"] = sheet_row
        save_domain_cache(paths, cache)
    print(json.dumps({"status": "valid", "sheet_row": sheet_row, "normalized_domain": domain}, indent=2, ensure_ascii=True))


# ---------------------------------------------------------------------------
# Stage 2: personalization (custom outreach lines)
# ---------------------------------------------------------------------------

def validate_personalization_spec(spec: dict) -> list[str]:
    errors = []
    if spec.get("approved") is not True:
        errors.append("Specification must have approved=true after explicit user approval.")
    for field in ["template", "target_profile"]:
        if not str(spec.get(field, "")).strip():
            errors.append(f"Specification requires {field}.")
    custom_fields = spec.get("custom_fields")
    if not isinstance(custom_fields, list) or not custom_fields:
        errors.append("Specification requires at least one custom_fields entry.")
        return errors
    names = []
    required = ["name", "insertion_point", "purpose", "wording_pattern", "sentence_requirements", "approved_example"]
    for index, item in enumerate(custom_fields):
        if not isinstance(item, dict):
            errors.append(f"custom_fields[{index}] must be an object.")
            continue
        for field in required:
            if not str(item.get(field, "")).strip():
                errors.append(f"custom_fields[{index}] requires {field}.")
        name = str(item.get("name", "")).strip()
        if name and not FIELD_RE.match(name):
            errors.append(f"Invalid custom field name: {name}")
        names.append(name)
    if len(names) != len(set(names)):
        errors.append("Custom field names must be unique.")
    reserved = set(QUALIFICATION_CORE_COLUMNS) | set(GAMMA_CORE_COLUMNS)
    collisions = set(names) & reserved
    if collisions:
        errors.append("Custom field names collide with reserved columns: " + ", ".join(sorted(collisions)))
    return errors


def command_init_personalization(args: argparse.Namespace) -> None:
    output_dir = Path(args.output_dir).resolve()
    paths = output_paths(output_dir)
    state = load_state(paths)
    spec = load_json(Path(args.spec))
    errors = validate_personalization_spec(spec)
    if errors:
        raise ValueError("Invalid personalization specification:\n- " + "\n- ".join(errors))
    field_names = [item["name"] for item in spec["custom_fields"]]
    paths["personalization_spec"].write_text(json.dumps(spec, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    state["personalization_fields"] = field_names
    merged_columns = list(state["output_columns"])
    for name in field_names:
        if name not in merged_columns:
            merged_columns.append(name)
    state["output_columns"] = merged_columns
    save_state(paths, state)
    print(json.dumps({"status": "initialized", "output_columns": state["output_columns"], "personalization_fields": field_names}, indent=2))


def validate_personalization_result(result: dict, custom_specs: list[dict]) -> list[str]:
    errors = []
    label = result.get("_qualification_label")
    if label not in LABELS:
        errors.append("_qualification_label must be one of the known labels (read it from the sheet row).")
    if not str(result.get("_normalized_domain", "")).strip():
        errors.append("_normalized_domain is required (copy the sheet row's normalized_domain value) so this row's output can be reused by other rows at the same company.")
    if label == "skip":
        for item in custom_specs:
            if str(result.get(item["name"], "")).strip():
                errors.append(f"Skip rows must leave custom field '{item['name']}' blank.")
    else:
        for item in custom_specs:
            value = str(result.get(item["name"], ""))
            if not value.strip():
                errors.append(f"Successful non-skip result requires custom field '{item['name']}'.")
            maximum = item.get("max_characters")
            if isinstance(maximum, int) and maximum > 0 and len(value) > maximum:
                errors.append(f"'{item['name']}' exceeds max_characters ({maximum}).")
    return errors


def command_validate_personalization_result(args: argparse.Namespace) -> None:
    output_dir = Path(args.output_dir).resolve()
    paths = output_paths(output_dir)
    state = load_state(paths)
    if not paths["personalization_spec"].exists():
        raise ValueError("Personalization is not initialized. Run 'init-personalization' first.")
    spec = load_json(paths["personalization_spec"])
    result = load_json(Path(args.result))
    errors = validate_personalization_result(result, spec["custom_fields"])
    if errors:
        raise ValueError("Invalid result:\n- " + "\n- ".join(errors))
    sheet_row = {name: result.get(name, "") for name in state["personalization_fields"]}
    domain = str(result.get("_normalized_domain", "")).strip().lower()
    if domain:
        cache = load_domain_cache(paths)
        cache.setdefault(domain, {})["personalization"] = sheet_row
        save_domain_cache(paths, cache)
    print(json.dumps({"status": "valid", "sheet_row": sheet_row, "normalized_domain": domain}, indent=2, ensure_ascii=True))


# ---------------------------------------------------------------------------
# Stage 3: gamma deck
# ---------------------------------------------------------------------------

GAMMA_TEXT_FIELDS = [
    "gamma_cover_line",
    "gamma_video_1_title",
    "gamma_video_1_brief",
    "gamma_video_2_title",
    "gamma_video_2_brief",
    "gamma_video_3_title",
    "gamma_video_3_brief",
]


def validate_gamma_spec(spec: dict) -> list[str]:
    errors = []
    if spec.get("approved") is not True:
        errors.append("Specification must have approved=true after explicit user approval.")
    for field in ["cover_line_pattern", "video_brief_pattern"]:
        if not str(spec.get(field, "")).strip():
            errors.append(f"Specification requires {field}.")
    if not isinstance(spec.get("max_characters_brief"), int) or spec.get("max_characters_brief") <= 0:
        errors.append("Specification requires a positive integer max_characters_brief.")
    if not str(spec.get("approved_example_brief", "")).strip():
        errors.append("Specification requires approved_example_brief.")
    return errors


def command_init_gamma(args: argparse.Namespace) -> None:
    output_dir = Path(args.output_dir).resolve()
    paths = output_paths(output_dir)
    state = load_state(paths)
    spec = load_json(Path(args.spec))
    errors = validate_gamma_spec(spec)
    if errors:
        raise ValueError("Invalid gamma-deck specification:\n- " + "\n- ".join(errors))
    paths["gamma_spec"].write_text(json.dumps(spec, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    merged_columns = list(state["output_columns"])
    for name in GAMMA_CORE_COLUMNS:
        if name not in merged_columns:
            merged_columns.append(name)
    state["output_columns"] = merged_columns
    save_state(paths, state)
    print(json.dumps({"status": "initialized", "output_columns": state["output_columns"], "gamma_columns": GAMMA_CORE_COLUMNS}, indent=2))


def validate_gamma_result(result: dict, spec: dict) -> list[str]:
    errors = []
    label = result.get("_qualification_label")
    if label not in LABELS:
        errors.append("_qualification_label must be one of the known labels (read it from the sheet row).")
    if not str(result.get("_normalized_domain", "")).strip():
        errors.append("_normalized_domain is required (copy the sheet row's normalized_domain value) so this row's deck can be reused by other rows at the same company.")
    status = result.get("gamma_deck_status")
    if status not in {"success", "failed", "skipped"}:
        errors.append("gamma_deck_status must be 'success', 'failed', or 'skipped'.")
    if label == "skip":
        if status != "skipped":
            errors.append("Rows labeled 'skip' must have gamma_deck_status='skipped'.")
        for field in GAMMA_TEXT_FIELDS + ["gamma_deck_url"]:
            if str(result.get(field, "")).strip():
                errors.append(f"Skipped rows must leave '{field}' blank.")
        return errors
    if status == "success":
        for field in GAMMA_TEXT_FIELDS:
            value = str(result.get(field, ""))
            if not value.strip():
                errors.append(f"Successful result requires {field}.")
        maximum = spec.get("max_characters_brief")
        for field in ["gamma_video_1_brief", "gamma_video_2_brief", "gamma_video_3_brief"]:
            value = str(result.get(field, ""))
            if isinstance(maximum, int) and maximum > 0 and len(value) > maximum:
                errors.append(f"'{field}' exceeds max_characters_brief ({maximum}).")
        url = str(result.get("gamma_deck_url", ""))
        if not url or not re.match(r"^https?://", url, re.I):
            errors.append("Successful result requires a valid HTTP(S) gamma_deck_url.")
    if status == "failed" and not str(result.get("gamma_deck_failure_reason", "")).strip():
        errors.append("Failed result requires gamma_deck_failure_reason.")
    return errors


def command_validate_gamma_result(args: argparse.Namespace) -> None:
    output_dir = Path(args.output_dir).resolve()
    paths = output_paths(output_dir)
    load_state(paths)
    if not paths["gamma_spec"].exists():
        raise ValueError("Gamma-deck stage is not initialized. Run 'init-gamma' first.")
    spec = load_json(paths["gamma_spec"])
    result = load_json(Path(args.result))
    errors = validate_gamma_result(result, spec)
    if errors:
        raise ValueError("Invalid result:\n- " + "\n- ".join(errors))
    sheet_row = {col: result.get(col, "") for col in GAMMA_CORE_COLUMNS}
    domain = str(result.get("_normalized_domain", "")).strip().lower()
    if domain:
        cache = load_domain_cache(paths)
        cache.setdefault(domain, {})["gamma"] = sheet_row
        save_domain_cache(paths, cache)
    print(json.dumps({"status": "valid", "sheet_row": sheet_row, "normalized_domain": domain}, indent=2, ensure_ascii=True))


# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("--sheet-id", required=True)
    init_parser.add_argument("--website-column", required=True)
    init_parser.add_argument("--company-column")
    init_parser.add_argument("--output-dir", required=True)
    init_parser.set_defaults(func=command_init)

    vqr_parser = subparsers.add_parser("validate-qualification-result")
    vqr_parser.add_argument("--output-dir", required=True)
    vqr_parser.add_argument("--result", required=True)
    vqr_parser.set_defaults(func=command_validate_qualification_result)

    ip_parser = subparsers.add_parser("init-personalization")
    ip_parser.add_argument("--output-dir", required=True)
    ip_parser.add_argument("--spec", required=True)
    ip_parser.set_defaults(func=command_init_personalization)

    vpr_parser = subparsers.add_parser("validate-personalization-result")
    vpr_parser.add_argument("--output-dir", required=True)
    vpr_parser.add_argument("--result", required=True)
    vpr_parser.set_defaults(func=command_validate_personalization_result)

    ig_parser = subparsers.add_parser("init-gamma")
    ig_parser.add_argument("--output-dir", required=True)
    ig_parser.add_argument("--spec", required=True)
    ig_parser.set_defaults(func=command_init_gamma)

    vgr_parser = subparsers.add_parser("validate-gamma-result")
    vgr_parser.add_argument("--output-dir", required=True)
    vgr_parser.add_argument("--result", required=True)
    vgr_parser.set_defaults(func=command_validate_gamma_result)

    ld_parser = subparsers.add_parser("lookup-domain")
    ld_parser.add_argument("--output-dir", required=True)
    ld_parser.add_argument("--domain", help="Already-normalized domain (e.g. 'example.com').")
    ld_parser.add_argument("--website", help="Raw website value to normalize into a domain.")
    ld_parser.add_argument("--stage", required=True, choices=["qualification", "personalization", "gamma"])
    ld_parser.set_defaults(func=command_lookup_domain)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
