#!/usr/bin/env python3
"""Regenerate two original mathematical/flow examples for the ML glossary.

Run with Python 3, NumPy and Matplotlib installed. The source root is resolved
from this script, and only the two named SVG outputs are written.
"""
from pathlib import Path
from html import escape
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'docs/computational-science/machine-learning/images'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'svg.fonttype': 'none', 'svg.hashsalt': 'ml-glossary-examples', 'font.size': 12})
x = np.linspace(-2, 2, 501)
f1 = x
f2 = x + 0.5*x*(x*x-1)
train_x = np.array([-1., 0., 1.])
assert np.allclose(train_x + 0.5*train_x*(train_x**2-1), train_x)
assert 0.5 + 0.5*0.5*(0.5**2-1) == 0.3125
assert 2 + 0.5*2*(2**2-1) == 5
fig, ax = plt.subplots(figsize=(7, 4.1), layout='constrained')
ax.axvspan(-1, 1, color='#eeeeee', label='Observed input interval')
ax.plot(x, f1, color='#176493', lw=2, label=r'$f_1(x)=x$')
ax.plot(x, f2, color='#b95b00', lw=2, label=r'$f_2(x)=x+0.5x(x^2-1)$')
ax.scatter(train_x, train_x, color='black', s=37, zorder=5, label='Shared training points')
ax.set(xlim=(-2, 2), ylim=(-6, 6), xlabel=r'$x$ (dimensionless)', ylabel=r'$f(x)$ (dimensionless)')
ax.set_xticks([-2,-1,0,1,2]); ax.set_yticks([-6,-3,0,3,6])
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.tick_params(direction='in', top=True, right=True)
for spine in ax.spines.values(): spine.set_color('black'); spine.set_linewidth(1.2)
ax.grid(False)
ax.legend(frameon=False, loc='upper left', fontsize=10)
plot_path = OUT / 'interpolation-extrapolation.svg'
fig.savefig(plot_path, metadata={'Date': None})
plot_path.write_text('\n'.join(line.rstrip() for line in plot_path.read_text().splitlines()) + '\n')
plt.close(fig)

parts=['<svg xmlns="http://www.w3.org/2000/svg" width="920" height="410" viewBox="0 0 920 410">',
'<rect width="920" height="410" fill="white"/>',
'<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="#243441"/></marker></defs>',
'<g font-family="DejaVu Sans, sans-serif" fill="#172531">']
def text(x,y,value,size=20):
 parts.append(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="middle">{escape(value)}</text>')
def box(x,y,w,h,lines,color):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{color}" stroke="#243441" stroke-width="1.6"/>')
 for k,line in enumerate(lines): text(x+w/2, y+h/2+(k-(len(lines)-1)/2)*27+7, line)
def arrow(points):
 parts.append(f'<polyline points="{points}" fill="none" stroke="#243441" stroke-width="1.8" marker-end="url(#arrow)"/>')
text(460,31,'Split by original group',23)
box(20,155,205,90,['Original groups','A, B, C, D'],'#f0f2f4')
box(320,60,205,80,['Training','A, B'],'#e6f0f7')
box(320,160,205,80,['Validation','C'],'#f0f2f4')
box(320,260,205,80,['Test','D'],'#f0f2f4')
box(620,60,275,80,['Training augmentation','A1, A2, B1, B2'],'#fff1dd')
arrow('225,200 265,200 265,100 320,100')
arrow('225,200 320,200')
arrow('225,200 265,200 265,300 320,300')
arrow('525,100 620,100')
text(463,382,'Each transformed copy retains its original group.',18)
parts.extend(['</g>','</svg>'])
(OUT/'augmentation-split.svg').write_text('\n'.join(parts)+'\n')
print('Saved two SVG examples')
