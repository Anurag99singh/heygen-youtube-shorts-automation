# Current production policy — 13 November 2026
The user explicitly removed ALL manual script, plan, first-ten-test and final-publication approval gates. Run unattended: daily production starts at **10:00 IST**; daily trend research stays at 09:00 IST. Pick topic, write script, generate through HeyGen Video Agent, monitor, validate and schedule through Buffer plugin for **next day 09:00 IST** without asking for routine approval.
YouTube description means text BELOW the posted video: store it in V (YouTube Description), title in U. Never append description, hashtags, source footer or a separate caption section to the spoken script/HeyGen Doc. Pass V only to Buffer text. On-video subtitle settings remain unchanged.
Retain strict 30–35s measured duration, fixed voice d35557f1a8e24de1a34345cf58a30e51, selected/default avatar resolved by exact look ID, factual/visual QA and duplicate prevention. E/I/P are legacy review fields, not eligibility gates; do not write APPROVE pretending a human reviewed. Respect an explicit future user HOLD/REVISE/stop.
VID-001 was manually removed from Buffer by the user. Keep its recorded IDs as history, mark it intentionally cancelled in notes, exclude it from production/reconciliation retries and do not recreate it. It must not block new daily videos.

## Historical record (superseded where inconsistent)
# Dedicated repository setup — completed

Canonical private repository: https://github.com/Anurag99singh/heygen-youtube-shorts-automation

On 13 November 2026:
- Created the dedicated private repository with main as default branch.
- Migrated the complete production folder to the root and retained the .agents discovery entry.
- Verified all 12 files and updated the live Sheet skill reference and two production task prompts.
- Removed the migrated HeyGen Shorts folder and discovery entry from consistent-explainer-videos-v3. All seven remaining files retained their original blob hashes.
- Kept the independent AI Trend Briefing and original explainer package in v3.
- Scheduled approved VID-001 with the Buffer plugin, post `6af6de6cfe8cb9dc190a4a45`, due 13 November 2026 at 17:36 IST.

Use [SKILL.md](SKILL.md) and [Buffer publishing](references/buffer-publishing.md) for current operation. Never request Buffer browser sign-in for scheduling. Preserve all workflow IDs, approvals and the future fixed voice. Do not commit credentials or signed media URLs. Read live Google Sheet and service records before relying on this dated setup record.

## Current policy update
New videos: 30–35 seconds inclusive, production prep 09:00 IST, target next-day 09:00, Buffer automatic/customScheduled. Dedicated title/caption and timing/monitoring references added. VID-001's historical schedule is currently unverified (recorded post returns 404); keep duplicate guard and investigate, never auto-recreate.
