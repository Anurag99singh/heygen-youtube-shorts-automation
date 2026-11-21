---
name: write-shorts-script
description: Write source-backed 30–35-second HeyGen AI-news production scripts using the user's fixed editorial template.
---

# Write the script

Read [template.md](template.md) in full before every draft or revision. It is the canonical output format, derived from the user's successful Wallet example on 17 November 2026. That example supplies style, not evidence that a product or security claim exists. The previous IBM/Microsoft reference is no longer the writing authority.

## Inputs and output
Inputs: verified topic and dated original sources, audience consequence, demonstrated capability, material caveats and selected avatar context. Output: one filled production prompt in the existing row's Google Doc D. For a new row create one Doc only. Keep research evidence, source URLs, YouTube title U, description V, hashtags and operational IDs outside this Doc. Return the exact same prompt to HeyGen; do not prepend a second instruction block.

## Develop the story before filling the template
1. Verify the announcement, product name, availability and all mechanism/security claims against original sources. Attribute vendor claims; never invent a benchmark, payment requirement, biometric check or personal test. Skip a topic without enough verified substance.
2. Scene 1: one concrete curiosity question grounded in a useful capability, followed by the named announcement. Avoid a greeting, hype and vague questions.
3. Scene 2: explain what changed through a specific user action → product action → result. Show a realistic sequence, not a list of features.
4. Scene 3: explain the one mechanism, safeguard or limitation viewers need to understand. Use a short question heading suited to the story (e.g. HOW DOES IT WORK?). Security is optional and must be evidenced. Do not reuse payment details for unrelated stories.
5. Scene 4: explain the practical consequence and a material availability limit or caveat. End reflectively, as in the user's example; no forced engagement CTA.
6. Write roughly 65–80 spoken words total, simple conversational English. Allocate about 6/9/10/8 seconds across scenes. Cut secondary claims before accelerating narration. Narration estimates do not prove runtime: final measured video must be 30.0–35.0s, target 32–34.
7. For every scene write specific visuals that demonstrate its narration, plus natural delivery/emphasis tied to exact words. Keep scene 1 avatar, scenes 2–3 B-roll, scene 4 B-roll returning to the same avatar. Use distinct illustrated editorial sequences, not realistic footage or generic AI imagery. Illustrative interfaces must not pretend to be official product footage.

## Fixed text and allowed substitutions
Fill only {{...}} slots in template.md. Preserve every other character, including opening metadata labels, FORMAT, TONE, scene labels/timing/emotion cues and all OVERALL VIDEO DIRECTIONS. The duration has deliberately been adapted from the 40-second example to the user's confirmed 30–35-second requirement.

Allowed dynamic fields: TOPIC; VIDEO_TITLE; SCENE_3_HEADING; each scene's VISUAL, NARRATION, DELIVERY; CALLOUTS (three short quoted phrases separated by commas/and); BROLL_SUBJECTS (topic-specific realistic footage); DEMONSTRATION_PROCESS (the process to show). Keep title short enough for one line at 44, consistent across scenes. No other boilerplate rewrites. The footer requires native Video Agent subtitles throughout, including B-roll, as explicitly updated by the user. YouTube description V remains separate. Never revert to the earlier no-subtitles instruction.

## Required checks before handoff
- Every narration claim has source support; visuals do not imply extra capabilities.
- Four scenes form one developed explanation with a practical ending.
- All placeholders filled; narration 65–80 words as a drafting guide; natural delivery fits the timing without rushing.
- Fixed prefix/footer match template exactly outside allowed slots; no backend IDs, description or hashtags in the Doc.
- Run `python scripts/script_contract.py --fields work/fields.json --output work/prompt.md` from plugin root. Supply a JSON object containing exactly the template fields. This renders the fixed text and checks word count. If Python is unavailable, perform the same comparisons explicitly and report that executable validation was unavailable.
- Read back the saved Doc and compare to the rendered prompt before any generation. A later revision updates the same Doc and reruns these checks. Never rewrite a script already bound to an active/completed render on a retry.

For a script-only test, render and inspect the prompt, then stop before HeyGen. Production authorization is owned by the main pipeline, not this writing skill.

## Distribution copy handoff
Use caption-writer for U/V/AA/AB. Copy is separate from narration. Current pipeline ends at approved email handoff; never schedule through Buffer.

## Visual style — consistent editorial B-roll
Use the template's single warm-paper 2D editorial theme for every B-roll: dark ink, muted blue, sage green, restrained yellow; serif headings, sans-serif labels; centered flat vector illustrations and clear sequential motion. Each scene explains its narration through specific objects, actions and a readable result. Preserve object continuity without recycling the same scene. Never request photorealistic footage.

Whenever an avatar is on screen, show only the avatar in the consistent studio, permanent title banner and synchronized subtitles. Keep every icon, prop, diagram, label and illustration exclusively in separate B-roll shots. Scene 4 cuts from B-roll back to the clean presenter; never composite them together. The title banner remains visible across the whole video and every transition.

Before saving, check all scene VISUAL fields against these rules; the footer cannot repair a contradictory scene description. Keep the existing four scenes, narration/source standards, 30–35-second target, voice, manual approvals and email handoff. The Gemini Tasks sample supplies visual direction only, not claims, a new topic, a five-scene requirement or an exact-35-second mandate.
