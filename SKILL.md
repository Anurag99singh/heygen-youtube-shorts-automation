---
name: heygen-youtube-shorts
description: Three-worker YouTube Shorts workflow with manual script and video approval using one Google Sheet, the script-writing skill, HeyGen and Gmail, ending at an approved distribution handoff.
---

# YouTube Shorts workflow

## Required HeyGen route and subtitles
Always use **HeyGen Video Agent** for this pipeline. Send the full production Doc including scene visuals, B-roll, persistent title, callouts, narration and editing directions. Never use Avatar Video, presenter-only rendering, or narration-only payloads as a substitute. Video Agent may vary wording/voice: request fidelity and inspect actual output; report deviations for human review rather than silently switching routes.

**Burned-in, speech-synchronized subtitles are required** throughout avatar and B-roll scenes. They are distinct from the YouTube description in V. Before video review, verify visible subtitles in the exported video. For an existing correct render missing subtitles, continue the same Video Agent session with a subtitle-only edit; preserve footage, audio, title, timing and all scene assets. Keep previous output IDs in checkpoint history and require human review of the updated export. Never schedule the uncaptioned source.

## One workbook only
https://docs.google.com/spreadsheets/d/1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8/edit

This account NEVER schedules through Buffer. It ends at a verified email handoff.

This is the ONLY spreadsheet used by this video pipeline. Pick supplied topics from its **Video Queue** tab, not from another workbook, research automation or repository. Do not invent or research replacement topics when no eligible supplied topic exists. Verify claims using the source article in C; source verification is not topic discovery. Read **Settings** for current HeyGen voice/group/default avatar, handoff recipient/folder/email settings; resolve selected G through **Avatar Library**. Ignore Grok Style Reference and old master-prompt links: the [script-writing skill](skills/script-writer/SKILL.md) and its [template](skills/script-writer/template.md) own writing style.

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
| M | Retired Buffer post ID; historical evidence only |
| O | Workflow Checkpoint: persistent JSON approval bindings, claims and attempt history |
| P/Q | Legacy history / optional stable MP4 only; never store expiring URL as durable media |
| R/S | Retired publishing history, hidden; never write new publishing data |
| T | QA, errors and review notes |
| U/V | Separate YouTube title / description below video; never spoken |
| W/X/Y/Z | Production date / retired publication target / actual render start / measured duration |

## Handoff schema additions
AA Instagram Caption; AB Instagram Hashtags; AC Final MP4 Drive Link; AD Distribution Approval (PENDING/APPROVE/REVISE/HOLD); AE Email Message ID; AF Email Sent At UTC; AG Handoff Error. Keep A:Z positions and historical values; hide retired/technical columns rather than deleting audit history. K/M/P/R/S/X are retired historical fields. No default publishing target from this account.

## Exactly three pipeline workers
### 1. Topic and script — daily 10:00 Asia/Kolkata
Read ONLY eligible supplied rows in Video Queue. Pick the first READY or unstarted row with B and C populated and no Doc, active/completed render, post or cancellation. An ID alone with no topic is not eligible. Prepare at most one new script per daily run; use W plus checkpoint to avoid a second new selection on a rerun of the same date. Resume a claimed WRITING row instead of duplicating it.

**Before any draft/revision, read [skills/script-writer/SKILL.md](skills/script-writer/SKILL.md) and [template.md](skills/script-writer/template.md).** Fill only dynamic slots; retain fixed opening/overall directions. Use [scripts/script_contract.py](scripts/script_contract.py) to render/check when Python is available, otherwise perform the same checks explicitly. Keep 65–80 spoken words as drafting guidance and final measured runtime 30–35s, target 32–34. Verify the source, edit existing D or create one Doc only if absent, and read it back. Read [caption skill](skills/caption-writer/SKILL.md); prepare U/V/AA/AB separately for distribution review. No source footer/description/hashtags in Doc narration.

Set E=PENDING, I=PENDING, AD=PENDING, L=SCRIPT REVIEW, W=production date; save current script binding in O and notify with D. Stop. This worker NEVER calls HeyGen or Buffer, never approves itself, and never reads another topic spreadsheet.

### 2. HeyGen completion — hourly
Read only existing RENDERING rows with persisted session/video IDs. Query the SAME session until video ID exists, then get that video. Pending, even after 10+ minutes, is not failure. Never generate or stop a render to poll. Persist actual progress, no tight polling or instant-webhook promises.

On completion save J permanent viewing page, Z measured seconds and real video ID in O. Check exact narration, every scene voice ID, avatar IDs, 9:16, persistent title throughout transitions, relevant distinct B-roll, speech-synchronized burned-in subtitles and no watermark. Final runtime must be 30.0–35.0 inclusive, no rounding. Missing proof/failure -> BLOCKED/T, preserve output; no automatic paid regeneration.

Passing output -> I=PENDING, L=VIDEO REVIEW; save review binding in O of video ID, J, approved script hash, G, U, V and duration; notify with J for HUMAN review. This worker never sets APPROVE, never rewrites the script and never schedules Buffer.

### 3. Approval and revision actions — hourly
This is the ONLY worker allowed to submit HeyGen or send the approved distribution email. Re-read the current row and Doc immediately before consequential writes. Handle at most one generation action per run and keep at most one active render across this queue. Review waiting, cancelled, pending and unchanged rows quietly.

**Script approval:** eligible L=SCRIPT REVIEW and E=APPROVE. Compare current Doc text, source/topic, resolved avatar and U/V with the current script binding in O. If changed since offered for review, reset E=PENDING, update binding and request fresh review; never apply an old approval to changed text. If matched, record the human approval binding and claim before submitting. Verify live group voice is Anshul -- 17 / d35557f1a8e24de1a34345cf58a30e51; resolve exact look from live G/Library with an explicit per-row G selection; blank G waits, never guess. Submit only D body through HeyGen Video Agent plugin with exact avatarId. No extra Plan approval stage. Immediately persist H/N/Y, available video ID and L=RENDERING; clear I to PENDING for the new output. Unknown submission outcome -> reconcile existing job before retry, never blindly submit again. No Buffer action at this stage.

**Script revision:** L=SCRIPT REVIEW and E=REVISE with nonempty F. Deduplicate feedback against the checkpoint. Apply requested changes through the script-writing skill to the SAME D, read back, update binding, E=PENDING and L=SCRIPT REVIEW. Missing feedback -> request it once; do not spend credits.

**Video approval:** I=APPROVE on VIDEO REVIEW with passing QA binds the exact reviewed video; it does not authorize email or publishing. Read the caption skill, prepare U/V/AA/AB, save the exact original final MP4 to the Settings handoff Drive folder via fresh HeyGen download (not a preview page or expiring signed URL), verify file MIME video/mp4, size and recipient access. Persist its stable Drive link in AC. If upload/access cannot be verified, BLOCKED/T; never claim handoff ready. Preserve the existing output and do not regenerate. Offer L=DISTRIBUTION REVIEW, AD=PENDING and record a distribution fingerprint in O. Notify the owner to inspect video and both copies.

**Distribution email:** This same hourly worker checks ready rows; no fourth scheduler. Only L=DISTRIBUTION REVIEW with I=APPROVE, AD=APPROVE by a human, passing QA, nonempty U/V/AA/AB/AC and matching offered binding permits sending. Fingerprint SHA256 sorted-key JSON of ID, exact video ID/J, Drive file ID/version/size/checksum, U/V/AA/AB, topic/source, recipient and Sheet ID. Verify actual Drive metadata/access before offering and again before send; if bytes/version/copy/recipient changes reset AD=PENDING and request fresh review. AD blank/PENDING/HOLD never authorizes email. No inherited approval from old rows. Never create Buffer posts, schedule, publish or reconcile Buffer from this account. Boss account owns all platform distribution.

Read Settings `Handoff recipient`, `Handoff folder`, `Email handoff enabled`. Missing/unverified recipient/folder or disabled sending -> wait/report setup blocker once. Email only the configured recipient; current installation owner authorized j.anshul@gmail.com. Use Gmail account verified in Settings. Before send re-read row and exact approval; persist/read back O claim with unique handoff key ID+distribution fingerprint. Search Sent for exact recipient, subject and handoff key before sending. Subject: INSTAGRAM READY. Body: Video ID, handoff key, exact Sheet row link, stable original MP4 link, platforms YouTube Shorts + Instagram Reels, and instruction to read approved U/V/AA/AB and deduplicate both platform posts by video ID+handoff key. No credentials or other queue rows in body. Use Gmail send tool. Persist real returned message ID AE and UTC sent timestamp AF promptly, L=HANDOFF SENT; read back. Unknown send outcome -> AG=UNCERTAIN/T, reconcile Sent before any retry; never blindly resend. Never mark sent from a draft or claim alone. Missing scheduled Gmail/Drive access blocks; quiet when unchanged.

**Revisions:** E=REVISE at SCRIPT REVIEW or I=REVISE with F feedback: deduplicate feedback, use same Doc and required writer/template, preserve all attempts and reset E/I/AD=PENDING, L=SCRIPT REVIEW. Require fresh script approval before another render. Copy-only feedback at distribution review uses caption skill, leaves approved video untouched, resets AD=PENDING and updates offered binding. Changed video/script revokes distribution approval. Never edit/render automatically from old feedback. If an email already went out, preserve AE/AF and history; mark HANDOFF INVALIDATED and notify owner that downstream may have acted; no automatic replacement/cancellation email. A deliberate new version requires fresh human approvals. Skip CANCELLED/HOLD rows and cancelled VID-001 forever.

## Checkpoints and state
O stores JSON: phase/claim timestamp; current script/review fingerprints; human-approved fingerprints; processed feedback/version; current video ID; and previous attempts with job/post IDs. Fingerprint = SHA256 of sorted-key UTF-8 JSON with exact current values (script text, topic/source, resolved avatar, U/V; add video ID/J/duration for video review). Persist/read back claims before external actions. Claims and IDs prevent a repeated worker from duplicating a write. If an operation has uncertain outcome, BLOCKED with evidence until reconciled; no blind timeout retry. Keep previous attempts even after revision. Do not treat legacy plan APPROVE values as new video approvals: only a newly offered VIDEO REVIEW with its recorded binding can be approved.

READY -> WRITING -> SCRIPT REVIEW -> RENDERING -> VIDEO REVIEW -> DISTRIBUTION REVIEW -> HANDOFF SENT. REVISE returns to SCRIPT REVIEW with fresh human approval. BLOCKED records exact recoverable failures; no automatic render retry loop. Skip all CANCELLED/HOLD rows and specifically cancelled VID-001 forever, retaining its history.

No other topic workbook or research worker is required. The caption skill and shared MP4 folder are required for handoff. Do not create duplicate workers. Scheduler prompts select one role above; they must not combine drafting with generation or completion checks with publishing. Report only verified changes and actionable new blockers. Repository edits or automated checks do not prove a video rendered or published.
