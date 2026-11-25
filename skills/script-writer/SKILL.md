---
name: heygen-shorts-script-writer
description: Write source-backed30–35-second production scripts with Sheet-selected B-roll theme and central audio-synchronized subtitles.
---

# Write or revise a Shorts script

## Inputs
Read the supplied topic/source, exact selected avatar and **AN Visual Theme** from the current queue row. Allowed choices: `Editorial 2D` and `Cinematic 3D`. If AN is blank, use Settings `Default visual theme` (Editorial2D unless explicitly changed). Unknown choices block; never infer theme from topic. Read template.md and themes.json in full. The sample supplies style, not factual evidence.

## Story and structure
Verify product name, announcement, mechanism and availability against original sources. Present AI-tech news to a global audience; retain country/age/plan limits as factual availability notes without implying worldwide access. No invented claims or personal experience.

Keep four timed scenes and65–80 spoken words as drafting guidance, natural delivery,30–35-second measured output. Scene1: concrete curiosity hook and announcement, clean avatar. Scene2: user action → product action → result, B-roll. Scene3: mechanism/safeguard/limitation, B-roll. Scene4: consequence and material caveat, B-roll cutting fully to the clean avatar. One topic and developed explanation, no feature list or forced CTA.

## Visual theme
Use the selected profile for EVERY B-roll scene, title and caption styling. `Editorial 2D` is warm-paper centered vector animation; `Cinematic 3D` is photorealistic technology-documentary CGI with believable interfaces and restrained camera motion. Write specific scene actions in that style; no mixed profiles. Source examples do not change duration or script structure.

Avatar shots show ONLY the chosen presenter in consistent studio, permanent title and subtitles. No adjacent props, illustrations, floating icons, diagrams or extra labels. Supporting visuals belong exclusively to separate B-roll shots. Title is continuous through all scenes/transitions.

## Central subtitles
Follow the one-layer rules in template.md: middle alignment centered at52% height, entire block within45–60%, word-onset reveal into stable short phrases, maximum two lines. Use theme-consistent contrast and typography. Reserve this zone before framing face/torso and placing B-roll action. Never move captions down to avoid a collision. Disable native bottom track; allow a custom synchronized replacement overlay. Verify actual output, not just instructions.

## Render and review
Fill only topic/scene fields; preserve fixed directions. Renderer injects the exact selected profile. Run `python scripts/script_contract.py --fields fields.json --theme "Editorial 2D" --output prompt.md` (or `Cinematic 3D`); if unavailable perform equivalent template/theme/word checks. Read back the saved SAME Google Doc before handoff. No descriptions, hashtags, technical IDs or source footers inside narration. Use caption-writer separately for U/V/AA/AB.

Bind resolved visual theme, exact script, source, avatar and copy to checkpoint O before offering script review. Theme change after review invalidates old approval: re-render scene visuals in same Doc, refresh binding and E=PENDING; never regenerate a completed/sent video merely because AN changed. Preserve attempt and sent history. Completed historical rows are not retroactively restyled. No automatic approvals, rendering or email from this skill.
