import importlib.util
from pathlib import Path
import re, unittest
spec=importlib.util.spec_from_file_location('contract',Path(__file__).resolve().parents[1]/'scripts/script_contract.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
class ContractTests(unittest.TestCase):
    def setUp(self):
        self.fields={key:'Topic-specific content' for key in re.findall(r'{{([A-Z0-9_]+)}}',c.TEMPLATE.read_text())}
        for i in range(1,5): self.fields[f'SCENE_{i}_NARRATION']=' '.join(['word']*18)
    def test_complete_render_preserves_footer(self):
        result=c.render(self.fields)
        self.assertNotIn('{{',result)
        # The full IMPORTANT block must pass unchanged to the renderer.
        self.assertEqual(result.split('**IMPORTANT:**')[1],c.TEMPLATE.read_text().split('**IMPORTANT:**')[1])
    def test_missing_field_rejected(self):
        self.fields.pop('TOPIC')
        with self.assertRaises(ValueError):c.render(self.fields)
    def test_extra_field_rejected(self):
        self.fields['NEW_FOOTER']='rewrite'
        with self.assertRaises(ValueError):c.render(self.fields)
    def test_long_narration_rejected(self):
        self.fields['SCENE_1_NARRATION']=' '.join(['word']*40)
        with self.assertRaises(ValueError):c.render(self.fields)
    def test_nested_prompt_rejected(self):
        self.fields['TOPIC']='**TOPIC:** another prompt'
        with self.assertRaises(ValueError):c.render(self.fields)
if __name__=='__main__':unittest.main()
