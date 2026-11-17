---
name: heygen-youtube-shorts
description: Three-worker YouTube Shorts workflow with manual script and video approval using one Google Sheet, the script-writing skill, HeyGen plugin and Buffer plugin.
---

# YouTube Shorts workflow

## Required HeyGen route and subtitles
Always use **HeyGen Video Agent** for this pipeline. Send the full production Doc including scene visuals, B-roll, persistent title, callouts, narration and editing directions. Never use Avatar Video, presenter-only rendering, or narration-only payloads as a substitute. Video Agent may vary wording/voice: request fidelity and inspect actual output; report deviations for human review rather than silently switching routes.

**Burned-in, speech-synchronized subtitles are required** throughout avatar and B-roll scenes. They are distinct from the YouTube description in V. Before video review, verify visible subtitles in the exported video. For an existing correct render missing subtitles, continue the same Video Agent session with a subtitle-only edit; preserve footage, audio, title, timing and all scene assets. Keep previous output IDs in checkpoint history and require human review of the updated export. Never schedule the uncaptioned source.

## One workbook only
https://docs.google.com/spreadsheets/d/1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8/edit

This is the ONLY spreadsheet used by this video pipeline. Pick supplied topics from its **Video Queue** tab, not from another workbook, research automation or repository. Do not invent or research replacement topics when no eligible supplied topic exists. Verify claims using the source article in C; source verification is not topic discovery. Read **Settings** for current HeyGen voice/group/default avatar, Buffer organization/channel and publishing time; resolve selected G through **Avatar Library**. Ignore Grok Style Reference and old master-prompt links: the [script-writing skill](skills/script-writer/SKILL.md) and its [template](skills/script-writer/template.md) own writing style.

Read metadata, exact headers, bounded rows and validation before edits. Preserve all unrelated cells, formulas, formatting, history and tabs. Latest user instructions and this workflow supersede old unattended/plan-review settings. No generated APPROVE values. Blank, PENDING, HOLD or unrecognized decisions never authorize generation or publishing.

## Sheet controls
| Column | Purpose |
| --- | --- |
| A/B/C | Stable video ID / supplied topic / original source article |
| D | Script Google Doc: one per video, edit in place |
| E | Script Review: PENDING / APPROVE / REVISE; human sets APPROVE |
| F | Human feedback for the current script or video revision |
| G | Selected avatar look label; resolve exact ID in Avatar Library |
| H/N | HeyGen session URL / session ID |
| I | Video Review: PENDING / APPROVE / REVISE; human sets APPROVE |
| J/K | Completed HeyGen viewing page / actual published YouTube URL |
| L | Status (states below) |
| M | Current Buffer post ID; primary duplicate guard |
| O | Workflow Checkpoint: persistent JSON approval bindings, claims and attempt history |
| P/Q | Legacy history / optional stable MP4 only; never store expiring URL as durable media |
| R/S/T | Buffer channel used / actual published timestamp / QA, errors and review notes |
| U/V | Separate YouTube title / description below video; never spoken |
| W/X/Y/Z | Production date / approved future publication target / actual render start / measured duration |

## Exactly three pipeline workers
### 1. Topic and script — daily 10:00 Asia/Kolkata
Read ONLY eligible supplied rows in Video Queue. Pick the first READY or unstarted row with B and C populated and no Doc, active/completed render, post or cancellation. An ID alone with no topic is not eligible. Prepare at most one new script per daily run; use W plus checkpoint to avoid a second new selection on a rerun of the same date. Resume a claimed WRITING row instead of duplicating it.

**Before any draft/revision, read [skills/script-writer/SKILL.md](skills/script-writer/SKILL.md) and [template.md](skills/script-writer/template.md).** Fill only dynamic slots; retain fixed opening/overall directions. Use [scripts/script_contract.py](scripts/script_contract.py) to render/check when Python is available, otherwise perform the same checks explicitly. Keep 65–80 spoken words as drafting guidance and final measured runtime 30–35s, target 32–34. Verify the source, edit existing D or create one Doc only if absent, and read it back. Prepare U and V separately: truthful 40–65-character title (max100); 45–80-word description plus source URL and 2–3 relevant hashtags including #Shorts. No source footer/description/hashtags in Doc narration.

Set E=PENDING, I=PENDING, L=SCRIPT REVIEW, W=production date; save current script binding in O and notify with D. Stop. This worker NEVER calls HeyGen or Buffer, never approves itself, and never reads another topic spreadsheet.

### 2. HeyGen completion — hourly
Read only existing RENDERING rows with persisted session/video IDs. Query the SAME session until video ID exists, then get that video. Pending, even after 10+ minutes, is not failure. Never generate or stop a render to poll. Persist actual progress, no tight polling or instant-webhook promises.

On completion save J permanent viewing page, Z measured seconds and real video ID in O. Check exact narration, every scene voice ID, avatar IDs, 9:16, persistent title throughout transitions, relevant distinct B-roll, speech-synchronized burned-in subtitles and no watermark. Final runtime must be 30.0–35.0 inclusive, no rounding. Missing proof/failure -> BLOCKED/T, preserve output; no automatic paid regeneration.

Passing output -> I=PENDING, L=VIDEO REVIEW; save review binding in O of video ID, J, approved script hash, G, U, V and duration; notify with J for HUMAN review. This worker never sets APPROVE, never rewrites the script and never schedules Buffer.

### 3. Approval and revision actions — hourly
This is the ONLY worker allowed to submit HeyGen or schedule Buffer. Re-read the current row and Doc immediately before consequential writes. Handle at most one generation action per run and keep at most one active render across this queue. Review waiting, cancelled, pending and unchanged rows quietly.

**Script approval:** eligible L=SCRIPT REVIEW and E=APPROVE. Compare current Doc text, source/topic, resolved avatar and U/V with the current script binding in O. If changed since offered for review, reset E=PENDING, update binding and request fresh review; never apply an old approval to changed text. If matched, record the human approval binding and claim before submitting. Verify live group voice is Anshul -- 17 / d35557f1a8e24de1a34345cf58a30e51; resolve exact look from live G/Library or Settings default, never guess. Submit only D body through HeyGen Video Agent plugin with exact avatarId. No extra Plan approval stage. Immediately persist H/N/Y, available video ID and L=RENDERING; clear I to PENDING for the new output. Unknown submission outcome -> reconcile existing job before retry, never blindly submit again. No Buffer action at this stage.

**Script revision:** L=SCRIPT REVIEW and E=REVISE with nonempty F. Deduplicate feedback against the checkpoint. Apply requested changes through the script-writing skill to the SAME D, read back, update binding, E=PENDING and L=SCRIPT REVIEW. Missing feedback -> request it once; do not spend credits.

**Video approval:** eligible L=VIDEO REVIEW, I=APPROVE, passing QA and current review binding matches exact video/J/script/avatar/U/V. If anything changed, reset I=PENDING and request review of current content. Bind the human approval before publishing. Read live Buffer destination and check R/M and existing target-slot posts. No post may be created from script approval alone.

Use current live publishing policy: default next day after W at 09:00 Asia/Kolkata, or explicit future target X; persist X once. If approval arrives after X, BLOCKED and ask for a new future target; no immediate publish/silent rollover. Fetch fresh direct MP4 from existing HeyGen get_video, never video-page/Drive-preview URL. For signed media require expiry beyond X+24h, refresh or BLOCKED. Do not commit signed URLs. Buffer plugin only: schedulingType=automatic, mode=customScheduled, dueAt=UTC(X), text=V, YouTube title=U, categoryId=28, public, not made for kids, appropriate AI disclosure. Check M/list_posts before create; reuse/reconcile existing post. Save M promptly, get_post verify correct channel, actual video asset, exact text/title, dueAt and scheduled/no-error status before L=SCHEDULED. Unknown create outcome -> reconcile, not recreate. Keep M on errors as duplicate guard.

**Video revision:** I=REVISE with nonempty F. First revoke any unsent scheduled post by moving that SAME post to draft and verifying draft status. Preserve historical video/session/post IDs in O. Edit the same script Doc for the requested visual/narration changes via the writer, reset E/I=PENDING and L=SCRIPT REVIEW. User must approve revised script before another paid render, and approve the new output before scheduling. Record feedback/version so repeated polls never create repeated revisions. Never overwrite an active job or remove evidence of old outputs. Only clear current job/post fields for a new attempt after preserving them in O; reconcile old pending/uncertain operations first.

**Publication and revocation:** reconcile existing M. Sent + actual external YouTube URL alone permits K/S/PUBLISHED. Errors -> BLOCKED/T, preserve M. If I changes from APPROVE to PENDING/REVISE/HOLD on an unsent scheduled post, move it to draft and verify before further work; do not modify an already-sent publication. Changes to approved content also revoke an unsent schedule and require new review. Preserve published history. Never fabricate a public URL.

## Checkpoints and state
O stores JSON: phase/claim timestamp; current script/review fingerprints; human-approved fingerprints; processed feedback/version; current video ID; and previous attempts with job/post IDs. Fingerprint = SHA256 of sorted-key UTF-8 JSON with exact current values (script text, topic/source, resolved avatar, U/V; add video ID/J/duration for video review). Persist/read back claims before external actions. Claims and IDs prevent a repeated worker from duplicating a write. If an operation has uncertain outcome, BLOCKED with evidence until reconciled; no blind timeout retry. Keep previous attempts even after revision. Do not treat legacy plan APPROVE values as new video approvals: only a newly offered VIDEO REVIEW with its recorded binding can be approved.

READY -> WRITING -> SCRIPT REVIEW -> RENDERING -> VIDEO REVIEW -> SCHEDULED -> PUBLISHED. REVISE returns to SCRIPT REVIEW with fresh human approval. BLOCKED records exact recoverable failures; no automatic render retry loop. Skip all CANCELLED/HOLD rows and specifically cancelled VID-001 forever, retaining its history.

No other workbook, research worker, external style document, config file or workflow reference is required. Do not create duplicate workers. Scheduler prompts select one role above; they must not combine drafting with generation or completion checks with publishing. Report only verified changes and actionable new blockers. Repository edits or automated checks do not prove a video rendered or published.
