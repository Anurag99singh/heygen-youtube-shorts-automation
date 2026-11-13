# Current production policy — 13 November 2026
The user explicitly removed ALL manual script, plan, first-ten-test and final-publication approval gates. Run unattended: daily production starts at **10:00 IST**; daily trend research stays at 09:00 IST. Pick topic, write script, generate through HeyGen Video Agent, monitor, validate and schedule through Buffer plugin for **next day 09:00 IST** without asking for routine approval.
YouTube description means text BELOW the posted video: store it in V (YouTube Description), title in U. Never append description, hashtags, source footer or a separate caption section to the spoken script/HeyGen Doc. Pass V only to Buffer text. On-video subtitle settings remain unchanged.
Retain strict 30–35s measured duration, fixed voice d35557f1a8e24de1a34345cf58a30e51, selected/default avatar resolved by exact look ID, factual/visual QA and duplicate prevention. E/I/P are legacy review fields, not eligibility gates; do not write APPROVE pretending a human reviewed. Respect an explicit future user HOLD/REVISE/stop.
VID-001 was manually removed from Buffer by the user. Keep its recorded IDs as history, mark it intentionally cancelled in notes, exclude it from production/reconciliation retries and do not recreate it. It must not block new daily videos.

# Sheet mapping and state machine

**Sheet URL:** https://docs.google.com/spreadsheets/d/1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8/edit

## Tabs
- `Video Queue` — the single operational ledger. Every Short gets a stable ID such as VID-002.
- `Avatar Library` — display label and exact HeyGen look ID; distinguish duplicate avatar names.
- `Settings` — production rules, fixed voice, current source links, Buffer channel.
- `Grok Style Reference` — old video narration reference; the IBM/Microsoft master Google Doc is authoritative for the full prompt style.

## Video Queue columns

| Col | Key | Meaning |
| --- | --- | --- |
| A | ID | Stable idempotency key (VID-001, VID-002, ...) |
| B | Topic | Fact-checked AI-software story |
| C | Source Article | Original authoritative article URL |
| D | Script Link | **Same Google Doc URL across revisions** |
| F | Feedback | Human instructions for revision |
| G | Avatar Look | Unique AVxx label; map through Avatar Library |
| H | HeyGen Plan | Session URL only when valid, never a misleading stopped session |
| J | Final Video | Permanent HeyGen viewing-page URL as soon as video completes |
| K | YouTube URL | Actual public YouTube video after Buffer reports published |
| L | Status | Workflow state |
| M | Buffer Post ID | Durable ID from Buffer create_post; primary duplicate guard |
| N | HeyGen Session ID | Active or completed HeyGen session identifier |
| O | Approved Plan Version | Version/identifier of plan actually approved |
| P | Plan Approval # | Approved test number during 10-test review phase |
| Q | Media MP4 URL | Optional **stable** direct public HTTPS MP4 for connector publishing; do not store expiring signed URL as stable |
| R | Buffer Channel ID | YouTube ID `6af6b7bf62b70b94b016cbe8` |
| S | Published Timestamp | Verified time after successful posting |
| T | Publishing Error | Failure cause or factual QA observations, user-readable |

## Added posting and timing fields
| Col | Key | Meaning |
| --- | --- | --- |
| U | YouTube Title | Approved publishing title; separate from script Doc |
| V | YouTube Description | Approved description, source and 2–3 hashtags |
| W | Production Date | India date YYYY-MM-DD; daily idempotency key |
| X | Target Publish At | Production date + 1 at 09:00 Asia/Kolkata, timezone explicit |
| Y | Render Started At | Real submission timestamp, not estimated completion |
| Z | Duration Seconds | Measured actual runtime; new videos pass only 30.0–35.0 inclusive |

U/V are reviewed with E. Store actual video ID as a J cell note until permanent view URL is available. W/X are assigned once, not recalculated on each hourly retry. Keep all earlier columns, validations and records intact. A missing Buffer post retains M as duplicate guard and L=BLOCKED.

The Sheet **can have dropdown validations** for E, G, I, L. Inspect live cell metadata before updating.

## Status transitions
```
READY
  -> WRITING
  -> SCRIPT REVIEW --(E=REVISE)--> WRITING (same Doc)
  -> PLAN REVIEW --(I=REVISE)--> HEYGEN PLAN (same session)
  -> RENDERING
  -> VIDEO READY (J filled with permanent view URL)
  -> SCHEDULED (M filled with Buffer post ID)
  -> PUBLISHED (K verified YouTube URL)
```
- `BLOCKED` on failed QA, missing usable direct video asset or insufficient source validity, unavailable authentication, incorrect voice, render timeout, etc. Leave precise reason in T. User may explicitly accept a one-off exception; record that exception but never change a global quality rule.
- `PLAN PAUSED` allowed if HeyGen UI countdown was actually paused. Never fake a pause based on a stop-session API.
- Mark `RENDERING` only after a real session and job ID exist.
- Mark `VIDEO READY` the moment HeyGen finishes and J is written, even if Buffer upload remains pending; if publishing is blocked, put that reason in T (or L=BLOCKED after documenting video completion).
- Do not write K merely because Buffer scheduled a post; URL comes from actual publishing confirmation.

## Duplicate and reconciliation policy
- Before **HeyGen generation**, inspect N and H, HeyGen sessions and J. Do not regenerate existing finished video.
- Before **Buffer create_post**, inspect M and Buffer channel posts for the video title, ID and media link. Avoid duplicates on retries, network timeouts, hourly checks and multiple cloud workers.
- After **Buffer create_post**, write M and L immediately. Then reconcile status to K/S later.
- **Single row per finished video**. Never create a new row for a revision.
