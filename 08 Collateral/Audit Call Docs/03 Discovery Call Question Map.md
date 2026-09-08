---
date_created: 2026-06-25
date_modified: 2026-06-25
status: reference
---
**VALENCE OPS**

**Discovery Call
Question Map**

*The owner and coordinator answer the same questions. Where their answers diverge is where the system needs to compensate.*

Document 03 of 3 | Pre-Deployment Infrastructure | Elective Clinic Vertical

Version 1.0 | Bengaluru, India | June 2026

# **How This Document Works**

This is not a generic discovery script. Every question here serves a forensic purpose — it surfaces a specific shadow pattern or confirms/rules out a specific failure mode.

The structure: ask the owner first, then ask the coordinator the same question separately. Document both answers. Where they diverge, that gap becomes a deployment requirement. It also becomes the emotional anchor of your proposal — the owner hearing their own gap described back to them is the most powerful diagnostic moment in the sales process.

| **Color** | **Meaning** |
| --- | --- |
| ASK (dark blue) | Who to ask this question to — Owner, Coordinator, or both |
| LISTEN FOR | The specific answer patterns that indicate a shadow behavior is active |
| TRIGGER (amber) | The answer that means you need to run an additional check |
| → CHECK (red) | The specific data check or follow-up question to run when triggered |

# **BLOCK A: Speed and Response Reality**

*Purpose: Identify the personal phone silo, shared inbox chaos, and after-hours coverage gaps.*

**QA1 If a patient messages your clinic WhatsApp right now — this exact minute — how quickly will someone personally respond? Not an auto-reply. An actual human message.**

|  |  |
| --- | --- |
| **Ask** | Ask Owner first, then Coordinator separately. |
| **Listen for** | Owner says under 5 minutes. Coordinator says 'I check in the morning' or 'whoever is at the desk picks it up.' Any pause, laugh, or qualification from the owner. The phrase 'it depends.' |
| **Trigger** | **Owner claims <5 min but coordinator describes a batch or shared process.** |
| **→ Check** | Check timestamp data for average first-response lag. Ask to see the WhatsApp inbox live during the call. Count how many linked devices are active on the account. |

**QA2 When a patient calls your clinic number and nobody picks up — what happens to that call?**

|  |  |
| --- | --- |
| **Ask** | Ask Owner, then ask the receptionist or coordinator. |
| **Listen for** | The answer 'nothing' or 'they call back if they want.' Any mention of a missed call log that lives on the physical phone only. No callback protocol described. |
| **Trigger** | **No systematic callback process described. Missed calls tracked only on the device call history.** |
| **→ Check** | This confirms inbound call leads are disappearing. Flag as a missing channel. Ask how many calls per day go unanswered on average. |

**QA3 Are there any patient types — high-value cases, doctor referrals, VIP patients — where you personally handle the conversation?**

|  |  |
| --- | --- |
| **Ask** | Ask Owner only. |
| **Listen for** | Any 'yes' answer. The phrase 'I prefer to handle those myself.' A mention of replying 'late at night' or 'on my personal phone.' |
| **Trigger** | **Owner confirms personal handling of any lead segment.** |
| **→ Check** | Run the procedure distribution cross-check: compare CRM procedure mix to billing procedure mix. Any underrepresented high-ticket procedure in the CRM confirms the owner exclusion silo. Flag this cohort as outside system scope unless owner agrees to migrate. |

# **BLOCK B: Follow-Up Reality**

*Purpose: Confirm follow-up intensity, inbox clearance marking, and phantom activity logging.*

**QB1 Take your last 20 leads that didn't convert. How many times did your team try to reach each one before moving on?**

|  |  |
| --- | --- |
| **Ask** | Ask Owner first, then Coordinator separately. |
| **Listen for** | Owner says 3–5 times. Coordinator says 1–2 times or cannot give a number. Either answer 'it depends on the lead' or 'I try a few times.' The phrase 'we follow up until they respond.' |
| **Trigger** | **Owner and coordinator give different numbers. Coordinator cannot give a specific number.** |
| **→ Check** | Pull activity count data from the dataset. Calculate mean and median attempts per lead before terminal status. If mean is <2 — the coordinator's answer is the truth. This becomes a core finding. |

**QB2 Where do you personally keep track of which patients you still need to follow up with?**

|  |  |
| --- | --- |
| **Ask** | Ask Coordinator directly. Do not ask the owner first. |
| **Listen for** | Any answer that is not the official CRM — a personal notebook, a sticky note, a WhatsApp message to themselves, a separate Excel sheet, 'in my head.' The phrase 'I just remember.' |
| **Trigger** | **Any answer describing a system outside the CRM.** |
| **→ Check** | Confirm parallel source is active. Ask to see this personal tracking system. Cross-reference 5 leads from it against the CRM. Any leads present in the personal system but not the CRM confirms the shadow CRM exists. |

**QB3 When a lead doesn't respond after a few attempts, how do you mark them in the system?**

|  |  |
| --- | --- |
| **Ask** | Ask Coordinator. |
| **Listen for** | 'Not interested' or 'lost' applied immediately after 1–2 attempts. 'I clear them out to keep the inbox clean.' Any mention of bulk-marking. The phrase 'if they don't respond they're probably not interested.' |
| **Trigger** | **Coordinator describes marking leads terminal after <3 genuine attempts.** |
| **→ Check** | Pull stage distribution data. Filter for leads marked Lost/Not Interested and cross-reference activity count. If >30% have 0–1 activity log, inbox clearance marking is confirmed at scale. |

# **BLOCK C: Data and System Reality**

*Purpose: Confirm parallel data sources, batch entry, and missing channels.*

**QC1 If I asked you right now — how many leads did you receive last month across all channels — could you give me an exact number?**

|  |  |
| --- | --- |
| **Ask** | Ask Owner. |
| **Listen for** | A round number given confidently ('about 200'). A pause followed by 'I'd have to check.' Any mention of needing to 'add up' different sources. The phrase 'it depends on how you count it.' |
| **Trigger** | **Owner cannot give a number without calculation, or gives a round estimate.** |
| **→ Check** | This confirms the owner does not have a single source of truth. It also means their stated metrics during the sales conversation are estimates, not data. Set up the audit as the first time they will have an accurate number. |

**QC2 Walk me through what happens between a patient sending their first WhatsApp message and that patient's information getting into your system.**

|  |  |
| --- | --- |
| **Ask** | Ask Coordinator. Ask them to walk through it step by step, not describe the policy. |
| **Listen for** | Any gap in the sequence. 'We write it down first.' 'I enter it later when I have time.' 'If they seem serious I add them.' Any mention of a step that happens before the system entry. The phrase 'I don't always enter them right away.' |
| **Trigger** | **Any gap described between first contact and system entry.** |
| **→ Check** | This is the batch entry detection question. The gap they describe is where leads are falling out. Document the sequence verbatim — it becomes the architecture brief for your automation design. |

**QC3 What channels are you getting inquiries from? For each one — where does that inquiry actually land?**

|  |  |
| --- | --- |
| **Ask** | Ask both Owner and Coordinator separately. |
| **Listen for** | Owner lists channels confidently. Coordinator describes a different or narrower set. Any channel the owner mentions that the coordinator does not handle. Any mention of Instagram DMs going to a personal phone. Any channel where 'it just comes in' with no clear landing point. |
| **Trigger** | **Coordinator describes fewer channels than owner, or any channel landing on a personal device.** |
| **→ Check** | Map each channel: what is the actual intake point. Any channel landing on a personal device is a missing data source. Estimate its volume using platform-specific metrics (Instagram insights, Google Business calls) and add to the missing pipeline calculation. |

# **BLOCK D: Appointment and No-Show Reality**

*Purpose: Establish whether appointment data exists, confirm no-show rates, and identify recovery gaps.*

**QD1 When a patient books a consultation — what exactly do you do between that booking and the appointment time?**

|  |  |
| --- | --- |
| **Ask** | Ask Coordinator. |
| **Listen for** | The word 'nothing' or a long pause. 'We just wait for them to come in.' A single WhatsApp message sent manually with no follow-up. Any description that ends before the appointment day. |
| **Trigger** | **No systematic pre-appointment communication described.** |
| **→ Check** | This is the no-show prevention gap. Confirm by asking the no-show rate directly: 'Out of every 10 consultations booked, how many don't show up?' Any number above 3 confirms the opportunity. Document it as a recoverable slot calculation. |

**QD2 When a patient doesn't show up for their consultation — what's the first thing that happens?**

|  |  |
| --- | --- |
| **Ask** | Ask Coordinator. |
| **Listen for** | 'Nothing.' 'We move on.' 'We call them sometimes.' Any answer where the clinic is passive. 'If they want to reschedule they'll reach out.' A response time of hours or days before any follow-up. |
| **Trigger** | **No structured, time-bound recovery sequence described.** |
| **→ Check** | Confirm recovery gap. Ask: 'In the last 30 days, how many no-shows did your team personally follow up with within 2 hours?' The answer anchors the no-show recovery ROI calculation. |

**QD3 When a patient attends a consultation but doesn't book a procedure — what happens next?**

|  |  |
| --- | --- |
| **Ask** | Ask both Owner and Coordinator. |
| **Listen for** | 'The doctor recommends and if they're interested they book.' 'We send them a quote.' Any absence of a structured follow-up sequence on the quote. The phrase 'they come back if they decide.' |
| **Trigger** | **No structured quote follow-up process described.** |
| **→ Check** | This is the quote graveyard check. Ask: 'In the last 30 days, how many treatment quotes did your team send out? Of those, how many received a structured follow-up within 48 hours?' Document the gap — this is your Proposal Graveyard diagnostic moment. |

# **BLOCK E: Staff and Incentive Reality**

*Purpose: Understand commission structure, turnover history, and whether automation will be adopted or resisted.*

**QE1 How does your team get paid for conversions — flat salary, commission, or a mix?**

|  |  |
| --- | --- |
| **Ask** | Ask Owner. |
| **Listen for** | Any commission structure tied to individual closing. 'They get a percentage of the first payment.' High commission percentages on high-ticket procedures. |
| **Trigger** | **Commission tied to individual closing.** |
| **→ Check** | Flag pipeline hoarding risk. Coordinators with individual commission incentives will resist automation that attributes conversions to the system rather than to them. Design the routing logic to explicitly give coordinators credit for reactivated leads they close. |

**QE2 Has any coordinator or front desk staff left in the last 12 months?**

|  |  |
| --- | --- |
| **Ask** | Ask Owner. |
| **Listen for** | Any 'yes.' Multiple departures. A casual 'yes we've had some turnover.' |
| **Trigger** | **Any staff departure confirmed.** |
| **→ Check** | Run the turnover black hole check: identify departure date, pull all leads assigned to former staff, check activity velocity before and after. Size the orphaned cohort. These leads are isolated as a separate reactivation target — cold-outreach framing, not continuation framing. |

**QE3 If I told you this system will send messages to leads automatically — what's your concern about that?**

|  |  |
| --- | --- |
| **Ask** | Ask Owner and Coordinator separately. |
| **Listen for** | Owner says 'patients might not like it' or 'I worry about the tone.' Coordinator says 'what if I'm already talking to them?' or 'will they know it's automated?' Any mention of not wanting patients to feel like they're getting spam. |
| **Trigger** | **Any concern about collision between automation and live coordinator conversations.** |
| **→ Check** | This surfaces the biggest adoption risk. The concern is real and valid. Document it. The answer determines how you design the handoff logic — the system must visibly pause automation when a coordinator is in active conversation, and coordinators need to see this in the dashboard. |

# **Post-Call: Narrative Divergence Summary**

After completing both the owner and coordinator conversations, fill in this comparison:

| **Question** | **Owner Said** | **Coordinator Said** |
| --- | --- | --- |
| First response time |  |  |
| Follow-up attempts per lead |  |  |
| Where follow-ups are tracked |  |  |
| What triggers a lead marked lost |  |  |
| Channels receiving leads |  |  |
| What happens after no-show |  |  |
| Quote follow-up process |  |  |
| Personal phone usage |  |  |

***Every row where the answers differ is a deployment requirement. It is also a line in your proposal. The owner needs to hear the gap described in their own data — not as a criticism of their team, but as the exact system failure your automation is designed to fix.***