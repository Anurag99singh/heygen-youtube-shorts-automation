---
name: heygen-youtube-shorts
description: Create, review, render, validate and schedule <=30-second AI-software news YouTube Shorts through Google Docs, a single Google Sheet, HeyGen Video Agent and Buffer. Strict voice, script, title, plan-approval, idempotency and media-transfer rules.
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
2. **HARD runtime limit: 30.0 seconds**, including any intro, transitions and ending. Aim for 27–29 seconds; reject longer output.
3. **Four-scene simple prompt**: Hook (avatar); Feature/Announcement (B-roll); Why it matters (B-roll); CTA (avatar). Each scene has **VISUAL**, **NARRATION** (exact spoken lines), **DELIVERY DIRECTION**. Use short plain English matching the IBM/Microsoft prompt's clarity, not a technical document.
4. Topic-specific **title persists from first to last frame**, across *all scenes and transitions*. One line, ~44 pt, just below top edge, no face overlap.
5. 9:16 portrait; realistic, specifically relevant B-roll; natural gestures; subtle music; **no generated subtitles, captions or watermark**.
6. Maintain **fixed voice ID `d35557f1a8e24de1a34345cf58a30e51`** across every scene. This is NOT `Anshul 2026` (`7b9850bf42ed4d999891709c3f7341a9`). Check actual rendered scene voice IDs. Group default voice has already been updated but is not proof the render used it.
7. User chooses an avatar per row in **Video Queue column G**. Resolve its exact look ID from **Avatar Library**; never guess from duplicate look names.
8. **One Google Doc per video, edited in place.** Revisions always update the **same URL in column D**. Do not create v2/v3 duplicate Docs. Avoid putting voice IDs, workflow internals, review instructions, HTTP/API details, or scheduler explanations inside the HeyGen script.
9. Sources must be credible and link to original coverage/product announcements. Focus on **AI software**: agents, AI apps, generated media, coding tools, software models/research. No generic robotics roundup.
10. Use approval gates: **E = script approval; I = actual HeyGen plan approval for the first 10 tests unless user explicitly overrides for an individual test.** Never treat script approval as approval to render or publish. The user explicitly allowed VIDEO-001 to render and approved its wrong voice *for that video only*; do not generalize the exception.
11. **Never claim a publication/schedule until Buffer confirms an actual post ID and status**. Never create duplicate videos/posts as retries.

## Runbook
1. **Read live queue**. Choose one relevant `READY` row; skip rows with an active HeyGen session, a finished video, a Buffer Post ID, or a pending approval. Read Settings and avatar mapping.
2. **Research/source** topic, draft a simple <=30s four-scene HeyGen prompt in the row's existing Google Doc (create one document ONLY for a brand-new row); write document link to D and set status `SCRIPT REVIEW`. Wait for E `APPROVE`; on `REVISE`, edit the same Doc using F feedback and reset E to `PENDING`.
3. **Before HeyGen**, confirm selected look, fixed voice, and plan mode. For first 10 tests use HeyGen **Plan / Chat mode** in an attended Work browser. The connected `video_agent_generate` action starts generation and does NOT expose a reliable Plan Mode/pause toggle. Do not use it for an unapproved plan-stage handoff. **Stopping the session is not a plan pause**; prior test demonstrated it loses the blueprint.
4. Once the actual HeyGen plan is visible, store session URL in H; set status `PLAN REVIEW`; wait for I `APPROVE`; on `REVISE`, improve plan **in the same HeyGen session**. For an explicit user override to go straight to rendering, record that per-row, submit **only the approved Doc body**, not a preamble, with selected `avatarId`.
5. During render, store HeyGen session ID in N and `RENDERING` in L. Monitor the existing job; never resubmit the prompt merely to check status.
6. As soon as HeyGen completes, **store permanent HeyGen viewing page in J** (e.g. `https://app.heygen.com/videos/VIDEO_ID`), runtime and evaluation in T, set L `VIDEO READY` or `BLOCKED`. Check actual length, all scene narration text, voice IDs, avatar IDs, captions, and visible persistent title when possible. If a check cannot be verified, state that explicitly.
7. **Buffer handoff — plugin only.** Use the connected Buffer plugin, never a Buffer browser session. After publication approval and QA, fetch a fresh direct MP4 from HeyGen `get_video` and use `assets: [{video: {url: freshVideoUrl}}]` in Buffer `create_post`, Automatic / Add to Queue. A signed HeyGen URL is temporary, but was successfully accepted by Buffer for VID-001 on 13 November 2026. Validate its expiry against the actual queue slot plus a safety margin; do not call it permanent, store it in GitHub, or leave it in Sheet Q as durable media. Read `references/buffer-publishing.md` for expiry and post-verification rules. A video page/private Drive preview is invalid media. Verify the returned post through `get_post`; missing media or an error is BLOCKED, never scheduling success.
8. Verify Buffer account/channel, check duplicate post by M and Buffer list_posts, then use automatic scheduling, addToQueue (unless user specifies another slot), YouTube `categoryId: "28"`, title + short source-backed description; mark `isAiGenerated` appropriately. Record Buffer post ID in M and `SCHEDULED` in L. Only fill K with **actual YouTube URL after sent** and reconcile status `PUBLISHED`.
9. Final user update: exact step performed, links, checked/unchecked quality gates and any blocker. **No claims of background progress** unless an Automation was actually created and verified.

## Additional references (read relevant file)
- [Prompt template](references/script-template.md)
- [Sheet schema and state machine](references/sheet-schema.md)
- [HeyGen voice, approval and QA](references/heygen-controls.md)
- [Buffer upload and scheduling](references/buffer-publishing.md)
- [Schedulers and Cloud handoff](references/schedulers.md)
- [Test 1 incident and accepted exception](references/test-1-incident.md)

## Source of truth precedence
Live Google Sheet + connector status > connected HeyGen/Buffer records > user instruction in current chat > repository references. The repository explains **how** to work; it is never the sole evidence that a video has rendered or a post was scheduled. Preserve credentials outside GitHub.
