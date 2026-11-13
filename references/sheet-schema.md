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
| E | Script Review | PENDING / APPROVE / REVISE |
| F | Feedback | Human instructions for revision |
| G | Avatar Look | Unique AVxx label; map through Avatar Library |
| H | HeyGen Plan | Session URL only when valid, never a misleading stopped session |
| I | Plan Review | PENDING / APPROVE / REVISE |
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

The Sheet **can have dropdown validations** for E, G, I, L. Inspect live cell metadata before updating.

## Status transitions
```
READY
  -> WRITING
  -> SCRIPT REVIEW --(E=REVISE)--> WRITING (same Doc)
                  --(E=APPROVE)--> HEYGEN PLAN
  -> PLAN REVIEW --(I=REVISE)--> HEYGEN PLAN (same session)
                 --(I=APPROVE)--> RENDERING
  -> RENDERING
  -> VIDEO READY (J filled with permanent view URL)
  -> SCHEDULED (M filled with Buffer post ID)
  -> PUBLISHED (K verified YouTube URL)
```
- `BLOCKED` on failed QA, missing stable video asset, unavailable authentication, incorrect voice, render timeout, etc. Leave precise reason in T. User may explicitly accept a one-off exception; record that exception but never change a global quality rule.
- `PLAN PAUSED` allowed if HeyGen UI countdown was actually paused. Never fake a pause based on a stop-session API.
- Mark `RENDERING` only after a real session and job ID exist.
- Mark `VIDEO READY` the moment HeyGen finishes and J is written, even if Buffer upload remains pending; if publishing is blocked, put that reason in T (or L=BLOCKED after documenting video completion).
- Do not write K merely because Buffer scheduled a post; URL comes from actual publishing confirmation.

## Duplicate and reconciliation policy
- Before **HeyGen generation**, inspect N and H, HeyGen sessions and J. Do not regenerate existing finished video.
- Before **Buffer create_post**, inspect M and Buffer channel posts for the video title, ID and media link. Avoid duplicates on retries, network timeouts, hourly checks and multiple cloud workers.
- After **Buffer create_post**, write M and L immediately. Then reconcile status to K/S later.
- **Single row per finished video**. Never create a new row for a revision.
