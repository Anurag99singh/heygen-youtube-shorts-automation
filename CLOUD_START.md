# Start in ChatGPT Work / GPT Cloud

Read [SKILL.md](SKILL.md), [sheet schema](references/sheet-schema.md), [HeyGen controls](references/heygen-controls.md), [Buffer publishing](references/buffer-publishing.md) and [schedulers](references/schedulers.md).

Canonical private repository: https://github.com/Anurag99singh/heygen-youtube-shorts-automation
Live queue: https://docs.google.com/spreadsheets/d/1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8/edit

## Resume prompt
Read the canonical skill and relevant references through connected GitHub. Inspect the live Google Sheet first. Reconcile existing video/session/post IDs before creating anything. Schedule only through the **Buffer plugin**, not a Buffer browser session. Fetch a fresh direct MP4 from HeyGen, check its expiry covers the actual queue slot plus margin, schedule Automatic / Add to Queue, then retrieve the post to verify media and status. Do not treat temporary URLs as permanent hosting or commit them to GitHub.

VID-001 is already scheduled: Buffer Post ID `6af6de6cfe8cb9dc190a4a45`, due **13 November 2026, 17:36 IST**, `2026-11-13T12:06:00Z`. Check that exact post; never regenerate or reschedule it as a new post. Its 23.1967-second video and one-off older voice were approved. Write the actual YouTube URL to K and published time to S only after Buffer confirms sent.

For future videos use voice **Anshul -- 17**, `d35557f1a8e24de1a34345cf58a30e51`, <=30 seconds, four scenes, full-time title and selected avatar. Honor script E and first-ten-test HeyGen plan I approvals. Edit the same Google Doc for revisions. HeyGen plan review can still require an attended browser; this is separate from Buffer scheduling.

## Existing workers
- Daily AI Trends for Shorts: 09:00 IST; skill stays in v3.
- Daily AI Short Script: approximately 10:00 IST, draft only.
- HeyGen Buffer Handoff: hourly; plugin-based scheduling and sent/error reconciliation.

## Setup
Connect GitHub, Google Drive/Sheets/Docs, HeyGen and Buffer. No Buffer browser sign-in is required for the verified plugin route. Do not store passwords, tokens or signed media URLs in the repository.
