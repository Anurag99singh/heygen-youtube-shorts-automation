"""Render the user's fixed script format; reject missing/extra fields and oversized narration."""
import argparse, json, re
from pathlib import Path
TEMPLATE = Path(__file__).resolve().parents[1] / 'skills/write-shorts-script/template.md'
def render(fields, theme="Editorial 2D"):
    template = TEMPLATE.read_text()
    profiles = json.loads((TEMPLATE.parent / 'themes.json').read_text())
    if theme not in profiles:
        raise ValueError(f'Unknown theme: {theme}')
    profile = profiles[theme]
    for key, value in {'THEME_NAME': theme, 'TITLE_STYLE': profile['title'], 'THEME_DIRECTIONS': profile['broll'], 'CAPTION_STYLE': profile['captions']}.items():
        template = template.replace('{{'+key+'}}', value)
    names = set(re.findall(r'{{([A-Z0-9_]+)}}', template))
    if set(fields) != names:
        raise ValueError(f'Missing: {names-set(fields)}; unexpected: {set(fields)-names}')
    for key, value in fields.items():
        if not isinstance(value, str) or not value.strip() or '{{' in value or '}}' in value:
            raise ValueError(f'Invalid field: {key}')
        if '### OVERALL VIDEO DIRECTIONS' in value or '**TOPIC:**' in value:
            raise ValueError(f'Nested production prompt in {key}')
    count = sum(len(re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", fields[f'SCENE_{i}_NARRATION'])) for i in range(1,5))
    if not 65 <= count <= 80:
        raise ValueError(f'Narration has {count} words; draft 65–80 before rendering')
    return re.sub(r'{{([A-Z0-9_]+)}}', lambda m: fields[m[1]], template)
if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--fields', type=Path, required=True); p.add_argument('--output', type=Path, required=True); p.add_argument('--theme', default='Editorial 2D')
    a = p.parse_args(); result = render(json.loads(a.fields.read_text()), a.theme); a.output.write_text(result)
    print('PASS: complete fields, 65–80 narration words, fixed template rendered. Actual runtime and factual/visual QA still required.')
