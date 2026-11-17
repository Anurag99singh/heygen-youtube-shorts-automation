# Generation, monitoring and publishing

Use config/workflow.json for immutable account/channel/voice IDs. Read the live Sheet and Settings for exact row values and avatar mapping. Daily production is 10:00 Asia/Kolkata; existing research is 09:00. Production date W gets target X=next day 09:00, assigned once. Keep existing schedules and enable states unless explicitly asked to change them.

## HeyGen
Resolve G through Avatar Library to an exact look ID. If G is blank, resolve the configured exact default from live Settings; never guess by name. Verify avatar group default is Anshul -- 17 / d35557f1a8e24de1a34345cf58a30e51. Submit only the script Doc body with selected avatarId using Video Agent. There is no manual Plan pause gate. If exact wording/voice cannot be achieved, record the capability blocker; don't silently change renderer.

Immediately persist H=session URL, N=session ID, Y=actual start, L=RENDERING, actual video ID in a note on J until permanent URL exists. If a write or generation outcome is uncertain, reconcile the same job before retrying. Never call stop as a plan pause.

For pending renders, query the same session until video_id exists, then that video's status. Foreground polling: at least 30 seconds apart, up to 20 minutes. Ten-plus minutes is normal. Persist before exiting; hourly continuation resumes the same job. No webhook/instant-completion guarantee. Never regenerate to poll.

On completion save J=permanent HeyGen video page, Z=measured seconds, L=VIDEO READY. Validate actual 30.0–35.0s inclusive (no rounding), 9:16, exact narration in every scene, all voice IDs equal required voice, presenter avatar IDs match, topic title from first to last frame/transitions, no generated subtitles/watermarks, realistic distinct relevant B-roll. Narration estimates and defaults are not evidence of actual output. Record concrete QA in T; missing proof/failure -> BLOCKED, preserve output, no automatic paid re-render loop.

## Buffer plugin only
Destination organization/channel/category and mode are in config. Read M and list_posts before creating. Existing M means get_post/reconcile, not a new post. VID-001 is intentionally cancelled: preserve historical IDs and skip retries/recreation.

Fetch fresh direct MP4 from existing HeyGen get_video. A video page or private Drive preview is not media. Signed sources are temporary: parse real expiry; it must cover immutable X plus 24h. Refresh if needed, otherwise BLOCKED. Never commit signed URLs or save them as durable Sheet Q media. The old pilot proved scheduling acceptance, not guaranteed publication.

Require nonempty U title and V description. Use channelId from config; schedulingType=automatic, mode=customScheduled, dueAt=UTC equivalent of X, assets=[{video:{url:freshVideoUrl}}], text=V, metadata.youtube.title=U, categoryId=28, privacy=public, madeForKids=false, appropriate isAiGenerated. Do not use Buffer browser login or Add to Queue (cannot guarantee X).

Check target-slot collision before scheduling. If X passed, BLOCKED with missed-slot explanation; ask for next date, no silent rollover/immediate posting. Unknown create outcome: list/get posts first; do not blindly retry.

Immediately save actual M post ID and L=SCHEDULED only after confirmed scheduled. get_post must confirm correct channel, media, title/text, automatic mode, status/no error and dueAt=X. Recheck actual dueAt+24h against media expiry. On error retain M as duplicate guard and set BLOCKED/T with actual reason. Later hourly checks reconcile sent/error. Only actual sent status and external YouTube URL permit K, S and PUBLISHED. Never invent a publication URL from a scheduled post.
