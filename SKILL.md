---
name: heygen-youtube-shorts
description: Run the AI-software YouTube Shorts pipeline using the dedicated script-writing skill, Google Sheets/Docs, HeyGen and Buffer.
---

# YouTube Shorts pipeline

## Read only what the phase needs
- Identity, destination, timing and policy: [config/workflow.json](config/workflow.json).
- **Before writing or revising any script: [script-writing skill](skills/script-writer/SKILL.md) and its [fixed template](skills/script-writer/template.md). Mandatory; do not improvise another script format.**
- Queue columns: [sheet schema](references/sheet-schema.md).
- Generation, monitoring, QA and publishing: [workflow](references/workflow.md).
- Separate posting copy: [YouTube title/description](references/youtube-caption.md).

## Execute in order
1. Read the live queue and Settings. Reconcile existing date, topic, session/video and post IDs before writing. One row per Asia/Kolkata production date W; assign next-day 09:00 target X once. Skip cancelled VID-001 forever. Respect explicit HOLD/REVISE/stop. Never duplicate an active/completed render or uncertain Buffer write.
2. Pick one verified AI-software story from the existing 09:00 trend research; if unavailable, verify a fresh original source using its existing Sources directory. Deduplicate source/event/topic. An older scheduled or independently blocked row does not block today's draft; at most one render active.
3. **Invoke skills/script-writer/SKILL.md.** Build the four-scene explanation, fill only the fixed template's dynamic fields, render/check the contract, and write/read back the same Google Doc D. Keep the opening and overall directions unchanged except template slots. Target 65–80 spoken words and 32–34 seconds; measured final runtime must be 30–35 inclusive. Draft title U and description V separately.
4. Follow references/workflow.md to resolve the exact selected/default avatar look and fixed voice; submit only the Doc production prompt through HeyGen Video Agent. Persist job IDs immediately. Poll the same job; never generate to check status.
5. Save completed video URL and measured duration immediately; check narration, voice, avatar, persistent title, visuals and runtime. BLOCKED for failures or unverified required checks; no blind paid regeneration loop.
6. After passing QA, use Buffer plugin only, automatic/customScheduled at X. Check duplicates and source validity, verify returned post through get_post, then record M/L. Only actual sent confirmation permits K/S/PUBLISHED. Missed slot -> BLOCKED; no immediate publish or silent rollover.

## Authorization and test mode
Standing production policy is unattended: no manual script/plan/first-ten/final approval gates; E/I/P are legacy history, never fabricate APPROVE. Preserve explicit HOLD/REVISE/stop. Updating this repository does not enable paused automations. Check actual task state, not cached configuration.

When the user requests a **script-only test**, complete step 3 and stop before generation or scheduling. This repository update itself is not a request to spend HeyGen credits or publish a test video.

Current user instructions set policy; live Sheet/service records determine state. Never claim completion, scheduling or publication without evidence. Keep credentials and signed MP4 URLs out of GitHub.
