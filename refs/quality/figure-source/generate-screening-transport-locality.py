from pathlib import Path
import sys
from html import escape

out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
figures = {
 'ml-hamiltonian-overview.svg': ('Learned Hamiltonians for quantum transport', [('Small structures','DFT training data'), ('Model training','band energies or H / S'), ('Larger structure','environment → H'), ('Transport','NEGF; Poisson if included')], 'Overlap and electrostatics must be specified for the chosen model.'),
 'high-k-selection.svg': ('High-k candidate screening', [('Bulk candidates','phase / stability'), ('Electronic & dielectric','band gap / permittivity'), ('Interface & film','offsets / defects / reactions'), ('Device assessment','process / leakage')], 'Criteria depend on structure and calculation conditions; no numerical thresholds shown.'),
 'block-stitching.svg': ('Repeated channel blocks and open boundaries', [('Left contact','self-energy ΣL'), ('Channel layer 1','H₀, S₀'), ('Channel layer 2 … N','H₀, S₀'), ('Right contact','self-energy ΣR')], 'Adjacent layers require both H and S coupling. RGF uses the resulting block structure.'),
 'order-n-locality.svg': ('Locality in linear-scaling electronic structure', [('Electronic locality','density matrix decay'), ('Controlled truncation','localization cutoff'), ('Sparse operations','localized representation'), ('Electronic structure','density / SCF update')], 'Accuracy depends on cutoff and electronic conditions; the diagram is not timing data.')
}
for name, (title, boxes, note) in figures.items():
    x0, gap, width = 24, 26, 265
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 280" role="img">', '<rect width="1200" height="280" fill="white"/>', '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9 Z" fill="#34495e"/></marker></defs>', f'<text x="600" y="40" text-anchor="middle" font-family="sans-serif" font-size="24" font-weight="bold" fill="#172b3a">{escape(title)}</text>']
    for i, (a,b) in enumerate(boxes):
        x=x0+i*(width+gap)
        s += [f'<rect x="{x}" y="78" width="{width}" height="105" rx="9" fill="#edf4f7" stroke="#34596b" stroke-width="2"/>',f'<text x="{x+width/2}" y="119" text-anchor="middle" font-family="sans-serif" font-size="21" font-weight="bold" fill="#172b3a">{escape(a)}</text>', f'<text x="{x+width/2}" y="151" text-anchor="middle" font-family="sans-serif" font-size="17" fill="#283f4d">{escape(b)}</text>']
        if i<3:
            marker = '' if name == 'block-stitching.svg' else ' marker-end="url(#arrow)"'
            s.append(f'<path d="M{x+width+3} 130 H{x+width+gap-4}" stroke="#34495e" stroke-width="2"{marker}/>')
    s += [f'<text x="600" y="235" text-anchor="middle" font-family="sans-serif" font-size="17" fill="#3e4e58">{escape(note)}</text>', '</svg>']
    (out/name).write_text('\n'.join(s)+'\n', encoding='utf-8')
