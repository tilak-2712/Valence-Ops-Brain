**VALENCE OPS**

**Pre-Deployment
Shadow Audit
Checklist**

*Run this before touching any clinic data. Every check.*

Document 01 of 3 | Pre-Deployment Infrastructure | Elective Clinic Vertical

Version 1.0 | Bengaluru, India | June 2026

# **Purpose & How to Use This Document**

This checklist runs before the Revenue Leakage Audit. Its job is to determine whether the data the clinic hands you is complete enough to trust. A Revenue Leakage Audit run on a corrupted or partial dataset produces wrong numbers — and wrong numbers mean a system that misfires on launch.

The checklist is sequenced deliberately. Run Phase 1 checks first. The findings there change how you interpret everything in Phase 2 and 3. Do not skip ahead.

**Three outputs come out of this audit:**

* A data trust score — how much of the pipeline is actually visible to you
* A list of active shadow patterns — which of the 20 known failure modes are confirmed present
* A deployment risk rating — whether you can proceed, need to remediate first, or need to renegotiate scope

# **PHASE 1: Data Source Verification**

*Run before you look at a single lead record. The goal is to establish what data sources actually exist and whether you have all of them.*

## **1.1 — Channel Mapping**

Ask the owner: "Walk me through every channel where a patient can reach your clinic — WhatsApp, Instagram, website form, phone call, walk-in, Google Business, referral. For each one, where does that inquiry go first?"

**Map each channel to one of:**

* A — Goes into CRM/spreadsheet (trackable)
* B — Goes into WhatsApp inbox (partially trackable)
* C — Goes into owner/coordinator personal phone (NOT trackable)
* D — Handled verbally / walk-in register / paper (NOT trackable)

***Red flag threshold: Any channel mapped to C or D means the dataset you've been handed is structurally incomplete. Note which channels and continue.***

## **1.2 — Volume Plausibility Check**

Get the clinic's last 90-day ad spend across all channels. Apply the CPQL benchmark to estimate expected lead volume.

| **Specialty** | **CPQL Range (₹)** | **At ₹1L Spend** | **At ₹3L Spend** |
| --- | --- | --- | --- |
| IVF / Fertility | ₹1,180 – ₹2,400 | 42 – 85 leads | 125 – 254 leads |
| Aesthetic Dermatology | ₹980 – ₹1,800 | 56 – 102 leads | 167 – 306 leads |
| Hair Transplant | ₹1,350 – ₹2,640 | 38 – 74 leads | 114 – 222 leads |
| Cosmetic Surgery | ₹1,200 – ₹2,500 | 40 – 83 leads | 120 – 250 leads |
| Dental (Implants/Aligners) | ₹800 – ₹1,600 | 63 – 125 leads | 188 – 375 leads |
| LASIK | ₹900 – ₹1,700 | 59 – 111 leads | 176 – 333 leads |

**Formula: Estimated leads = Ad Spend ÷ CPQL midpoint**

Compare estimated leads against leads logged in their dataset. A gap >25% confirms top-of-funnel capture failure. A gap >50% means you are looking at a partial dataset — proceed with extreme caution on any diagnostic number you produce.

*Cross-check: Pull Meta Ads Manager → Leads Generated for the same period. Compare directly to CRM lead count. Any divergence >10% confirms missing leads.*

## **1.3 — Parallel Source Detection**

Ask to see the physical reception desk during peak hours. Look for:

* A walk-in register or paper notebook
* Sticky notes with patient names/numbers
* A separate spreadsheet tab that was not in the export
* A WhatsApp group where leads are being shared informally

Ask the coordinator: "Where do you personally keep track of which patients you need to follow up with?" The answer to this question — not the CRM — is often the real system.

***If you are handed an Excel file with exactly 8–10 perfectly named columns and zero blank fields — stop. This is a sanitized export, not a raw data dump. Ask for the original system export or CRM CSV.***

# **PHASE 2: Data Integrity Checks**

*Run on the actual dataset the clinic provides. These checks identify active manipulation and incompleteness patterns.*

## **2.1 — Timestamp Distribution Analysis**

Export lead creation timestamps and last-updated timestamps. Run a frequency distribution by hour of day.

* Healthy data: timestamps distributed organically across business hours, 9 AM – 7 PM
* Batch entry signature: >60% of updates clustered in a 45-minute window at end of day
* CSV upload signature: multiple leads with identical timestamps down to the second

Batch entry means first-contact timestamps are meaningless. Speed-to-lead metrics will be wrong. Flag this finding explicitly in your audit output.

## **2.2 — Status Distribution Check**

Pull the count of leads in each status. Benchmark against expected distributions for digital ad traffic:

| **Status** | **Expected Range** | **Red Flag If...** |
| --- | --- | --- |
| New / Uncontacted | 15–30% of total | < 5% — leads never enter top of funnel |
| In Follow-up / Nurturing | 30–45% of total | > 70% — recency bias is active |
| Lost / Not Interested | 20–35% of total | > 50% — inbox clearance marking likely |
| Converted | 11–20% for digital leads | > 35% — denominator suppression |
| Hostile / Complaint | 15–20% minimum | < 2% — conflict eradication occurring |

## **2.3 — Activity Count Cross-Check**

For all leads marked Lost or Not Interested: check the logged activity count (calls made, messages sent).

* If >30% of terminal leads have 0 or 1 activity logged: inbox clearance marking confirmed
* If activity logs show 15–20 "Call Attempted" entries within a 2-minute window: phantom logging confirmed
* If call durations are uniformly zero or blank: cross-check against telephony CDRs

***Request telephony CDR export if available. Mismatch between CRM call logs and telecom records is definitive proof of phantom activity.***

## **2.4 — Conversion Rate Plausibility**

Calculate implied CPL: Ad Spend ÷ Total Logged Leads. Compare to benchmark CPL for their specialty and city.

If implied CPL is 3–5x higher than benchmark: leads have been deleted. The denominator has been suppressed.

Cross-check: Compare CRM "Converted" count against HMS/billing software unique new patients for the same period. Divergence confirms either high-intent exclusion or CRM used as vanity dashboard.

## **2.5 — Lead Age Distribution**

Pull lead age distribution by created\_date. Look at the follow-up stage specifically:

* What percentage of follow-up leads are older than 30 days with zero recent activity?
* What percentage of all activity is concentrated on leads <2 days old?

If >80% of activity is on <15% of the database (the newest leads): recency bias confirmed. This is actually a positive signal for Valence Ops — it means a large, unworked mid-funnel exists. Document the size of this cohort.

## **2.6 — Phone Number Quality Audit**

Run a phone number formatting check on the full dataset before any other analysis:

* Count numbers that are not 10 digits after stripping +91, 0, country codes
* Count numbers that appear to be landlines (starting with 044, 080, 022, etc.)
* Count duplicate numbers appearing under different names
* Check for SIM recycling risk: flag all leads with zero bidirectional communication in >90 days

***Any lead with zero bidirectional contact in >90 days is SIM recycling risk. Do not send medical content to these numbers without identity verification first (DPDP liability).***

# **PHASE 3: Shadow Behavior Confirmation**

*These checks confirm specific behavioral patterns that cause system misfires. Run after Phase 1 and 2 are complete.*

## **3.1 — The Personal Phone Check**

Ask to observe a coordinator respond to a live incoming inquiry during your site visit. Watch which device they reach for. If they reach for a personal mobile rather than an official device or desktop portal: personal silo confirmed.

Secondary check: Look at the CRM data for leads that jump from "New" to "Converted" with zero intermediate activity and no nurturing lag. A perfectly cylindrical funnel with no drop-off stages is a silo signature.

## **3.2 — The Owner Conversation Check**

Ask the owner: "Are there any patient types you personally handle — high-value cases, referrals from doctor friends, sensitive cases — where you manage the conversation directly?"

Then cross-check: Pull the CRM's procedure distribution. Compare to revenue by procedure from billing. If a high-revenue procedure is underrepresented in the CRM relative to billing: owner exclusion is active on that segment.

## **3.3 — The Narrative Divergence Test**

Ask the owner and coordinator the same three questions separately:

* "If a patient messages your WhatsApp right now, how quickly will someone personally respond?"
* "How many times does your team try to reach a lead before moving on?"
* "Where do you keep track of patients you need to follow up with?"

Owner answers represent the policy. Coordinator answers represent the reality. Where they diverge is where your automation needs to compensate. Document the gap explicitly — this becomes the emotional anchor of your proposal.

## **3.4 — Converted-But-Still-Lost Check**

Run a VLOOKUP or name-match between the last 60 days of paying patients (from billing/HMS) and the CRM database. Any paying patient still marked "Lost" or "Not Interested" in the CRM confirms the owner-conversion attribution failure. These patients must be suppressed from any reactivation sequence immediately.

## **3.5 — WhatsApp Quality Rating Check**

Before any campaign planning, check the clinic's WhatsApp Business Manager dashboard:

* Green rating: proceed to normal campaign planning
* Yellow rating: conservative warm-up required — 20–40 messages/day for 7 days minimum before scaling
* Red rating: rehabilitation sequence required before any reactivation campaign. Full reactivation delayed by 14–21 days.

Also check: current messaging tier limit (250/day vs 1,000/day vs 10,000/day). Campaign volume must stay within tier limits or a ban is triggered.

## **3.6 — Staff Turnover Data Gap Check**

Ask: "Has any coordinator or front desk staff left in the last 12 months?" If yes: identify the departure date. Pull all leads assigned to the former employee. Check activity velocity before and after departure date. A sudden drop to zero on departure date confirms the turnover black hole. These leads are orphaned — prime reactivation targets but require cold-outreach framing, not continuation framing.

# **PHASE 4: Audit Output & Deployment Decision**

## **4.1 — Data Trust Score**

After completing all checks, assign a Data Trust Score:

| **Score** | **What It Means** | **Deployment Decision** |
| --- | --- | --- |
| A | No shadow patterns confirmed. Dataset represents >80% of actual pipeline. Timestamps reliable. | Proceed to Revenue Leakage Audit immediately. |
| B | 1–3 shadow patterns confirmed. Dataset is partial but usable. Key segments may be missing. | Proceed with remediation notes. Flag missing segments in audit output. Set correct expectations on reactivation volume. |
| C | 4–6 shadow patterns confirmed. Dataset is significantly incomplete or manipulated. | Remediate before proceeding. Fix phone numbers, reconcile billing vs CRM, suppress converted patients. Re-run Phase 2 checks after remediation. |
| D | 7+ shadow patterns confirmed. Dataset cannot be trusted as a basis for diagnosis. | Renegotiate scope. The audit deliverable must include a data reconstruction phase before reactivation can begin. This changes the timeline and potentially the pricing conversation. |

## **4.2 — Shadow Audit Summary Template**

Document your findings in this format before moving to the Revenue Leakage Audit:

* Data Trust Score: [A / B / C / D]
* Confirmed shadow patterns: [list by name]
* Estimated missing pipeline: [number of leads not visible in dataset]
* SIM recycling risk cohort: [number of leads flagged]
* Converted-but-lost patients suppressed: [number]
* WhatsApp quality rating: [Green / Yellow / Red] — current tier: [250 / 1K / 10K]
* Deployment risk: [Proceed / Remediate First / Renegotiate Scope]
* Key narrative divergence points: [owner said X, coordinator said Y]