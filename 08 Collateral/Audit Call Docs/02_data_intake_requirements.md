---
date_created: 2026-08-13
date_modified: 2026-08-13
status: reference
---
**VALENCE OPS**

**Data Intake
Requirements**

> ## ⛔ STAGE-4 DOCUMENT — DO NOT SEND BEFORE A SIGNED PILOT
>
> **Re-staged 2026-08-04, header corrected 2026-08-13.** This document previously instructed *"hand this to the clinic before the audit."* That is now wrong and it was the most dangerous sentence in this folder: it asks a clinic that has agreed to nothing to hand two strangers a raw CRM export, Meta access, WhatsApp history, billing counts and a staff list. Sending it early ends conversations.
>
> **Correct use:** delivered live, in the 45-minute screen-share setup session at Stage-4 kickoff, after a yes. Not emailed. Not a document the clinic fills in alone.
>
> **At Stage 3 (findings), the ask is exactly ONE item, producible in under ten minutes.** In order of preference: last 90 days of enquiries from wherever they're kept → a screenshot of WhatsApp Business stats → last month's no-show count, however rough → five minutes with the coordinator. See `SALES_MOTION.md` §3/Stage 3 and `sales-motion/04-findings-and-rollout.md`.
>
> The document itself is good. It was sitting at the wrong point in the sequence.

Document 02 of 3 | Stage-4 Onboarding | Elective Clinic Vertical

Version 1.1 | Bengaluru, India | re-staged Aug 2026

# **Why We Need All of This**

The accuracy of your Revenue Leakage Findings depends entirely on whether the data we work from reflects your actual pipeline. Most clinics have data in multiple places — a CRM, a spreadsheet, a WhatsApp inbox, a billing system. We need all of it. A partial dataset produces wrong numbers, and wrong numbers mean a system that misfires.

Everything listed below is required before we begin the audit. If a source does not exist for your clinic, note that explicitly — that absence is itself a finding.

# **ITEM 1: Lead Database Export**

Export your complete lead database — every lead ever recorded, not just recent or active ones. Do not filter by status, date, or coordinator.

## **Preferred format**

* Raw CSV or XLSX export directly from your CRM (GoHighLevel, Zoho, HubSpot, etc.)
* If using Google Sheets: share edit access or export as CSV — do not manually copy-paste
* If using WhatsApp manually: export chat history as .txt files for key patient threads

## **Required fields**

| **Field** | **What We're Looking For** | **If Missing...** |
| --- | --- | --- |
| Lead name | Identity matching across systems | Flag — may indicate parallel source |
| Phone number(s) | All numbers on record, including alternates | Critical gap — cannot run WhatsApp campaign |
| Lead source / channel | Where did the inquiry originate | Channel blindness confirmed if missing |
| Created date / timestamp | When the lead first entered the system | Cannot measure speed-to-lead |
| Current status / stage | New, Follow-up, Lost, Converted, etc. | Cannot assess pipeline distribution |
| Last contacted date | When was the last actual contact attempt | Cannot identify dead pipeline age |
| Assigned coordinator | Which staff member owns this lead | Cannot detect orphaned pipelines |
| Activity count / log | Number of calls, messages, attempts | Cannot confirm follow-up reality |
| Procedure of interest | What procedure did they enquire about | Cannot segment reactivation by intent |
| Consultation date (if booked) | Appointment timestamp | Cannot run no-show analysis |
| Consultation outcome | Showed / No-show / Rescheduled / Converted | Cannot assess show-up rate |

***Important: Do not send a cleaned or filtered version of your data. We need the raw export including blank fields, formatting errors, and duplicate entries. These are findings, not problems to fix before sending.***

# **ITEM 2: Ad Platform Access (Read-Only)**

We need read-only access to your advertising dashboards to cross-check lead volumes against what was captured in your system.

## **Required**

* Meta Business Suite / Ads Manager — read-only user access
* Google Ads — read-only access if running search campaigns
* Google Business Profile — admin or manager access to see call history and message volume

## **Specifically we will pull**

* Leads Generated (Meta) vs. Leads Logged (CRM) for the last 90 days
* Click-to-WhatsApp click volume vs. WhatsApp conversations initiated
* Google Business call click volume vs. calls logged in your system

If access cannot be shared, export the following screenshots: Meta Ads Manager results column showing "Leads" metric by month for the last 3 months. Google Business Insights showing calls, messages, and direction requests for the last 3 months.

# **ITEM 3: WhatsApp Business Account Details**

## **WhatsApp Business App users**

* Export the last 90 days of chat history for your primary clinic number as a .txt backup
* Note how many staff members are linked to the account via WhatsApp Web
* Note whether any staff members use personal numbers to contact patients

## **WhatsApp Business API users**

* Share your WhatsApp Manager dashboard screenshot showing: quality rating (Green/Yellow/Red), current messaging tier, and template approval status
* Export the last 30 days of template message delivery reports
* Note which platform hosts your API (Meta directly, or a BSP like Interakt, Wati, AiSensy)

***If your quality rating is Yellow or Red, do not attempt to send any campaign messages before the audit is complete. Doing so risks a permanent ban that would delay deployment significantly.***

# **ITEM 4: Billing / HMS Data**

We need a count — not detailed patient records — of new paying patients for the last 90 days by procedure type.

## **What to export**

* Total new patient count per month for the last 3 months
* Breakdown by procedure type if available (hair transplant, IVF, cosmetic, dental, etc.)
* This does not need to include names, amounts, or personal health data — aggregate counts are sufficient

We use this to cross-check against the CRM's "Converted" count. If billing shows 80 new patients but the CRM shows 20 conversions, we know referral and walk-in patients are being excluded from your lead tracking.

# **ITEM 5: Staff Information**

## **Current staff list**

* Name and role of every person who handles patient inquiries (receptionist, coordinator, doctor)
* Whether each person uses an official clinic number or personal number for patient contact
* Which CRM / spreadsheet login they use (note if multiple people share a login)

## **Former staff (last 12 months)**

* Name and departure date of any coordinator or front desk staff who left
* Note whether their leads were reassigned and to whom

We flag all leads assigned to former staff as an orphaned pipeline — these are reactivation targets but require different messaging framing.

# **ITEM 6: Appointment Data (If Separate from Lead Data)**

If appointments are tracked in a separate system (a booking tool, Google Calendar, paper register), export or photograph the last 90 days.

* Date and time of each booked consultation
* Show / No-show outcome for each slot
* Procedure type for each appointment
* Source of the booking (which channel did the lead come from)

If no appointment tracking exists in any digital form, note this explicitly. It is a finding — and the no-show recovery system will be the first structured tracking this clinic has ever had.

# **What Happens After You Send This**

Once we receive all items above, the audit takes 48–72 hours. You will receive:

* A Revenue Leakage Findings document — one page, your numbers, the three biggest leak points, and a recoverable pipeline estimate
* A deployment readiness summary — what needs to be in place before the system goes live
* A recommended first step with a timeline and expected outcome

If any item above is unavailable, send what you have and note what is missing. Missing items become part of the findings — they are never a reason to delay the audit.