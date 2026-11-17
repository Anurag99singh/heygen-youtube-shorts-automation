# HeyGen YouTube Shorts

Read [main pipeline](SKILL.md). It uses only the [topic/review workbook](https://docs.google.com/spreadsheets/d/1uWtWc04CIZwGD5EqaE1YBOdkE8UIVU4O8SmZisERlI8/edit).

Three workers:
1. Daily 10:00 IST: select supplied topic → [script writer](skills/script-writer/SKILL.md) → manual script review.
2. Hourly: check existing HeyGen jobs → update Sheet → manual video review.
3. Hourly: process approvals/revisions → approved script to HeyGen; approved video to Buffer; verify publication.

In Video Queue use E for script APPROVE/REVISE, I for video APPROVE/REVISE, F for feedback. PENDING waits. No automatic approval.

The [fixed template](skills/script-writer/template.md) and [contract renderer](scripts/script_contract.py) support the writer. All workflow instructions and column mapping are in SKILL.md. No other topic spreadsheet or supporting workflow documents are required.

Always generate through Video Agent with the complete production prompt. Burned-in subtitles are mandatory; YouTube description V is separate.
