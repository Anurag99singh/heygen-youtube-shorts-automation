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
7. Sheet J was populated with permanent HeyGen video page, not the signed MP4. The video page is **not** a direct public media file. `get_video` returned `...mp4?Expires=...&Signature=...`, which Buffer connector prohibits because it is temporary.
8. An hourly completion monitor was created, but it did **not** fire instantly. It was paused when wrong voice was detected. That has no bearing on this video's one-time publication exception. A Work-browser video download and Buffer upload still needs execution before claiming Buffer scheduled.
9. HeyGen reported continuous title but there was not independent frame-by-frame verification. Be honest about this.

## Next actions
- For VID-001, user accepted voice exception and authorized **Buffer scheduling**. Do not rerender. Upload MP4 to Buffer using Work browser if a stable direct media URL cannot be supplied. Verify Buffer actual post ID and write M/L. When published, write K/S.
- For VID-002+, keep fixed Anshul -- 17 in all scenes, confirm after render, and insist on ≤30 secs.
- For more accurate progress updates, write J immediately when status changes during a task run; polling is still at most hourly without a real callback integration.

## Actual pilot status (update live Sheet for authoritative current)
Generated ✓; 23.2 seconds ✓; exact four narration strings ✓; selected avatar ✓; **voice exception accepted for VID-001**; video linked J ✓; Buffer scheduled **not yet verified**.

## Additional progress — 2026-11-13
- User explicitly authorized publishing VID-001 despite its older voice.
- Buffer **Idea** created and verified: `6af6d4257438174bb4e4ad74`; text/title/source prepared, but no video media attached. This is **not** a scheduled post.
- Existing Google Sheet J contains the permanent HeyGen page and L is **VIDEO READY**. T explains the pending upload.
- Active daily script task: `6af6d39cf50c8191a087adb5bd1376d4` (approx 10AM IST); active hourly HeyGen Buffer worker: `6af6c74482fc8191bd1608e67cdea0ee`. Work-browser file upload still unverified.
- Github create-repository operation is unavailable through connected tool. This skill was saved under existing private repo `consistent-explainer-videos-v3`; dedicated new repo still needs to be created via browser/Work mode.
