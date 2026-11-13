# Buffer → YouTube: robust publishing handoff

## Connected service
- Buffer account: `anuragsinghisgood@gmail.com`, organization `6ae9a6a24fd7379ad1914b12`.
- YouTube channel ID: `6af6b7bf62b70b94b016cbe8`.
- Channel: [Anurag Singh](https://www.youtube.com/channel/UCMRdswVU_FY3vugUBGfG0bw).
- Buffer schedule: https://publish.buffer.com/channels/6af6b7bf62b70b94b016cbe8/schedule
- Time zone: Asia/Kolkata.
- User explicitly prefers **Buffer automatic scheduling**, not ChatGPT Work using YouTube Studio to publish.

## Stable media problem
HeyGen's `get_video` returns a permanent **video page** (`https://app.heygen.com/videos/VIDEO_ID`) plus a **signed temporary MP4 URL** with `Expires=` and `Signature=`. The signed URL expires, and Buffer connector's `create_post` requires **direct public HTTP(S) video media URL that does not expire**. The permanent HeyGen page is not a direct MP4 and cannot be used as `assets[].video.url`.

**Never submit either of these invalid forms to Buffer connector:**
- temporary signed HeyGen `...mp4?Expires=...`
- private Drive document or file preview URL, or a HeyGen video page.

### Supported option A — ChatGPT Work browser (no additional paid tools)
1. Open finished HeyGen video page from Sheet J; download MP4 to **Work's cloud computer**.
2. Open connected Buffer YouTube channel's Schedule UI.
3. Create YouTube Short post; upload local downloaded MP4 **through Buffer UI**. Don't paste expiring video URL.
4. Add title and short accurate description with original source. Use **automatic** publishing (not reminder), add to queue or use approved custom slot, category **Science & Technology (28)**, mark AI-generated if appropriate.
5. Confirm the actual scheduled queue item. Record Buffer Post ID if shown or retrieve via connected Buffer `list_posts`; update Sheet M and L= SCHEDULED. Update K/S only after actual publication.
6. If Work browser cannot interact with Buffer, stop and report this as a manual browser upload blocker. **Do not fake scheduling.**

### Supported option B — Connector with stable public MP4
If a user-approved stable publicly downloadable MP4 exists (NOT a signed temporary link), call:
```text
Buffer.create_post({
  channelId: "6af6b7bf62b70b94b016cbe8",
  schedulingType: "automatic",
  mode: "addToQueue",
  text: "MiniMax says its new H3-Image model creates and edits images using multiple references. Source: https://www.minimax.io/blog/minimax-h3-image #AI #Shorts",
  assets: [{ video: { url: "<STABLE_PUBLIC_DIRECT_MP4>" } }],
  metadata: {
    youtube: {
      title: "MiniMax H3-Image: Fast 4K AI Images #Shorts",
      categoryId: "28",
      privacy: "public",
      madeForKids: false,
      isAiGenerated: true
    }
  }
})
```
This is **pseudocode**, not an HTTP-ready script and not permission to invent the URL.

## Safety/idempotency
- Check Sheet M is blank and Buffer `list_posts` for existing matching video before creating. If already scheduled, don't create another.
- Only proceed if the user has authorized publication and all required QA passes (or they explicitly accept a *video-specific* exception).
- On Buffer success, write M Buffer Post ID and L=SCHEDULED immediately, plus actual scheduled dueAt in T or a relevant notes field.
- Reconcile Buffer sent status later; populate K with actual YouTube link, S published timestamp and L=PUBLISHED.
- On failure, keep J video page intact, update T and L=BLOCKED. A completed video is not evidence of a scheduled post.
- Verify account/channel active before attempting.

## VID-001
- Video page: https://app.heygen.com/videos/321845ae839b45adb611145293a24e8b
- Duration 23.1967s; user's explicit exception accepts its older voice just for this test.
- **2026-11-13 handoff blocker:** only signed expiring MP4 URL is available through HeyGen connector, and Chat-mode Browser integration can read but cannot click/upload. Use Work browser as the direct local-upload route. `SCHEDULED` cannot be recorded until Buffer actually returns a post record.

## Buffer Idea for VID-001 (prepared, not scheduled)
The connected Buffer organization now contains verified Idea ID `6af6d4257438174bb4e4ad74`, titled `VID-001 · MiniMax H3-Image: Fast 4K AI Images #Shorts`. It contains the approved caption, source and permanent HeyGen page URL. **It does not contain MP4 media and is not a post.** In Work/Buffer browser, use the idea as the caption source and attach the finished downloaded MP4; then schedule via automatic queue and obtain actual Buffer Post ID.
