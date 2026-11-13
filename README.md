# HeyGen → YouTube Shorts — Cloud skill

This folder contains a self-contained operational reference for the user's **AI software news → approved script → HeyGen Video Agent → quality check → Buffer → YouTube** workflow.

**Start here:** [SKILL.md](SKILL.md).

## Open working assets

| Asset | Link |
| --- | --- |
| Live automation tracker | [HeyGen → YouTube Shorts Sheet](https://docs.google.com/spreadsheets/d/1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8/edit) |
| Approved script example (same Doc is revised in place) | [VID-001 MiniMax Script](https://docs.google.com/document/d/1rcD_N0vOmVrCb0c7zzn6_xx_sojnz8aUcxhfAkfAMTc/edit) |
| Exact production style reference | [IBM & Microsoft HeyGen master prompt](https://docs.google.com/document/d/1aXsLa5MABozi7aBf4vbSmnplPdPyd6mNyRcb-JCkd0w/edit) |
| HeyGen Video Agent | https://app.heygen.com/video-agent |
| Buffer YouTube channel | https://publish.buffer.com/channels/6af6b7bf62b70b94b016cbe8/schedule |

## What is automated vs. what still needs Work browser

| Phase | Normal route | Required gate |
| --- | --- | --- |
| AI topics | Existing 9AM trend research task | Credible original source |
| Script | Google Docs + Sheet connector | Script review E=APPROVE |
| HeyGen plan | Work browser Plan/Chat mode | Plan review I=APPROVE, first 10 tests |
| Render | HeyGen Video Agent | Explicit approval/override; no silent auto-render |
| Video status / metadata | HeyGen connector | Check exact lines, voice ID, duration ≤30s |
| Stable MP4 and upload | Work browser: HeyGen download → Buffer upload; or stable direct public media URL | Expiring signed HeyGen URL invalid for Buffer connector |
| Scheduling | Buffer automatic addToQueue | Save Buffer Post ID M and status L |
| Publication verification | Buffer list/get posts | Actual YouTube link in K only after sent |

The **current connector cannot upload raw MP4 bytes to Buffer** and the HeyGen response link is an expiring signed URL. This is not silently solved by a scheduler; run the upload in ChatGPT Work browser, or provide a tested permanent public direct MP4 endpoint.

## Important decisions

- **Fixed future voice:** `Anshul -- 17` / `d35557f1a8e24de1a34345cf58a30e51`. The private Anshul group's default has been set to this ID. Check rendered scene IDs.
- **One-time exception:** user approved the wrong voice in video VID-001 and explicitly allowed it to be scheduled. This does *not* change the global voice rule.
- **Maximum video length:** 30 seconds hard ceiling; target 27–29. The completed VID-001 is **23.1967 sec**.
- **Persistent title:** one-line, top safe area, all frames/transitions.
- **One Google Doc per Short:** always edit in place on `REVISE`, never create multiple versions.
- **No extra paid orchestration tools:** ChatGPT, HeyGen, connected Google apps, Buffer and GitHub.
- **No duplicate submissions:** stable per-row IDs, inspect existing HeyGen session and Buffer posts first.

## Start a fresh ChatGPT Work session

> Read this skill file and the relevant references. Inspect the live Google Sheet. Work only on the next eligible video row; do not re-create an already-rendered or already-scheduled video. For script revisions update the same Google Doc. Maintain ≤30 seconds, persistent title, exact narration, selected avatar and fixed voice. During first ten tests use a paused HeyGen Plan/Chat approval before render unless the user explicitly overrides for that row. After completed video, update Sheet J immediately; use Work browser to upload the downloaded MP4 into Buffer where the connector lacks stable public media, and record scheduled/published IDs and URLs. Report verified results, not assumptions.

## Repository

Private canonical repository: https://github.com/Anurag99singh/heygen-youtube-shorts-automation

The complete production workflow lives at this repository root. The separate Daily AI Trend Briefing stays in https://github.com/Anurag99singh/consistent-explainer-videos-v3/blob/main/skills/ai-trend-briefing/SKILL.md . Existing v3 workflows remain unchanged.
