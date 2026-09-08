#!/usr/bin/env python3
"""Valence Ops — automatic wrap trigger.

Runs on Stop. Decides whether enough has happened to be worth proposing a
changeset, and if so blocks the stop so Claude produces one. Claude decides
whether anything is actually durable; this script only decides when to ask.

Tuning: WRAP_EVERY_N_TURNS below. Disable via /hooks.
"""
import sys, json, os, re, pathlib

WRAP_EVERY_N_TURNS = 2          # user turns since the last check before asking again
STATE = pathlib.Path(__file__).resolve().parent.parent / ".wrap-state.json"
SIGNOFF = re.compile(
    r"\b(bye|goodnight|good night|done for (the day|today|now)|that'?s (it|all|everything)"
    r"|log ?off|logging off|see you|catch you|end (of )?(the )?session|wrap( it)? up|signing off"
    r"|talk (to you )?(later|tomorrow)|for (the )?day)\b", re.I)

INSTRUCTION = (
    "AUTOMATIC WRAP (Stop hook). Follow CLAUDE.md section 'Write policy'.\n"
    "1. Review this session for DURABLE information only: a clinic fact Tilak reported, "
    "feedback or a judgement he gave, a working preference, a rule or decision, a deliverable produced, "
    "a thread opened or closed.\n"
    "2. Drop everything in policy section 2: drafts and unsent variants, chat reasoning, option surveys, "
    "session summaries, restatements of existing rules, timestamps and follow-up counts that decide nothing, "
    "and minor updates already captured in a state note or in git.\n"
    "3. If nothing durable survives, reply with exactly: Nothing durable to file. Then stop.\n"
    "4. Otherwise output ONLY the changeset table (File | Add or Amend | one line | label), plus a short "
    "'Waiting for your yes' list for anything in policy section 4 that always needs approval. "
    "Route state as stage, never as a timeline.\n"
    "5. DO NOT write, edit or commit anything. Stop after the table and wait for Tilak's approval.\n"
    "Tilak is responsible only for reporting real-world external events (sends, replies, calls, meetings, "
    "client and team). Never invent one, and never ask him to log anything else."
)

def main():
    try:
        inp = json.load(sys.stdin)
    except Exception:
        return
    if inp.get("stop_hook_active"):
        return                                   # already continuing from this hook; never loop
    sid = str(inp.get("session_id") or "default")
    tpath = inp.get("transcript_path")
    turns, last_text = 0, ""
    if tpath and os.path.exists(tpath):
        with open(tpath, errors="ignore") as fh:
            for line in fh:
                try:
                    ev = json.loads(line)
                except Exception:
                    continue
                if ev.get("type") != "user" or ev.get("isMeta"):
                    continue
                c = ev.get("message", {}).get("content")
                if isinstance(c, list):
                    if any(b.get("type") == "tool_result" for b in c if isinstance(b, dict)):
                        continue
                    text = " ".join(b.get("text", "") for b in c if isinstance(b, dict))
                else:
                    text = c or ""
                if "<local-command" in text or "<command-name>" in text:
                    continue
                turns += 1
                last_text = text
    try:
        state = json.loads(STATE.read_text())
    except Exception:
        state = {}
    last = int(state.get(sid, 0))
    if turns - last < WRAP_EVERY_N_TURNS and not SIGNOFF.search(last_text or ""):
        return
    state[sid] = turns
    try:
        STATE.write_text(json.dumps(state))
    except Exception:
        pass
    print(json.dumps({"decision": "block", "reason": INSTRUCTION}))

main()
