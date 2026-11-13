# Current production policy — 13 November 2026
The user explicitly removed ALL manual script, plan, first-ten-test and final-publication approval gates. Run unattended: daily production starts at **10:00 IST**; daily trend research stays at 09:00 IST. Pick topic, write script, generate through HeyGen Video Agent, monitor, validate and schedule through Buffer plugin for **next day 09:00 IST** without asking for routine approval.
YouTube description means text BELOW the posted video: store it in V (YouTube Description), title in U. Never append description, hashtags, source footer or a separate caption section to the spoken script/HeyGen Doc. Pass V only to Buffer text. On-video subtitle settings remain unchanged.
Retain strict 30–35s measured duration, fixed voice d35557f1a8e24de1a34345cf58a30e51, selected/default avatar resolved by exact look ID, factual/visual QA and duplicate prevention. E/I/P are legacy review fields, not eligibility gates; do not write APPROVE pretending a human reviewed. Respect an explicit future user HOLD/REVISE/stop.
VID-001 was manually removed from Buffer by the user. Keep its recorded IDs as history, mark it intentionally cancelled in notes, exclude it from production/reconciliation retries and do not recreate it. It must not block new daily videos.

# Daily dates, render monitoring and publication

## Production day and exact publication slot
- All dates and times use Asia/Kolkata.
- Start daily topic selection/script/caption preparation at **09:00 IST**.
- For production date D, persist W=D (YYYY-MM-DD) and X=D+1 at **09:00 IST** as a timezone-explicit timestamp when the row is first created. Example: production 2026-11-14 -> target 2026-11-15T09:00:00+05:30 (=2026-11-15T03:30:00Z).
- Schedule as soon as the completed video has passed QA and required approvals, for X. Do not wait until 09:00 to submit the post.
- Buffer request: schedulingType=automatic, mode=customScheduled, dueAt=the UTC equivalent of X. **Add to Queue no longer applies to new videos** because it cannot guarantee the requested 09:00 slot.
- Do not reschedule the previously approved VID-001 pilot just because defaults changed. Preserve its recorded ID and resolve its missing-post blocker.
- If X is already in the past, set BLOCKED with a missed-slot explanation and request the next date; never publish immediately or silently roll to another day.
- Check for another post already occupying X. Do not create duplicates or silently publish two daily Shorts in that slot.

## Idempotency and research race
- One new row per India production date; rerunning the daily task edits that row in place. Distinct production dates may coexist with a previously scheduled row. A scheduled or independently blocked older row must not stop the next day's topic/caption draft.
- Deduplicate stories using source URL, event and existing topics, not just title strings.
- The research task also runs at 09:00. If today's list is not ready, do not treat yesterday's list as today's. Use the existing Sources directory and research rules to verify a fresh candidate directly; then reconcile against today's list when available. Never wait indefinitely for the other task or create another research automation.
- Keep at most one active HeyGen render at a time; a queued script may wait without blocking status checks of an existing render.

## Completion monitoring (10+ minute renders)
1. Immediately on real render start, save H/session URL, N/session ID, Y/Render Started At and L=RENDERING. Save any actual video ID in a cell note on J until the permanent view URL is available.
2. The existing hourly worker reads these persisted IDs on every run and checks the **same job**, never re-generating to poll. If session has no video ID yet, get_video_agent_session; once it exposes video_id, get_video for that ID.
3. Pending/processing after 10 minutes is normal. Record current progress; do not assume failure or completion from elapsed time.
4. If an attended run is still active, it may poll the existing job no more often than every 30 seconds, up to the tool's 20-minute foreground window. Persist state before exiting. A 20-minute pending render is not automatically failed; hand it to the hourly worker.
5. On actual completed status, immediately save J permanent video page, Z measured duration, and L=VIDEO READY. Validate inclusive **30.0 <= duration <= 35.0**, exact narration, fixed voice, avatar, title and other visual rules. Missing proof is recorded, not invented.
6. QA failure -> BLOCKED and a specific repair request, not automatic paid regeneration. Preserve the finished video and review history.
8. Every later hourly run reconciles scheduled posts. Only sent confirmation plus actual external YouTube URL permits K/S/PUBLISHED. An error or 404 keeps M as duplicate guard and records BLOCKED; do not recreate automatically.

## Limits and escalation
This is **hourly polling**, not a HeyGen completion webhook. Detection usually occurs on the next hourly run, potentially around an hour after completion plus task-delivery delay. It cannot promise instant notification or a hard execution SLA. No current connected HeyGen event trigger is configured.
If a render is still pending near X, warn once with its actual state. At the missed target time, report the missed slot; do not conceal the delay. Approval or sign-in delays can prevent the next-day slot.

## Human review
