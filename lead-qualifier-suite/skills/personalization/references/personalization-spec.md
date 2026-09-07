# Personalization Specification

Create a JSON file with this shape only after the user explicitly approves the proposed wording and examples:

```json
{
  "approved": true,
  "approved_at": "2026-06-10T12:00:00+05:30",
  "template": "Hi {{first_name}}, ... {{custom_line_1}} ...",
  "copy_notes": "Any broader copy context.",
  "target_profile": "Use the default target profile.",
  "custom_fields": [
    {
      "name": "custom_line_1",
      "insertion_point": "After the opening greeting.",
      "purpose": "Connect what the company actually does to the outreach premise and, when required, to a GTM-specific end outcome.",
      "wording_pattern": "Noticed [verified capability], which helps [team or workflow] [specific GTM outcome].",
      "sentence_requirements": "One complete sentence or one approved phrase, conversational, 8-24 words, grounded in website evidence.",
      "max_characters": 180,
      "prohibited_claims": ["unsupported praise", "guessed results", "fabricated customer names"],
      "approved_example": "Noticed you help sales teams automate LinkedIn outreach, which helps them target better accounts and book more meetings."
    }
  ]
}
```

Rules:

- `approved` must be `true`.
- `template`, `target_profile`, and at least one `custom_fields` entry are required.
- Each custom-field `name` must be unique and safe as a CSV column.
- Include the exact insertion point and wording constraints for each field.
- When the approved copy contract requires it, custom fields must be based on what the company actually does and tied to a GTM-specific end outcome or result.
- Custom fields must be written only after the company is qualified from website evidence.
- Custom fields must remain blank for `skip` and `failed` rows.
- Examples illustrate form only; never reuse their claims for unrelated companies.
