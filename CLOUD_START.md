# Start in ChatGPT Work / GPT Cloud

**This task is for the HeyGen → Buffer → YouTube Shorts pipeline.**

## One paste to resume
```text
Read the production skill at:
https://github.com/Anurag99singh/heygen-youtube-shorts-automation/blob/main/SKILL.md

Follow its references, especially sheet-schema, heygen-controls, buffer-publishing and schedulers. The operational ledger is:
https://docs.google.com/spreadsheets/d/1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8/edit

Inspect the live Sheet before doing anything. Use existing IDs and approvals; do not duplicate completed videos, scripts or Buffer posts. For new videos always use Anshul -- 17 (voice ID d35557f1a8e24de1a34345cf58a30e51), simple four-scene script, persistent title and <=30 seconds.

First reconcile VID-001: completed video in Sheet J; user accepted that video's different voice, but it still needs Buffer publishing. Download finished MP4 from HeyGen via Work browser and upload it to Buffer's connected YouTube channel in automatic queue mode. Do not pass expiring HeyGen MP4 URL to connector. Once Buffer confirms a scheduled post, update Sheet M and L, then K only after actual publication.

For future videos apply script approval E and plan approval I for first ten tests. Edit the same Google Doc on revisions and use Plan/Chat mode safely in HeyGen's UI. Report exactly what was completed and any outstanding blocker.
```

## Important setup
- In Work, connect/authorize **GitHub, Google Drive/Sheets/Docs, HeyGen and Buffer**, plus the **browser/cloud computer** for local video upload.
- The built-in **Chat-mode** browser connector is read-only. It cannot download a file and click Buffer upload. The existing Buffer connector requires a permanent direct video URL.
- GitHub source is the **private `Anurag99singh/heygen-youtube-shorts-automation` repository**, so the cloud environment must have access to it.
- Never request secret tokens in a document or commit tokens to GitHub.

## Actual scheduled tasks
- Existing daily AI Trend Briefing at 09:00 IST.
- Daily AI Short Script — enabled, about 10:00 IST; draft only, approval required.
- HeyGen Buffer Handoff — enabled, hourly; status sync, validate and attempt publishing if media-transfer route is available.
- No sub-hourly HeyGen countdown monitor: work in Plan mode with the user present for first ten tests.

## Completed pilot
VID-001 finished **23.1967 s**; permanent HeyGen viewing URL is saved in Sheet J. One-video exception accepts original wrong voice. The group default was corrected for future videos. **Buffer upload has not been verified**, so do not claim VID-001 scheduled.

## Buffer prepared draft for VID-001
An unscheduled Buffer Idea exists with id `6af6d4257438174bb4e4ad74`. Use its prepared title/caption when attaching the downloaded MP4 via browser. It is NOT yet a scheduled YouTube post. First check Buffer channel for an existing post before creating another.
