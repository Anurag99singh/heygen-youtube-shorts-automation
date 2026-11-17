# Sheet mapping and state machine

**Sheet URL:** https://docs.google.com/spreadsheets/d/1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8/edit

## Tabs
- `Video Queue` — the single operational ledger. Every Short gets a stable ID such as VID-002.
- `Avatar Library` — display label and exact HeyGen look ID; distinguish duplicate avatar names.
- `Settings` — production rules, fixed voice, current source links, Buffer channel.
- `Grok Style Reference` — historical only; skills/script-writer/SKILL.md is the current writing authority.

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

E/I/P are legacy review history, not production gates. U/V are checked with the script. Store actual video ID as a J cell note until permanent view URL is available. W/X are assigned once, not recalculated on each hourly retry. Keep all earlier columns, validations and records intact. A missing Buffer post retains M as duplicate guard and L=BLOCKED.

The Sheet **can have dropdown validations** for E, G, I, L. Inspect live cell metadata before updating.

## Current states
READY -> WRITING -> RENDERING -> VIDEO READY -> SCHEDULED -> PUBLISHED.
Use BLOCKED/T for concrete failures; respect user HOLD/REVISE and revise the same Doc before rendering. Do not overwrite an active/completed job's bound script on retry. Legacy review columns/validations and all historical records remain intact. Only real job IDs permit RENDERING; only a confirmed Buffer post permits SCHEDULED; only actual sent confirmation permits K/S/PUBLISHED.

## Duplicate and reconciliation policy
- Before **HeyGen generation**, inspect N and H, HeyGen sessions and J. Do not regenerate existing finished video.
- Before **Buffer create_post**, inspect M and Buffer channel posts for the video title, ID and media link. Avoid duplicates on retries, network timeouts, hourly checks and multiple cloud workers.
- After **Buffer create_post**, write M and L immediately. Then reconcile status to K/S later.
- **Single row per finished video**. Never create a new row for a revision.
