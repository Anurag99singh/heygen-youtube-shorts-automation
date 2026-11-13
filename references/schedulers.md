# Scheduled workers and Cloud setup

## Existing schedule (DO NOT duplicate)
**Daily AI Trend Briefing** is already an enabled 09:00 Asia/Kolkata automation. It gathers 10 recent AI-software-first topics and recommends top three. Existing skill: https://github.com/Anurag99singh/consistent-explainer-videos-v3/blob/main/skills/ai-trend-briefing/SKILL.md (separate v3 repository). Reuse the source/trend Sheet; don't rebuild it or create another 9AM research task.

## Recommended workers for the production pipeline
These are **proposed configuration instructions**. A worker is NOT active merely because it is documented here. Inspect actual `Automations.peek` results before claiming anything has been scheduled. No task should spend HeyGen credits or publish without the required approvals.

| Worker | Suggested cadence | Work |
| --- | --- | --- |
| **A — Daily Script Prep** | Daily at 09:30 IST after trends | Read top eligible AI software trend, choose one fresh topic, check source, write/revise existing Script Doc, set E=PENDING/L=SCRIPT REVIEW; notify user for approval. Do not hand off to HeyGen while pending. |
| **B — Queue & HeyGen Review** | Hourly condition watch (maximum supported frequency) | Check Script Review E and Plan Review I. When approved, validate look + fixed voice and use **Work browser Plan mode**. Never submit generation through connector before plan approval. If plan cannot be safely paused, notify user; never claim plan ready. |
| **C — Video → Buffer Handoff** | Hourly condition watch | For rows with active HeyGen sessions, check exact existing session; on completion update J immediately, run QA, and if approved use Work browser to download MP4 and upload via Buffer UI (or connector with permanent direct MP4). No duplicate post; record M/L and notify. |
| **D — Buffer Reconciliation** | Hourly condition watch or combine with C | Check scheduled posts for actual sent/error; write K (YouTube URL), S (published time), L=PUBLISHED only after confirmed sent. |

### Practical consolidation
To minimize cost/complexity, use **one 09:30 script task** and **one hourly state-machine task combining B+C+D**. Since ChatGPT Automations schedules cannot check every second and Work computer availability depends on attached environment, first verify that a Work task actually has access to HeyGen/Buffer browser when it fires. Keep initial 10 video plans attended.

### Daily Script Prep worker prompt
```text
Read SKILL.md and references/script-template.md plus sheet-schema.md from Anurag99singh/heygen-youtube-shorts-automation. Read existing AI Trend Briefing output; choose a recent AI-software story only if an eligible, unscripted topic exists. Use live automation Sheet 1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8. Prepare one <=30 second, four-scene, full-title HeyGen script in a new Doc only for a new row, or update the existing Doc in column D in place on a revision. Mark E=PENDING and L=SCRIPT REVIEW. Never call HeyGen rendering or Buffer publishing. Send me the link for approval, or skip with no update if already waiting.
```

### Hourly State-Machine worker prompt
```text
Read SKILL.md and references/sheet-schema.md, heygen-controls.md and buffer-publishing.md from Anurag99singh/heygen-youtube-shorts-automation. Scan the live Google Sheet for the oldest eligible unblocked item. Honor every human approval. Reconcile existing HeyGen sessions and completed videos without re-generating; immediately set Video Queue J to the permanent HeyGen video page on completion, and run exact scene narration/voice/duration QA. For first 10 tests, never silently render before the HeyGen plan is approved; operate HeyGen Plan mode through an attached Work browser or report inability to do so. When video is approved and completed, if a stable public direct MP4 is unavailable, use an attached Work browser to download the MP4 and upload it into Buffer's YouTube channel in automatic queue mode. The in-chat Buffer connector cannot upload local MP4 bytes. Before scheduling, inspect Sheet M and Buffer posts for duplicates; on success write M/L=SCHEDULED; after actual publication write K/S/L=PUBLISHED. Record blocker text honestly, never call a signed expiring MP4 stable, never publish a failed QA video without a video-specific user exception.
```

### Guardrails
- A scheduled worker's completion does NOT imply production or publishing happened. Verify connected services and cell updates.
- ChatGPT automated schedules run at most **hourly**; no reliable seconds-level HeyGen countdown interception.
- Do not allow multiple jobs on the same VID row; use IDs, status checks and explicit eligibility.
- Automatic rendering/publishing should be enabled only after an end-to-end pilot with verified audio and media upload.
- User's account may have a cap on active automations; prefer combining B+C+D into one task.
- If Cloud/Work browser sessions are logged out, stop at authentication, never claim success, and don't ask for passwords.
- A true event-driven HeyGen completion → Sheet update would require a webhook/event integration; under the no-paid-extra-tools requirement and current connectors, periodic hourly polling is the realistic option.


## Actual task activation — verified 2026-11-13
These tasks **have now been created/enabled** in ChatGPT Automations. Always recheck `Automations.peek` before relying on cached status.

| Task | Task ID | Verified state | Frequency |
| --- | --- | --- | --- |
| Existing Daily AI Trends for Shorts | `6af078ea40608191a2adc9c6e9ff0ae4` | Enabled | Daily 09:00 IST |
| Daily AI Short Script | `6af6d39cf50c8191a087adb5bd1376d4` | Enabled | Daily, approximately 10:00 IST |
| HeyGen Buffer Handoff | `6af6c74482fc8191bd1608e67cdea0ee` | Enabled | Hourly |

The two new tasks run via the current conversation's inherited environment. **Work/browser upload ability remains unverified in those environments**; do not claim automatic Buffer attachment or actual scheduling until a Buffer post ID exists. If the hourly worker cannot upload local MP4, it must leave precise blocker details and require the Work browser/file-upload route. The schedule alone cannot substitute for a stable direct media asset or cloud browser credentials.

The user approved the wrong voice **only for VID-001**. Its Buffer handoff is pending; no second HeyGen generation should be started for that video. Future videos require the corrected Anshul -- 17 voice.

## Dedicated repository handoff — 13 November 2026
The canonical HeyGen skill now lives at https://github.com/Anurag99singh/heygen-youtube-shorts-automation/blob/main/SKILL.md . The separate AI Trend Briefing remains in v3. Cloud browser access and approved MP4 download worked in the attended migration session; Buffer browser authentication was not completed, so local upload and scheduled publication remain unverified. Do not infer that the recurring tasks have an authenticated browser session from this attended check.
