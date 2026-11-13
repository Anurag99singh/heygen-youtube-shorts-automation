# Buffer → YouTube through the plugin

## Destination and user preference
- Use the **connected Buffer plugin only** for scheduling. Do not use a Buffer browser session or request a Buffer browser login.
- Organization: `6ae9a6a24fd7379ad1914b12`.
- YouTube channel: `6af6b7bf62b70b94b016cbe8`, Anurag Singh.
- Time zone: Asia/Kolkata.
- Automatic publishing; Add to Queue; Science & Technology (28); public; not made for kids; mark AI-generated appropriately.

## Verified media route
On 13 November 2026, Buffer `create_post` accepted the fresh direct signed MP4 returned by HeyGen `get_video`. `get_post` subsequently confirmed a video/mp4 asset, duration 23.208s, YouTube Short metadata, scheduled status and no error. The earlier blanket claim that signed HeyGen URLs cannot be sent to Buffer was incorrect.

A signed MP4 is **temporary**, not permanent hosting. The pilot source expired about seven days later, well after its scheduled slot. This proves scheduling acceptance; it does not prove successful publication or guarantee every future URL/queue combination.

## Runbook
1. Read the live row and Sheet M; check Buffer posts for duplicate video/title. If M exists, reconcile that post instead of creating another.
2. Confirm the required approvals and video QA. VID-001 has a video-specific older-voice exception.
3. Call HeyGen `get_video` for the existing video. Use its actual direct `videoUrl`, never the HeyGen viewing page or private Drive preview. Do not generate a new video.
4. For a signed URL, parse the expiry and inspect current Buffer channel schedule/queue. Require the expected slot plus at least 24 hours to precede expiry. If validity is too short, obtain a refreshed URL; if it still cannot cover the slot, report the media-validity blocker rather than silently changing publishing mode or creating duplicate posts.
5. Call Buffer:
   - `channelId: "6af6b7bf62b70b94b016cbe8"`
   - `schedulingType: "automatic"`
   - `mode: "addToQueue"`
   - `assets: [{video: {url: freshVideoUrl}}]`
   - approved caption/source and YouTube title/category metadata.
6. Immediately record actual returned post ID in M and scheduled state in L. Verify through `get_post`: correct channel, actual dueAt, Automatic/Add to Queue, video asset, YouTube settings, status and error.
7. Compare **actual returned dueAt** plus 24 hours against source expiry again. If outside validity, treat as an unresolved media-validity issue on that same post; do not create a second post or claim readiness.
8. Do not store the signed URL in GitHub or Sheet Q as durable media. Keep permanent HeyGen page in J. Record post ID, slot and expiry observations in T without the signed URL.
9. Reconcile with `get_post`. Only after sent, use actual returned YouTube external link in K, timestamp in S, and L=PUBLISHED. On error, record the returned reason; do not resubmit blindly.

## VID-001 — verified scheduled record
- HeyGen video: `321845ae839b45adb611145293a24e8b`; duration 23.1967s.
- Buffer Idea caption source: `6af6d4257438174bb4e4ad74`. The Idea alone is not a scheduled post.
- **Actual Buffer post:** `6af6de6cfe8cb9dc190a4a45`.
- **Due:** 13 November 2026, **17:36 IST** (`2026-11-13T12:06:00Z`).
- Retrieved status: `scheduled`; no error; video/mp4 asset present; Automatic / Add to Queue.
- Publication not yet confirmed. Never regenerate or duplicate this post.
