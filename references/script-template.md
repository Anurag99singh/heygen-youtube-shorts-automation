# Current production policy — 13 November 2026
The user explicitly removed ALL manual script, plan, first-ten-test and final-publication approval gates. Run unattended: daily production starts at **10:00 IST**; daily trend research stays at 09:00 IST. Pick topic, write script, generate through HeyGen Video Agent, monitor, validate and schedule through Buffer plugin for **next day 09:00 IST** without asking for routine approval.
YouTube description means text BELOW the posted video: store it in V (YouTube Description), title in U. Never append description, hashtags, source footer or a separate caption section to the spoken script/HeyGen Doc. Pass V only to Buffer text. On-video subtitle settings remain unchanged.
Retain strict 30–35s measured duration, fixed voice d35557f1a8e24de1a34345cf58a30e51, selected/default avatar resolved by exact look ID, factual/visual QA and duplicate prevention. E/I/P are legacy review fields, not eligibility gates; do not write APPROVE pretending a human reviewed. Respect an explicit future user HOLD/REVISE/stop.
VID-001 was manually removed from Buffer by the user. Keep its recorded IDs as history, mark it intentionally cancelled in notes, exclude it from production/reconciliation retries and do not recreate it. It must not block new daily videos.

# Script-writing template (human-readable HeyGen prompt)

Read the user's [IBM & Microsoft reference](https://docs.google.com/document/d/1aXsLa5MABozi7aBf4vbSmnplPdPyd6mNyRcb-JCkd0w/edit) before writing. Use **simple language**, natural conversational speech, and direct visual instructions. Do not copy the reference's factual claims into unrelated topics. Do not put voice IDs, prompt orchestration, scheduler setup, approval counters or API jargon into the visible script. Those belong in the Sheet/this skill.

## Word-count and timing
- English **30–35-second inclusive range**; aim for roughly **65–80 spoken words**, adjusted to the fixed voice, with 32–34 seconds total including transitions. Do **not** assume estimated reading time equals actual output. Check final video duration.
- Prefer **four scenes**: 0–6s, 6–15s, 15–26s, 26–33s (adjust naturally while keeping the complete video within 30–35s).
- Do not claim independent performance tests when only a company announcement exists.
- CTA should end with a simple question, not a generic slogan.
- Use a concise video title so the permanent one-line title fits in 9:16 safe margins.

## Copy-ready HeyGen prompt (replace brackets)
```text
HEYGEN VIDEO PROMPT

TOPIC: [Specific AI-software story]
TOTAL LENGTH: 30–35 seconds inclusive; target 33 seconds
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

SCENE 2 — THE FEATURE (6–15 sec) | B-ROLL

VISUAL:
[Relevant product capability or app workflow, realistically illustrated. No invented official UI.]

NARRATION:
[informative, confident]
“[Exact approved fact-checked spoken line.]”

DELIVERY DIRECTION:
[How to speak it; concise.]

SCENE 3 — WHY IT MATTERS (15–26 sec) | B-ROLL

VISUAL:
[Two or three specific credible examples supporting spoken lines, no generic AI imagery.]

NARRATION:
[thoughtful, explanatory]
“[Exact approved practical implication.]”

DELIVERY DIRECTION:
[Plain-language emphasis.]

SCENE 4 — CLOSING QUESTION (26–33 sec) | AVATAR

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
Subtle background music, smooth cuts, complete runtime between 30 and 35 seconds inclusive. Do not add subtitles, captions or watermarks.

IMPORTANT:
Use the narration exactly as written. Do not add, rewrite or remove spoken lines.
```

## Workflow
1. Select source-backed news story from READY row. Check claims against original article.
2. Edit existing Doc link in D, or create one only for a new row without a Doc.
4. If E=REVISE, use feedback F to edit **the same Doc** and set E back to PENDING.
5. HeyGen submission after approval is **only the Doc body text**, without ChatGPT wrapper/preamble.

