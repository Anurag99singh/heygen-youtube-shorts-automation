# Current production policy — 13 November 2026
The user explicitly removed ALL manual script, plan, first-ten-test and final-publication approval gates. Run unattended: daily production starts at **10:00 IST**; daily trend research stays at 09:00 IST. Pick topic, write script, generate through HeyGen Video Agent, monitor, validate and schedule through Buffer plugin for **next day 09:00 IST** without asking for routine approval.
YouTube description means text BELOW the posted video: store it in V (YouTube Description), title in U. Never append description, hashtags, source footer or a separate caption section to the spoken script/HeyGen Doc. Pass V only to Buffer text. On-video subtitle settings remain unchanged.
Retain strict 30–35s measured duration, fixed voice d35557f1a8e24de1a34345cf58a30e51, selected/default avatar resolved by exact look ID, factual/visual QA and duplicate prevention. E/I/P are legacy review fields, not eligibility gates; do not write APPROVE pretending a human reviewed. Respect an explicit future user HOLD/REVISE/stop.
VID-001 was manually removed from Buffer by the user. Keep its recorded IDs as history, mark it intentionally cancelled in notes, exclude it from production/reconciliation retries and do not recreate it. It must not block new daily videos.

# HeyGen → YouTube Shorts Automation

[Start with SKILL.md](SKILL.md). Private canonical repository for the AI-software video workflow.

## Daily flow
| When | Work |
| --- | --- |
| 09:00 IST, day D | Pick one verified useful AI-software topic; write the script, YouTube title and caption |
| After rendering (10+ minutes possible) | Persist finished video; check measured duration and all quality gates |
| As soon as ready and approved | Buffer plugin schedules exact **09:00 IST on D+1** |
| Hourly | Resume existing render IDs and reconcile scheduled/sent/error states |

New videos must be **30–35 seconds inclusive**, target 32–34. Captions here mean the YouTube posting description; generated on-video subtitles remain disabled. Use four scenes, portrait 9:16, persistent title and fixed **Anshul -- 17** voice `d35557f1a8e24de1a34345cf58a30e51`.

## Your review
3. During the pilot, review final video and authorize publication; record authorization in T. Automations never infer approval from silence.

Revisions edit the same Doc. A published/scheduled old row does not block the next production date. Missed 09:00 slots require a new date decision, never immediate publishing or silent rollover.

## Completion monitoring
Render start/session/video IDs are saved before exit. The hourly task checks those same jobs until completion, then validates and schedules authorized output. This is hourly polling, not instant notification or a configured completion webhook. HeyGen plan approval can require attended Work browser; **Buffer scheduling uses the plugin only**.

## Working assets
- [Live queue](https://docs.google.com/spreadsheets/d/1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8/edit)
- [Style master](https://docs.google.com/document/d/1aXsLa5MABozi7aBf4vbSmnplPdPyd6mNyRcb-JCkd0w/edit)
- [Daily timing and monitoring](references/daily-timing.md)
- [YouTube title/caption standard](references/youtube-caption.md)
- [Schedulers](references/schedulers.md)
- [Buffer handoff](references/buffer-publishing.md)
- [Sheet fields](references/sheet-schema.md)
- [Separate AI Trend Briefing](https://github.com/Anurag99singh/consistent-explainer-videos-v3/blob/main/skills/ai-trend-briefing/SKILL.md)

## Pilot status — latest check 13 November 2026
VID-001 was approved under the old 23.2-second pilot policy and its older voice was accepted only for that video. Buffer previously returned scheduled post `6af6de6cfe8cb9dc190a4a45`, but the latest get_post returns **404 Post not found** and list_posts is empty. Current scheduling/publication is unverified. Retain M as duplicate guard and resolve the missing-post issue before replacing it. Do not regenerate or silently reschedule this pilot.
