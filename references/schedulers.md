# Scheduled workers

Use existing tasks; never create duplicates. The live Sheet and connected service records take precedence over dated setup notes.

| Worker | Task ID | Schedule | Route |
| --- | --- | --- | --- |
| Daily AI Trends for Shorts | `6af078ea40608191a2adc9c6e9ff0ae4` | Daily 09:00 IST | Independent research skill in v3 |
| Daily AI Short Script | `6af6d39cf50c8191a087adb5bd1376d4` | Daily approximately 10:00 IST | Docs + Sheet; draft only |
| HeyGen Buffer Handoff | `6af6c74482fc8191bd1608e67cdea0ee` | Hourly | Status/QA, Buffer plugin scheduling and publication reconciliation |

All three were enabled in the latest setup inspection. Recheck actual Automations status before relying on cached state. Scheduling documentation does not prove that a task ran successfully.

## Script worker
Read root SKILL.md and references/script-template.md plus sheet-schema.md. Use existing daily AI Trend Briefing output. Prepare a fresh source-backed AI-software topic only when no existing item is awaiting review, render, media transfer or scheduling. Edit the same Doc for REVISE; create one Doc only for a new row. Set E=PENDING and L=SCRIPT REVIEW and send the link. Do not generate HeyGen videos, spend credits or schedule Buffer in this task.

## Hourly worker prompt
```text
Run the AI-software YouTube Shorts QUEUE / HEYGEN / BUFFER RECONCILIATION phase. Read https://github.com/Anurag99singh/heygen-youtube-shorts-automation/blob/main/SKILL.md plus references/sheet-schema.md, heygen-controls.md and buffer-publishing.md through connected GitHub. Inspect live Google Sheet 1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8. Process eligible rows idempotently. Check existing HeyGen sessions WITHOUT starting another render; on completion write permanent HeyGen page to J immediately and verify <=30 seconds, exact narration, selected avatar and scene voice IDs. Future fixed voice: d35557f1a8e24de1a34345cf58a30e51. VID-001 has an explicit one-off older-voice exception and is ALREADY SCHEDULED: Buffer post 6af6de6cfe8cb9dc190a4a45, due 2026-11-13T12:06:00Z (17:36 IST). Reconcile that exact post; never regenerate or create a duplicate. For newly authorized videos, schedule using the BUFFER PLUGIN ONLY, Automatic / Add to Queue, channel 6af6b7bf62b70b94b016cbe8, org 6ae9a6a24fd7379ad1914b12. Do not open or require Buffer browser sessions. Fetch fresh direct MP4 from HeyGen get_video; signed sources were accepted in the verified pilot but remain temporary. Require source expiry to cover the expected AND actual returned queue slot plus at least 24 hours; do not call signed URLs permanent or store them in GitHub/Sheet Q. Never use a viewing page/private Drive preview as media. Check Sheet M and Buffer posts for duplicates before create_post. Immediately save returned M post ID and L=SCHEDULED, then get_post to confirm video asset, actual dueAt, YouTube metadata and no error; record unresolved media/expiry errors honestly on the same post without duplicate retries. For scheduled posts, use get_post; on actual sent status and returned YouTube link write K, S and L=PUBLISHED; on error record reason and BLOCKED. Preserve E script approval and I first-ten-test HeyGen PLAN approval; script approval alone does not authorize render. HeyGen plan review may still need attended Work browser; that is separate from plugin-only Buffer scheduling. Only notify on new completion, successful scheduling/publication or a meaningful NEW blocker; avoid repetitive hourly notices.
```

## Production constraints
- Retain first-ten-test HeyGen plan approval and script review. Keep initial HeyGen plans attended; do not silently render through an unsafe connector route.
- **Buffer scheduling is plugin-only.** No Buffer browser login or local browser upload is required for the verified fresh direct-MP4 route.
- Signed media is temporary. Fetch fresh, verify queue-slot validity and saved media, then reconcile actual publication. Do not store signed URLs as durable assets.
- Do not regenerate VID-001 or create a second Buffer post for it.
- Polling cannot provide instant completion events. Hourly is the supported recurring cadence; no seconds-level countdown control.
- A worker's completion is not publication evidence. Confirm Buffer sent status and actual YouTube external link before K/S/PUBLISHED.
- An enabled task does not establish that its inherited environment can access every service. Record failures accurately and avoid duplicate writes.

## Verified pilot
Buffer plugin scheduling succeeded on 13 November 2026: post `6af6de6cfe8cb9dc190a4a45`, due **17:36 IST**, Automatic / Add to Queue. `get_post` verified video asset, Short settings and scheduled status without error. Publication is not yet confirmed.

The canonical workflow lives here. Daily research stays at https://github.com/Anurag99singh/consistent-explainer-videos-v3/blob/main/skills/ai-trend-briefing/SKILL.md .
