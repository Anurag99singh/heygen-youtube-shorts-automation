# Repository migration record

Created the private canonical repository https://github.com/Anurag99singh/heygen-youtube-shorts-automation on 13 November 2026. Copied the complete production folder from `Anurag99singh/consistent-explainer-videos-v3/skills/heygen-youtube-shorts/` to this repository root, and preserved `.agents/skills/heygen-youtube-shorts/SKILL.md` as the discovery entry. All Google, HeyGen, Buffer, voice, approval and automation IDs remain unchanged. Daily AI Trend Briefing stays in v3. Verify live Google Sheet and Buffer before relying on any pilot status.

## Original migration instructions (historical)

# Move this skill to its own new GitHub repository

## Why this page exists
The current connected GitHub tool can write to repositories but **does not expose create-repository**. The skill was therefore pushed to the existing **private** `Anurag99singh/consistent-explainer-videos-v3` repository. The user's original request is a **new independent repository**. Use an authenticated **ChatGPT Work cloud browser** (or GitHub's website) to complete this setup.

## Suggested repository
- Owner: `Anurag99singh`
- Repository name: `heygen-youtube-shorts-automation`
- Visibility: **Private by default**. Do not make it public without the user's approval.
- Default branch: `main`
- Description: `AI software Shorts production skill: Google Sheets, Google Docs, HeyGen Video Agent, Buffer and YouTube`.

## Steps in ChatGPT Work
1. Open logged-in GitHub and create **new private repository** with the suggested name.
2. Copy **the complete contents** of `skills/heygen-youtube-shorts/` from the existing v3 repo to the **root** of the new repo. Keep `SKILL.md`, `README.md`, `CLOUD_START.md`, `config/workflow.json`, `references/*`, `NEW_REPO_SETUP.md`.
3. Copy `.agents/SKILL.md` from the existing v3 repo into the new repo's same path. Adjust its reference so it points to the new repo root `SKILL.md` rather than the old nested path.
4. Fix internal relative links and GitHub URLs in `CLOUD_START.md`, `README.md`, `references/schedulers.md`, and `config/workflow.json` to point to the new repository. **Preserve all original Google Sheet, Google Doc, HeyGen and Buffer IDs and policies.**
5. Verify `SKILL.md`, the JSON config and each reference file are readable on GitHub; use `main` branch links.
6. Change Sheet Settings' GitHub Skill reference to the new repo's `SKILL.md`. Update the active automation prompts **only after verifying the new skill is accessible**.
7. Keep existing Daily AI Trend Briefing skill in v3; the new repo may point to it rather than duplicating it.
8. Don't store passwords, API keys, tokens, temporary signed HeyGen download URLs or Google OAuth credentials in either repo.

## Work prompt (copy)
> In the cloud browser, create a private GitHub repository `Anurag99singh/heygen-youtube-shorts-automation`. Migrate the complete HeyGen skill folder and its Codex discovery entry from my existing private `consistent-explainer-videos-v3` repo. Preserve all workflow configuration, update internal paths for the new repo, verify the files on main, then update the active ChatGPT automation task prompts and Google Sheet GitHub skill link. Do not delete or break existing v3 video/trend skills. Do not make anything public.

## Independent of repository creation: Buffer publishing
VID-001 has a verified 23.2-second completed HeyGen video, and an unscheduled Buffer Idea. To schedule: Work browser downloads the actual MP4 from the permanent HeyGen page, opens the Buffer YouTube channel, uploads the MP4, uses the saved idea caption, chooses **automatic queue**, confirms a scheduled post ID and updates Sheet M and L. Work browser upload is required because the existing HeyGen direct MP4 URL expires.
