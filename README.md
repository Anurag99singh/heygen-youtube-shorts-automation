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

## Workflow and approval gates

| Phase | Normal route | Required gate |
| --- | --- | --- |
| AI topics | Existing 9AM trend research task | Credible original source |
| Script | Google Docs + Sheet connector | Script review E=APPROVE |
| HeyGen plan | Work browser Plan/Chat mode | Plan review I=APPROVE, first 10 tests |
| Render | HeyGen Video Agent | Explicit approval/override; no silent auto-render |
| Video status / metadata | HeyGen connector | Check exact lines, voice ID, duration ≤30s |
| Video media transfer | Fresh HeyGen direct MP4 → Buffer plugin | Check expiry covers queue slot plus margin; verify saved video asset |
| Scheduling | Buffer automatic addToQueue | Save Buffer Post ID M and status L |
| Publication verification | Buffer list/get posts | Actual YouTube link in K only after sent |

Use the **Buffer plugin for all scheduling**, without a Buffer browser login. On 13 November 2026, Buffer accepted the fresh signed HeyGen MP4 and scheduled VID-001. Signed URLs remain temporary: check expiry against the actual queue time, verify the saved post and media, and reconcile publication. See [Buffer publishing](references/buffer-publishing.md).

## Important decisions

- **Fixed future voice:** `Anshul -- 17` / `d35557f1a8e24de1a34345cf58a30e51`. The private Anshul group's default has been set to this ID. Check rendered scene IDs.
- **One-time exception:** user approved the wrong voice in video VID-001 and explicitly allowed it to be scheduled. This does *not* change the global voice rule.
- **Maximum video length:** 30 seconds hard ceiling; target 27–29. The completed VID-001 is **23.1967 sec**.
- **Persistent title:** one-line, top safe area, all frames/transitions.
- **One Google Doc per Short:** always edit in place on `REVISE`, never create multiple versions.
- **No extra paid orchestration tools:** ChatGPT, HeyGen, connected Google apps, Buffer and GitHub.
- **No duplicate submissions:** stable per-row IDs, inspect existing HeyGen session and Buffer posts first.

## Start a fresh ChatGPT Work session

> Read this skill file and the relevant references. Inspect the live Google Sheet. Work only on the next eligible video row; do not re-create an already-rendered or already-scheduled video. For script revisions update the same Google Doc. Maintain ≤30 seconds, persistent title, exact narration, selected avatar and fixed voice. During first ten tests use a paused HeyGen Plan/Chat approval before render unless the user explicitly overrides for that row. After completed video, update Sheet J immediately; use the Buffer plugin with a fresh direct MP4 and an expiry check, and record scheduled/published IDs and URLs. Report verified results, not assumptions.

## Repository

Private canonical repository: https://github.com/Anurag99singh/heygen-youtube-shorts-automation

The complete production workflow lives at this repository root. The separate Daily AI Trend Briefing stays in https://github.com/Anurag99singh/consistent-explainer-videos-v3/blob/main/skills/ai-trend-briefing/SKILL.md . Existing v3 workflows remain unchanged.

## Verified pilot schedule
VID-001: Buffer post `6af6de6cfe8cb9dc190a4a45`, status `scheduled`, 13 November 2026 at **17:36 IST** (`2026-11-13T12:06:00Z`), Automatic / Add to Queue. Retrieved through `get_post` with video asset, YouTube Short metadata and no error. Publication has not yet been confirmed; read live Sheet/Buffer on every run.
