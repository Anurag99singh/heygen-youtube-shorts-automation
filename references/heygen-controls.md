# HeyGen: voice, plans, rendering and QA

## Identity and voice (strict)
- HeyGen connected workspace: Anshul / account `anshulprojectmgmt@gmail.com`.
- Private Anshul avatar **group ID** `34dc0457ca4d4eeb92dae5a9e5180bd8`.
- **REQUIRED every time:** voice **Anshul -- 17**, ID `d35557f1a8e24de1a34345cf58a30e51`, English, ACTIVE.
- Former wrong voice **Anshul 2026**: `7b9850bf42ed4d999891709c3f7341a9`.
- Group default voice was changed via `update_avatar_group` and **read-back verified** to `d35557f1a8e24de1a34345cf58a30e51` on 2026-11-13. Still **do not assume** Video Agent obeys the default: VID-001 initially used wrong default despite prompt-level voice request.
- When a video is ready, `get_video_scenes` and inspect **every scene[].script[].voice_id**, plus `avatar_id` for presenter scenes. Mismatch is a hard failure unless user expressly accepts an exception for that specific video.
- Avatar look choice comes from Video Queue G and Avatar Library B; never match by ambiguous avatar display name.

## Plan approval: first 10 supervised tests
1. Script Doc approved E=APPROVE.
2. In **ChatGPT Work browser**, open HeyGen Video Agent, start a **new Plan / Chat mode** session. Select avatar/voice and 9:16 in the UI.
3. Paste **only** the approved script Doc body. No artificial instructions before or after. Follow the user's exact scenes, title and narration.
4. If HeyGen begins a short auto-render countdown, pause it via the **visible HeyGen interface**, then confirm it actually paused. No periodic automation can beat a seconds-long timer reliably.
5. Show actual video blueprint to user. Save live session H, mark PLAN REVIEW, obtain I=APPROVE; on I=REVISE, revise within **same session**.
6. The `video_agent_generate` connector **is a generation action**, not a safe plan-only action. It has no Plan/Chat selector; **do not use before plan approval** unless user clearly authorizes a one-time direct render. `stop_video_agent_session` is **not** a countdown pause; it halts the whole agent and can prevent any plan being returned.

## Direct render: only when authorized
- User may override mandatory plan review **for one specified video**. If yes, call `video_agent_generate` with **prompt equal to exactly the Google Doc body**, `avatarId` equal to the selected look ID; do not add `conversationContext` boilerplate or another wrapper.
- The tool does not expose a reliable `voiceId` input. Verify group default before rendering and **actual scene voice IDs after**. A request in Doc for consistent voice alone is insufficient to force voice choice.
- Save `sessionId` and returned `video_id`. Never duplicate the generation to poll.
- Poll `get_video_agent_session` / `get_video` at reasonable intervals. If pending, record pending; **do not claim a final video exists**.
- On completion, write **permanent HeyGen viewing page** into Video Queue J immediately, even if Buffer cannot upload yet.

## QA checklist
- [ ] Actual duration is **≤30.0 sec** and 9:16.
- [ ] Four scene scripts match approved narration **exactly**, not paraphrased; no added spoken lines.
- [ ] Every scene voice ID equals `d35557f1a8e24de1a34345cf58a30e51`, unless a documented single-video exception.
- [ ] Presenter scene avatar ID equals the selected look ID.
- [ ] No captions/subtitles, no watermark (visual check if needed).
- [ ] Topic title persists throughout video including transitions, not just scene 1 (frame-level review required where metadata does not expose title visibility).
- [ ] B-roll supports narration (avoid fake UI presented as real and generic robots).
- [ ] Final direct media link is stable and valid for Buffer, or use Work browser to upload the actual MP4.

## Prior failure
- VID-001 exact scene narration and avatar were correct and duration **23.1967s**, but all scene voice IDs were the old group default. The user **explicitly accepted that video's voice only**. See [test-1-incident.md](test-1-incident.md).
