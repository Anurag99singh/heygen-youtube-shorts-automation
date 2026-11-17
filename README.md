# HeyGen → YouTube Shorts

Start with [SKILL.md](SKILL.md). It connects the existing trend research → dedicated script writer → same Google Doc → HeyGen → QA → Buffer → verified YouTube publication.

## Files to use
- [Script-writing skill](skills/script-writer/SKILL.md): story quality and allowed dynamic fields.
- [Fixed script template](skills/script-writer/template.md): your successful format, adapted to 30–35 seconds.
- [Workflow](references/workflow.md): generation, monitoring, QA, scheduling and publication.
- [Sheet schema](references/sheet-schema.md), [posting copy](references/youtube-caption.md), [configuration](config/workflow.json).

Older reference filenames contain short redirects for compatibility. Repository-migration instructions and incident narratives were removed from the active workflow; Git history preserves them. Account IDs, queue and cancelled pilot guards are retained.

## Test the writer
Ask: “Use skills/script-writer/SKILL.md to draft one source-verified topic. Script-only test: stop before HeyGen or Buffer.”

The writer renders only variable fields into the fixed template with `python scripts/script_contract.py --fields work/fields.json --output work/prompt.md`. It checks placeholder completeness and narration length; it does not verify facts or guarantee video runtime. Read back the saved Doc before generation. Existing production and handoff automations remain paused until explicitly resumed.
