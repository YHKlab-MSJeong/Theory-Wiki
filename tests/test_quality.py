import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


spec = importlib.util.spec_from_file_location('quality', Path(__file__).resolve().parents[1] / 'scripts/check_quality.py')
quality = importlib.util.module_from_spec(spec)
spec.loader.exec_module(quality)


class QualityCheckTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='wiki-quality-test-')
        self.root = Path(self.temp.name)
        (self.root / 'docs').mkdir()
        (self.root / 'refs/quality/evidence').mkdir(parents=True)
        self.doc = self.root / 'docs/article.md'
        self.doc.write_text('---\ndescription: 설명\n---\n# Article\n', encoding='utf-8')
        self.evidence = self.root / 'refs/quality/evidence/evidence.md'
        self.evidence.write_text('review', encoding='utf-8')
        self.registry = self.root / 'refs/quality/registry.json'
        self.registry.write_text(json.dumps({'article.md': {
            'status': 'pass', 'document_sha256': quality.digest(self.doc),
            'evidence': 'refs/quality/evidence/evidence.md',
            'evidence_sha256': quality.digest(self.evidence), 'assets': {},
            'coverage': {'mode': 'full', 'description': 'entire document'},
            'reviewer': {'role': 'independent reviewer', 'independent': True, 'date': '2026-10-28'},
            'sources': {'a': {'url': 'https://a.example', 'location': 'p. 1', 'provenance': 'a'},
                        'b': {'url': 'https://b.example', 'location': 'p. 2', 'provenance': 'b'}},
            'findings': [{'claim': 'claim', 'scope': 'conditions', 'status': 'supported', 'sources': ['a', 'b']}],
        }}), encoding='utf-8')
        (self.root / 'mkdocs.yml').write_text('nav:\n  - Article: article.md\n', encoding='utf-8')

    def tearDown(self):
        self.temp.cleanup()

    def test_verified_document_passes(self):
        self.assertEqual(quality.check(self.root), [])

    def test_document_changes_are_blocked(self):
        self.doc.write_text(self.doc.read_text(encoding='utf-8') + 'New claim.\n', encoding='utf-8')
        self.assertTrue(any('article changed' in x for x in quality.check(self.root)))

    def test_evidence_changes_are_blocked(self):
        self.evidence.write_text('modified', encoding='utf-8')
        self.assertTrue(any('evidence changed' in x for x in quality.check(self.root)))

    def test_unregistered_article_is_blocked(self):
        self.registry.write_text('{}', encoding='utf-8')
        self.assertTrue(any('lacks a pass record' in x for x in quality.check(self.root)))

    def test_unverified_finding_is_blocked(self):
        data = json.loads(self.registry.read_text())
        data['article.md']['findings'][0]['status'] = 'inaccessible'
        self.registry.write_text(json.dumps(data))
        self.assertTrue(any('unsupported' in x for x in quality.check(self.root)))

    def test_duplicate_provenance_is_blocked(self):
        data = json.loads(self.registry.read_text())
        data['article.md']['sources']['b']['provenance'] = 'A'
        self.registry.write_text(json.dumps(data))
        self.assertTrue(any('two documented' in x for x in quality.check(self.root)))

    def test_duplicate_url_is_blocked(self):
        data = json.loads(self.registry.read_text())
        data['article.md']['sources']['b']['url'] = 'https://a.example/'
        self.registry.write_text(json.dumps(data))
        self.assertTrue(any('two documented' in x for x in quality.check(self.root)))

    def test_string_false_reviewer_is_blocked(self):
        data = json.loads(self.registry.read_text())
        data['article.md']['reviewer']['independent'] = 'false'
        self.registry.write_text(json.dumps(data))
        self.assertTrue(any('independent review' in x for x in quality.check(self.root)))

    def test_missing_baseline_chain_is_blocked(self):
        data = json.loads(self.registry.read_text())
        data['article.md']['coverage'] = {'mode': 'changes', 'description': 'changed', 'baseline_sha256': 'fake'}
        self.registry.write_text(json.dumps(data))
        self.assertTrue(any('baseline' in x for x in quality.check(self.root)))


if __name__ == '__main__':
    unittest.main()
