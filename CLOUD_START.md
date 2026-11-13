# Current production policy — 13 November 2026
The user explicitly removed ALL manual script, plan, first-ten-test and final-publication approval gates. Run unattended: daily production starts at **10:00 IST**; daily trend research stays at 09:00 IST. Pick topic, write script, generate through HeyGen Video Agent, monitor, validate and schedule through Buffer plugin for **next day 09:00 IST** without asking for routine approval.
YouTube description means text BELOW the posted video: store it in V (YouTube Description), title in U. Never append description, hashtags, source footer or a separate caption section to the spoken script/HeyGen Doc. Pass V only to Buffer text. On-video subtitle settings remain unchanged.
Retain strict 30–35s measured duration, fixed voice d35557f1a8e24de1a34345cf58a30e51, selected/default avatar resolved by exact look ID, factual/visual QA and duplicate prevention. E/I/P are legacy review fields, not eligibility gates; do not write APPROVE pretending a human reviewed. Respect an explicit future user HOLD/REVISE/stop.
VID-001 was manually removed from Buffer by the user. Keep its recorded IDs as history, mark it intentionally cancelled in notes, exclude it from production/reconciliation retries and do not recreate it. It must not block new daily videos.

# Resume the daily HeyGen workflow

Read [SKILL.md](SKILL.md), [daily timing](references/daily-timing.md), [captions](references/youtube-caption.md), [sheet schema](references/sheet-schema.md), [HeyGen controls](references/heygen-controls.md) and [Buffer publishing](references/buffer-publishing.md).

Live queue: https://docs.google.com/spreadsheets/d/1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8/edit
Repository: https://github.com/Anurag99singh/heygen-youtube-shorts-automation

Start topic/script/caption preparation daily at 09:00 IST. Create one row per production date W; set X to next day 09:00 IST once. Draft title U and caption V separately from the bare script Doc D. New video runtime must be measured within 30.0–35.0 seconds inclusive (aim 32–34), fixed voice d35557f1a8e24de1a34345cf58a30e51, four scenes, full-time title and selected avatar.


Legacy VID-001 recorded post 6af6de6cfe8cb9dc190a4a45 now returns 404 and list_posts is empty. Keep M and BLOCKED; do not duplicate or regenerate. Its prior 23.1967-second pilot is historical, not the new target.

Existing daily research remains in v3; production-prep and hourly tasks use this dedicated repository. Hourly polling is not an instant completion webhook. Missing approvals, missed slots, API errors and environment limits must be reported honestly.
