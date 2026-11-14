#!/usr/bin/env python3
"""Draw the wiki's original rotation and message-passing schematic.

Run with Python 3 from any directory. Only this repository copy's
docs/computational-science/machine-learning/images/
ml-symmetry-message-passing.svg is written. The drawing uses editable SVG
elements and the installed Roboto font. No publication artwork is reused.

Definitions used in the drawing
https://arxiv.org/html/1802.08219v3, section 3
https://proceedings.mlr.press/v70/gilmer17a/gilmer17a.pdf, section 2
https://arxiv.org/pdf/2101.03164, figure 1 and equation 6

Conditions
Active +90-degree rotation about z in fixed Cartesian axes.
Four nonperiodic atoms at x = 0, 1, 2, 3 angstrom with cutoff 1.1 angstrom.
Initial features are dimensionless illustrative values, not measured data.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / (
    "docs/computational-science/machine-learning/images/"
    "ml-symmetry-message-passing.svg"
)

positions = (0.0, 1.0, 2.0, 3.0)
cutoff = 1.1
neighbors = {
    i: {j for j in range(4) if j != i and abs(positions[j] - positions[i]) < cutoff}
    for i in range(4)
}
dependencies = [{i} for i in range(4)]
features = [1, 2, 4, 8]
history = [features.copy()]
dependency_history = [dependencies]
for _ in range(2):
    features = [features[i] + sum(features[j] for j in neighbors[i]) for i in range(4)]
    dependencies = [
        dependencies[i].union(*(dependencies[j] for j in neighbors[i]))
        for i in range(4)
    ]
    history.append(features)
    dependency_history.append(dependencies)

assert neighbors == {0: {1}, 1: {0, 2}, 2: {1, 3}, 3: {2}}
assert history == [[1, 2, 4, 8], [3, 7, 14, 12], [10, 24, 33, 26]]
assert dependency_history[1][0] == {0, 1}
assert dependency_history[2][0] == {0, 1, 2}

svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="700" viewBox="0 0 1040 700" role="img" aria-labelledby="title description">
<title id="title">Active rotation and graph message-passing dependencies</title>
<desc id="description">The upper panel rotates a two-atom configuration and a vector by positive 90 degrees around z with fixed Cartesian axes. The scalar stays seven, and the vector changes from (1,0,0) to (0,1,0). The lower panel uses a nonperiodic four-node chain with spacing one angstrom and edge cutoff 1.1 angstrom. Node zero depends on nodes zero and one after one step, and on nodes zero, one, and two after two steps. Original wiki schematic.</desc>
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M0 0 L10 5 L0 10 Z" fill="#222"/>
  </marker>
  <marker id="vector" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M0 0 L10 5 L0 10 Z" fill="#23658e"/>
  </marker>
  <style>
    text { font-family: Roboto, sans-serif; fill: #171c20; font-size: 20px; }
    .title { font-size: 24px; font-weight: 600; }
    .small { font-size: 18px; }
    .center { text-anchor: middle; }
    .blue { fill: #23658e; }
    .orange { fill: #985c12; }
    .axis { fill: none; stroke: #222; stroke-width: 1.5; marker-end: url(#arrow); }
    .bond { stroke: #222; stroke-width: 2; }
    .bracket { fill: none; stroke-width: 2.5; }
  </style>
</defs>
<rect width="1040" height="700" fill="#fff"/>
<rect x="20" y="20" width="1000" height="290" rx="6" fill="#fff" stroke="#222" stroke-width="1.5"/>
<text x="43" y="56" class="title">Active rotation by +90° about z</text>
<text x="995" y="56" class="small" text-anchor="end">Fixed Cartesian axes</text>

<path d="M125 215 H346 M125 215 V91" class="axis"/>
<text x="352" y="221">x</text>
<text x="119" y="86">y</text>
<line x1="125" y1="215" x2="205" y2="215" class="bond"/>
<circle cx="125" cy="215" r="10" fill="#fff" stroke="#222" stroke-width="2"/>
<circle cx="205" cy="215" r="10" fill="#e7f0f7" stroke="#222" stroke-width="2"/>
<path d="M205 215 H260" fill="none" stroke="#23658e" stroke-width="3.5" marker-end="url(#vector)"/>
<text x="254" y="195" class="blue center">v = (1, 0, 0)</text>
<text x="225" y="282" class="center">s = 7</text>

<path d="M406 167 H565" fill="none" stroke="#222" stroke-width="2" marker-end="url(#arrow)"/>
<text x="485" y="145" class="center">R</text>

<path d="M705 215 H938 M705 215 V91" class="axis"/>
<text x="944" y="221">x</text>
<text x="681" y="96">y</text>
<line x1="705" y1="215" x2="705" y2="135" class="bond"/>
<circle cx="705" cy="215" r="10" fill="#fff" stroke="#222" stroke-width="2"/>
<circle cx="705" cy="135" r="10" fill="#e7f0f7" stroke="#222" stroke-width="2"/>
<path d="M705 135 V80" fill="none" stroke="#23658e" stroke-width="3.5" marker-end="url(#vector)"/>
<text x="740" y="114" class="blue">v′ = (0, 1, 0)</text>
<text x="805" y="282" class="center">s′ = 7</text>

<rect x="20" y="330" width="1000" height="350" rx="6" fill="#fff" stroke="#222" stroke-width="1.5"/>
<text x="43" y="369" class="title">Edge cutoff and message-passing steps</text>
<text x="995" y="369" class="small" text-anchor="end">r<tspan baseline-shift="sub" font-size="13">c</tspan> = 1.1 Å</text>

<line x1="100" y1="458" x2="280" y2="458" class="bond"/>
<line x1="280" y1="458" x2="460" y2="458" class="bond"/>
<line x1="460" y1="458" x2="640" y2="458" class="bond"/>
<text x="190" y="433" class="center small">1 Å</text>
<text x="370" y="433" class="center small">1 Å</text>
<text x="550" y="433" class="center small">1 Å</text>

<circle cx="100" cy="458" r="22" fill="#23658e" stroke="#222" stroke-width="1.5"/>
<circle cx="280" cy="458" r="22" fill="#e7f0f7" stroke="#222" stroke-width="1.5"/>
<circle cx="460" cy="458" r="22" fill="#faedda" stroke="#222" stroke-width="1.5"/>
<circle cx="640" cy="458" r="22" fill="#eee" stroke="#222" stroke-width="1.5"/>
<text x="100" y="465" class="center" style="fill:#fff">0</text>
<text x="280" y="465" class="center">1</text>
<text x="460" y="465" class="center">2</text>
<text x="640" y="465" class="center">3</text>
<text x="100" y="514" class="center small">x = 0 Å</text>
<text x="280" y="514" class="center small">1 Å</text>
<text x="460" y="514" class="center small">2 Å</text>
<text x="640" y="514" class="center small">3 Å</text>

<path d="M78 546 V558 H302 V546" class="bracket" stroke="#23658e"/>
<text x="190" y="587" class="center blue">1 step · nodes 0, 1</text>
<path d="M78 610 V622 H482 V610" class="bracket" stroke="#985c12"/>
<text x="280" y="652" class="center orange">2 steps · nodes 0, 1, 2</text>

<text x="735" y="448" class="small">Initial h = (1, 2, 4, 8)</text>
<text x="735" y="498" class="blue">h₀⁽¹⁾ = 1 + 2 = 3</text>
<text x="735" y="548" class="orange">h₀⁽²⁾ = 3 + 7 = 10</text>
<text x="735" y="597" class="small">Local sum + self update</text>
<text x="735" y="627" class="small">Nonperiodic chain</text>
</svg>
'''

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(svg, encoding="utf-8")
print(OUTPUT)
