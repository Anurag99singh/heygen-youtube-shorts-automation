# Current production policy — 13 November 2026
The user explicitly removed ALL manual script, plan, first-ten-test and final-publication approval gates. Run unattended: daily production starts at **10:00 IST**; daily trend research stays at 09:00 IST. Pick topic, write script, generate through HeyGen Video Agent, monitor, validate and schedule through Buffer plugin for **next day 09:00 IST** without asking for routine approval.
YouTube description means text BELOW the posted video: store it in V (YouTube Description), title in U. Never append description, hashtags, source footer or a separate caption section to the spoken script/HeyGen Doc. Pass V only to Buffer text. On-video subtitle settings remain unchanged.
Retain strict 30–35s measured duration, fixed voice d35557f1a8e24de1a34345cf58a30e51, selected/default avatar resolved by exact look ID, factual/visual QA and duplicate prevention. E/I/P are legacy review fields, not eligibility gates; do not write APPROVE pretending a human reviewed. Respect an explicit future user HOLD/REVISE/stop.
VID-001 was manually removed from Buffer by the user. Keep its recorded IDs as history, mark it intentionally cancelled in notes, exclude it from production/reconciliation retries and do not recreate it. It must not block new daily videos.

---
name: heygen-youtube-shorts
description: Create, review, render, validate and schedule 30–35-second AI-software news YouTube Shorts through Google Docs, a single Google Sheet, HeyGen Video Agent and Buffer. Strict voice, script, title, plan-approval, idempotency and media-transfer rules.
---

# HeyGen → YouTube Shorts Automation

Use this skill when the user asks to prepare, revise, review, generate, monitor, schedule or publish the **AI-software news YouTube Shorts pipeline**. Do not silently switch to a different video pipeline. This file is the entry point for ChatGPT Work/cloud tasks. Read the related reference files before performing writes.

## Authoritative references
- **Live video queue:** https://docs.google.com/spreadsheets/d/1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8/edit (spreadsheet ID `1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8`)
- Tabs: `Video Queue`, `Avatar Library`, `Settings`, `Grok Style Reference`.
- **Writing style master:** https://docs.google.com/document/d/1aXsLa5MABozi7aBf4vbSmnplPdPyd6mNyRcb-JCkd0w/edit (IBM & Microsoft Imagine Enterprise example).
- **Existing approved VID-001 script:** https://docs.google.com/document/d/1rcD_N0vOmVrCb0c7zzn6_xx_sojnz8aUcxhfAkfAMTc/edit.
- **Daily AI Trend Briefing:** existing trend-research skill at https://github.com/Anurag99singh/consistent-explainer-videos-v3/blob/main/skills/ai-trend-briefing/SKILL.md; existing 9:00 AM IST daily task. Do not duplicate it.
- **Buffer destination:** YouTube channel `6af6b7bf62b70b94b016cbe8` (Anurag Singh), organization `6ae9a6a24fd7379ad1914b12`, timezone `Asia/Kolkata`.
- **HeyGen:** private Anshul avatar group `34dc0457ca4d4eeb92dae5a9e5180bd8`. Immutable intended voice: **Anshul -- 17**, `d35557f1a8e24de1a34345cf58a30e51`.

## Production invariants
1. User wants **YouTube Shorts only**, via **Buffer**, and no additional paid orchestration service.
2. **HARD runtime range: 30.0–35.0 seconds inclusive**, including intro, transitions and ending. Aim for 32–34 seconds. Reject measured output below 30 or above 35; do not round it into range. Applies to new videos; preserve VID-001's previously approved pilot history.
3. **Four-scene simple prompt**: Hook (avatar); Feature/Announcement (B-roll); Why it matters (B-roll); CTA (avatar). Each scene has **VISUAL**, **NARRATION** (exact spoken lines), **DELIVERY DIRECTION**. Use short plain English matching the IBM/Microsoft prompt's clarity, not a technical document.
4. Topic-specific **title persists from first to last frame**, across *all scenes and transitions*. One line, ~44 pt, just below top edge, no face overlap.
5. 9:16 portrait; realistic, specifically relevant B-roll; natural gestures; subtle music; **no generated subtitles, captions or watermark**.
6. Maintain **fixed voice ID `d35557f1a8e24de1a34345cf58a30e51`** across every scene. This is NOT `Anshul 2026` (`7b9850bf42ed4d999891709c3f7341a9`). Check actual rendered scene voice IDs. Group default voice has already been updated but is not proof the render used it.
7. User chooses an avatar per row in **Video Queue column G**. Resolve its exact look ID from **Avatar Library**; never guess from duplicate look names.
8. **One Google Doc per video, edited in place.** Revisions always update the **same URL in column D**. Do not create v2/v3 duplicate Docs. Avoid putting voice IDs, workflow internals, review instructions, HTTP/API details, or scheduler explanations inside the HeyGen script.
9. Sources must be credible and link to original coverage/product announcements. Focus on **AI software**: agents, AI apps, generated media, coding tools, software models/research. No generic robotics roundup.
11. **Never claim a publication/schedule until Buffer confirms an actual post ID and status**. Never create duplicate videos/posts as retries.

## Runbook
1. **Read live queue**. Use one row per India production date. Resume existing rows idempotently. Do not start another render for an active/completed job. A previously scheduled or separately blocked older row does not block the next day's topic draft. Read Settings and avatar mapping.
5. During render, store HeyGen session ID in N, render start timestamp in Y, actual video ID in a J cell note, and `RENDERING` in L. Monitor the existing job; never resubmit the prompt merely to check status.
6. As soon as HeyGen completes, **store permanent HeyGen viewing page in J** (e.g. `https://app.heygen.com/videos/VIDEO_ID`), measured runtime in Z and evaluation in T, set L `VIDEO READY` or `BLOCKED`. Check actual length, all scene narration text, voice IDs, avatar IDs, captions, and visible persistent title when possible. If a check cannot be verified, state that explicitly.
8. Verify Buffer account/channel, check duplicate post by M and Buffer list_posts, then use `schedulingType: "automatic"`, `mode: "customScheduled"` and `dueAt` equal to production date W + one day at **09:00 IST** (persisted in X), YouTube `categoryId: "28"`, prepared U title + V source-backed caption; mark `isAiGenerated` appropriately. Record Buffer post ID in M and `SCHEDULED` in L. Only fill K with **actual YouTube URL after sent** and reconcile status `PUBLISHED`.
9. Read [daily timing](references/daily-timing.md) for the 09:00 production start, exact next-day slot, research race, persistent 10+ minute render monitoring and missed-slot handling. Read [YouTube descriptions](references/youtube-caption.md) before drafting U/V. The daily and hourly tasks must never require a Buffer browser login.
10. Final user update: exact step performed, links, checked/unchecked quality gates and any blocker. **No claims of background progress** unless an Automation was actually created and verified.

## Additional references (read relevant file)
- [Prompt template](references/script-template.md)
- [YouTube title/caption standard](references/youtube-caption.md)
- [Daily dates and render monitoring](references/daily-timing.md)
- [Sheet schema and state machine](references/sheet-schema.md)
- [HeyGen voice, approval and QA](references/heygen-controls.md)
- [Buffer upload and scheduling](references/buffer-publishing.md)
- [Schedulers and Cloud handoff](references/schedulers.md)
- [Test 1 incident and accepted exception](references/test-1-incident.md)

## Source of truth precedence
The current user's instructions set policy; live Google Sheet and connected service records determine actual state; repository notes are dated operational guidance. The repository explains **how** to work; it is never the sole evidence that a video has rendered or a post was scheduled. Preserve credentials outside GitHub.
