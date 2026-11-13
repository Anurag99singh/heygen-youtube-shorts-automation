# Script-writing template (human-readable HeyGen prompt)

Read the user's [IBM & Microsoft reference](https://docs.google.com/document/d/1aXsLa5MABozi7aBf4vbSmnplPdPyd6mNyRcb-JCkd0w/edit) before writing. Use **simple language**, natural conversational speech, and direct visual instructions. Do not copy the reference's factual claims into unrelated topics. Do not put voice IDs, prompt orchestration, scheduler setup, approval counters or API jargon into the visible script. Those belong in the Sheet/this skill.

## Word-count and timing
- English 30-second ceiling; aim for about **55–65 spoken words** and 27–29 seconds depending on voice pace, leaving room for transitions. Do **not** assume estimated reading time equals actual output. Check final video duration.
- Prefer **four scenes**: 0–6s, 6–13s, 13–21s, 21–29s (adjust naturally so total ≤30s).
- Do not claim independent performance tests when only a company announcement exists.
- CTA should end with a simple question, not a generic slogan.
- Use a concise video title so the permanent one-line title fits in 9:16 safe margins.

## Copy-ready HeyGen prompt (replace brackets)
```text
HEYGEN VIDEO PROMPT

TOPIC: [Specific AI-software story]
TOTAL LENGTH: Maximum 30 seconds
FORMAT: Vertical 9:16 Reel
TONE: Professional, conversational, informative and engaging.

SCENE 1 — HOOK (0–6 sec) | AVATAR

VISUAL:
[Camera-facing avatar in a simple, relevant modern setting; uncluttered and credible.]

NARRATION:
[curious, upbeat]
“[Exact approved spoken hook.]”

DELIVERY DIRECTION:
[One or two sentences about a natural emphasis and pacing.]

SCENE 2 — THE FEATURE (6–13 sec) | B-ROLL

VISUAL:
[Relevant product capability or app workflow, realistically illustrated. No invented official UI.]

NARRATION:
[informative, confident]
“[Exact approved fact-checked spoken line.]”

DELIVERY DIRECTION:
[How to speak it; concise.]

SCENE 3 — WHY IT MATTERS (13–21 sec) | B-ROLL

VISUAL:
[Two or three specific credible examples supporting spoken lines, no generic AI imagery.]

NARRATION:
[thoughtful, explanatory]
“[Exact approved practical implication.]”

DELIVERY DIRECTION:
[Plain-language emphasis.]

SCENE 4 — CLOSING QUESTION (21–29 sec) | AVATAR

VISUAL:
[Brief relevant footage, then the SAME avatar, clothing, voice and setting as Scene 1.]

NARRATION:
[curious, engaging]
“[Exact approved closing question.]”

DELIVERY DIRECTION:
[Relaxed, genuine question; do not rush.]

OVERALL VIDEO DIRECTIONS

TITLE DISPLAY:
Display “[ONE-LINE VIDEO TITLE]” throughout ALL scenes and transitions. Approximately 44 pt, just below the top edge with safe margins. Never cover the avatar's face.

TEXT AND VISUALS:
Keep text cards short, centered in the safe middle portion, readable on phones. Use realistic B-roll that matches the narration. No generic robots, holograms or glowing brains.

AVATAR:
Use the selected avatar consistently with natural expressions and subtle gestures. Keep clothing, setting and voice consistent.

AUDIO AND EDITING:
Subtle background music, smooth cuts, complete runtime ≤30 seconds. Do not add subtitles, captions or watermarks.

IMPORTANT:
Use the narration exactly as written. Do not add, rewrite or remove spoken lines.
```

## Workflow
1. Select source-backed news story from READY row. Check claims against original article.
2. Edit existing Doc link in D, or create one only for a new row without a Doc.
3. Write the Doc link and mark SCRIPT REVIEW; wait for E=APPROVE.
4. If E=REVISE, use feedback F to edit **the same Doc** and set E back to PENDING.
5. HeyGen submission after approval is **only the Doc body text**, without ChatGPT wrapper/preamble.
