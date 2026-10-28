#!/usr/bin/env python3
"""Check publication record integrity; this cannot verify scientific truth."""
import hashlib
import json
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def walk_nav(node):
    if isinstance(node, list):
        for item in node:
            yield from walk_nav(item)
    elif isinstance(node, dict):
        for value in node.values():
            yield from walk_nav(value)
    elif isinstance(node, str):
        yield node


def check(root):
    docs = root / 'docs'
    config = yaml.safe_load((root / 'mkdocs.yml').read_text(encoding='utf-8'))
    registry = json.loads((root / 'refs/quality/registry.json').read_text(encoding='utf-8'))
    nav = list(walk_nav(config.get('nav', [])))
    issues = []
    if len(nav) != len(set(nav)):
        issues.append('navigation contains duplicate paths')
    articles = {p.relative_to(docs).as_posix() for p in docs.rglob('*.md') if p.name != 'index.md'}
    pages = {p.relative_to(docs).as_posix() for p in docs.rglob('*.md')}
    for path in nav:
        if not (docs / path).is_file():
            issues.append(f'navigation path missing: {path}')
    for path in sorted(pages):
        if nav.count(path) != 1:
            issues.append(f'page must occur once in navigation: {path}')
    for path in sorted(articles):
        content = (docs / path).read_text(encoding='utf-8')
        if not content.startswith('---\n') or '\ndescription:' not in content:
            issues.append(f'article requires description front matter: {path}')
        if len(re.findall(r'^#\s+', content, re.M)) != 1:
            issues.append(f'article requires exactly one H1: {path}')
        if re.search(r'^#{4,}\s+', content, re.M):
            issues.append(f'article must not use H4 or deeper: {path}')
        if re.search(r'^##\s+(?!\d+\.\s)', content, re.M) or re.search(r'^###\s+(?!\(\d+\)\s)', content, re.M):
            issues.append(f'heading numbering invalid: {path}')
        if re.search(r'<img\b|!\[[^\]]*\]\[', content, re.I):
            issues.append(f'HTML or reference-style images require manual handling: {path}')
        entry = registry.get(path)
        if not entry or entry.get('status') != 'pass':
            issues.append(f'article lacks a pass record: {path}')
            continue
        coverage = entry.get('coverage', {})
        if coverage.get('mode') not in {'full', 'changes', 'meaning-preserving'} or not coverage.get('description'):
            issues.append(f'coverage missing or invalid: {path}')
        if coverage.get('mode') != 'full' and (not re.fullmatch(r'[0-9a-f]{64}', str(coverage.get('baseline_sha256', ''))) or not entry.get('prior_evidence')):
            issues.append(f'baseline or previous evidence missing: {path}')
        reviewer = entry.get('reviewer', {})
        if not reviewer.get('role') or reviewer.get('independent') is not True or not reviewer.get('date'):
            issues.append(f'independent review missing: {path}')
        sources = entry.get('sources', {})
        findings = entry.get('findings', [])
        if not findings:
            issues.append(f'findings missing: {path}')
        for finding in findings:
            if finding.get('status') != 'supported' or not finding.get('claim') or not finding.get('scope'):
                issues.append(f'unsupported or incomplete finding: {path}')
            refs = finding.get('sources', [])
            verified = [sources.get(ref, {}) for ref in refs]
            provenance = {str(item.get('provenance', '')).strip().casefold() for item in verified if item.get('provenance')}
            urls = {str(item.get('url', '')).strip().rstrip('/').casefold() for item in verified if item.get('url')}
            if (len(provenance) < 2 or len(urls) < 2
                    or any(not item.get('url') or not item.get('location') or not item.get('provenance') for item in verified)):
                issues.append(f'finding needs two documented independent sources: {path}')
        if entry.get('document_sha256') != digest(docs / path):
            issues.append(f'article changed since verification: {path}')
        evidence_rel = Path(entry.get('evidence', ''))
        evidence = (root / evidence_rel).resolve()
        if not evidence.is_relative_to((root / 'refs/quality/evidence').resolve()) or not evidence.is_file():
            issues.append(f'evidence missing or outside evidence directory: {path}')
        elif entry.get('evidence_sha256') != digest(evidence):
            issues.append(f'evidence changed since registration: {path}')
        elif coverage.get('mode') != 'full' and coverage.get('baseline_sha256') not in evidence.read_text(encoding='utf-8'):
            issues.append(f'baseline is not recorded in evidence: {path}')
        for previous in entry.get('prior_evidence', []):
            target = (root / previous['path']).resolve()
            if not target.is_relative_to((root / 'refs/quality/evidence').resolve()) or not target.is_file() or digest(target) != previous['sha256']:
                issues.append(f'previous evidence missing or changed: {path}')
        for match in re.findall(r'!\[[^\]]*\]\(([^)\s]+)', content):
            if '://' in match:
                issues.append(f'external image forbidden: {path}: {match}')
                continue
            target = ((docs / path).parent / match).resolve()
            if not target.is_relative_to(docs.resolve()):
                issues.append(f'image outside docs: {path}: {match}')
            elif target.relative_to(docs.resolve()).as_posix() not in entry.get('assets', {}):
                issues.append(f'image lacks recorded hash: {path}: {match}')
        for asset, expected in entry.get('assets', {}).items():
            target = (docs / asset).resolve()
            if not target.is_relative_to(docs.resolve()) or not target.is_file() or digest(target) != expected:
                issues.append(f'asset missing or changed: {asset}')
    return issues


if __name__ == '__main__':
    try:
        failures = check(ROOT)
    except (OSError, ValueError, TypeError, yaml.YAMLError) as exc:
        failures = [f'quality check failed: {exc}']
    for failure in failures:
        print(f'ERROR: {failure}', file=sys.stderr)
    if failures:
        sys.exit(1)
    print('Publication record integrity check passed; scientific review remains independent.')
