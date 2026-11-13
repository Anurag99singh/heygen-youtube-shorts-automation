# Current production policy — 13 November 2026
The user explicitly removed ALL manual script, plan, first-ten-test and final-publication approval gates. Run unattended: daily production starts at **10:00 IST**; daily trend research stays at 09:00 IST. Pick topic, write script, generate through HeyGen Video Agent, monitor, validate and schedule through Buffer plugin for **next day 09:00 IST** without asking for routine approval.
YouTube description means text BELOW the posted video: store it in V (YouTube Description), title in U. Never append description, hashtags, source footer or a separate caption section to the spoken script/HeyGen Doc. Pass V only to Buffer text. On-video subtitle settings remain unchanged.
Retain strict 30–35s measured duration, fixed voice d35557f1a8e24de1a34345cf58a30e51, selected/default avatar resolved by exact look ID, factual/visual QA and duplicate prevention. E/I/P are legacy review fields, not eligibility gates; do not write APPROVE pretending a human reviewed. Respect an explicit future user HOLD/REVISE/stop.
VID-001 was manually removed from Buffer by the user. Keep its recorded IDs as history, mark it intentionally cancelled in notes, exclude it from production/reconciliation retries and do not recreate it. It must not block new daily videos.

## Historical record (superseded where inconsistent)
> Historical pilot record. Current policy is 30–35 seconds for NEW videos, production starts 09:00 IST and exact next-day 09:00 publication. Latest 13 November live check: recorded VID-001 Buffer ID returns 404; list_posts empty. Current state is BLOCKED, M retained, no duplicate. Historical scheduling success below does not establish current queue state.

# VID-001 — pilot findings and recovery

Date: 2026-11-13, Asia/Kolkata.

## Source record
- Topic: MiniMax H3-Image — Fast 4K AI Images.
- Original source: https://www.minimax.io/blog/minimax-h3-image.
- Google Doc (one stable URL): https://docs.google.com/document/d/1rcD_N0vOmVrCb0c7zzn6_xx_sojnz8aUcxhfAkfAMTc/edit.
- Selected avatar: `AV07 · Anshul Jain`, look `692b3398e8634695b23891002c516a47`.
- Required voice for NEXT videos: **Anshul -- 17**, `d35557f1a8e24de1a34345cf58a30e51`.
- Buffer YouTube channel: `6af6b7bf62b70b94b016cbe8`.

## What happened
1. Initial Video Agent call contained a long preamble telling HeyGen to plan only. HeyGen started generating anyway. The assistant used `stop_video_agent_session`, which led to `waiting_for_input` but **no blueprint**. Session `ca0983d620874db7b5cb0114f6b99509`. **Lesson:** stop is not a safe plan pause.
2. User explicitly overrode plan review for this test and asked to send the approved script alone, render and schedule.
3. Active session `6a996f7aa76d448d8b971bdb51057006`; video ID `321845ae839b45adb611145293a24e8b`; permanent HeyGen page https://app.heygen.com/videos/321845ae839b45adb611145293a24e8b.
4. HeyGen reported completed. `get_video` verified **23.1967 sec**, 9:16. `get_video_scenes` showed four **exact** approved narration lines and correct presenter avatar look IDs.
5. `get_video_scenes` found wrong voice `7b9850bf42ed4d999891709c3f7341a9` **Anshul 2026** in all scenes. User explicitly **accepted this result for VID-001 only**. Do not use that voice in future videos.
6. Updated the avatar GROUP's default voice to `d35557f1a8e24de1a34345cf58a30e51` and confirmed with `get_avatar_group` read-back.
7. Sheet J was populated with permanent HeyGen video page, not the signed MP4. The video page is **not** a direct public media file. `get_video` returned `...mp4?Expires=...&Signature=...`, which is temporary. Later plugin testing accepted this route with sufficient remaining validity; see the verified scheduling update below.
8. An hourly completion monitor was created, but it did **not** fire instantly. It was paused when wrong voice was detected. That has no bearing on this video's one-time publication exception. The later Buffer plugin scheduling verification supersedes this earlier pending handoff.
9. HeyGen reported continuous title but there was not independent frame-by-frame verification. Be honest about this.

## Next actions
- For VID-001, user accepted voice exception and authorized **Buffer scheduling**. Do not rerender. Use the Buffer plugin with a fresh direct MP4 and expiry check. Verify actual post ID and write M/L. When published, write K/S.
- For VID-002+, keep fixed Anshul -- 17 in all scenes, confirm after render, and insist on ≤30 secs.
- For more accurate progress updates, write J immediately when status changes during a task run; polling is still at most hourly without a real callback integration.

## Actual pilot status (update live Sheet for authoritative current)
Generated ✓; 23.2 seconds ✓; exact four narration strings ✓; selected avatar ✓; **voice exception accepted for VID-001**; video linked J ✓; Buffer scheduled **verified via plugin**; publication not yet confirmed.

## Additional progress — 2026-11-13
- User explicitly authorized publishing VID-001 despite its older voice.
- Buffer **Idea** created and verified: `6af6d4257438174bb4e4ad74`; text/title/source prepared, but no video media attached. This is **not** a scheduled post.
- Existing Google Sheet J contains the permanent HeyGen page and L is **SCHEDULED**. M contains verified Buffer post ID.
- Active daily script task: `6af6d39cf50c8191a087adb5bd1376d4` (approx 10AM IST); active hourly HeyGen Buffer worker: `6af6c74482fc8191bd1608e67cdea0ee`. Buffer plugin scheduling verified; no Buffer browser session required.
- Github create-repository operation is unavailable through connected tool. This skill was saved under existing private repo `consistent-explainer-videos-v3`; dedicated private repository has now been created and the old HeyGen folder removed from v3.

## Verified plugin handoff — 13 November 2026
Buffer post `6af6de6cfe8cb9dc190a4a45` was created and retrieved through the plugin, status scheduled, due `2026-11-13T12:06:00Z` (17:36 IST). Automatic / Add to Queue, video asset and YouTube Short metadata confirmed; no error. Fresh signed source had about seven days of validity. This corrects the earlier assumption that a Buffer browser upload was mandatory. Publication remains to be reconciled.
