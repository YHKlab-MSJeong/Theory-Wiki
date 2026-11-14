#!/usr/bin/env python3
"""Create the original vector schematic used in the CNN glossary.

Run this file with Python 3. It writes only cnn-receptive-field.svg in the
machine-learning images directory relative to this repository copy.

The model has two 3 x 3 convolutions, stride 1, dilation 1, and padding 0.
Reference for receptive-field definitions and the single-path recurrence:
https://distill.pub/2019/computing-receptive-fields/
No published artwork or measured data are reused.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = (
    ROOT
    / "docs/computational-science/machine-learning/images"
    / "cnn-receptive-field.svg"
)

# Enumerate spatial dependencies independently of the drawing coordinates.
first_layer = {
    (row, col): {
        (row + kernel_row, col + kernel_col)
        for kernel_row in range(3)
        for kernel_col in range(3)
    }
    for row in range(3)
    for col in range(3)
}
output_dependencies = set().union(*first_layer.values())
assert len(first_layer) == 9
assert output_dependencies == {(row, col) for row in range(5) for col in range(5)}
assert 1 + (3 - 1) + (3 - 1) == 5


def grid(x, y, count, fill):
    """Draw one square feature map using the same 44-pixel cell size."""
    size = count * 44
    elements = [
        f'<rect x="{x}" y="{y}" width="{size}" height="{size}" '
        f'fill="{fill}" stroke="#263541" stroke-width="1.5"/>'
    ]
    for index in range(1, count):
        offset = index * 44
        elements.extend(
            [
                f'<path d="M{x + offset} {y} V{y + size}" class="grid-line"/>',
                f'<path d="M{x} {y + offset} H{x + size}" class="grid-line"/>',
            ]
        )
    return "\n".join(elements)


svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1050" height="450" viewBox="0 0 1050 450" role="img" aria-labelledby="title description">
  <title id="title">CNN kernel windows and receptive field</title>
  <desc id="description">Two 3×3 convolutions with stride 1, dilation 1, and padding 0 map a 5×5 input to a 3×3 feature map and then to one output. The second convolution uses a 3×3 window on the preceding feature map. The output's theoretical receptive field covers the entire 5×5 original input. Original schematic, using the definitions in https://distill.pub/2019/computing-receptive-fields/.</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 Z" fill="#263541"/>
    </marker>
    <marker id="rf-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M0 0 L10 5 L0 10 Z" fill="#23658e"/>
    </marker>
    <style>
      text {{ font-family: 'DejaVu Sans', sans-serif; fill: #18232d; text-anchor: middle; }}
      .stage {{ font-size: 22px; font-weight: 600; }}
      .operation {{ font-size: 18px; }}
      .condition {{ font-size: 17px; fill: #4e5d68; }}
      .grid-line {{ fill: none; stroke: #8a9ba5; stroke-width: 1; }}
    </style>
  </defs>
  <rect width="1050" height="450" fill="#fff"/>

  <text x="525" y="34" class="condition">stride = 1 · dilation = 1 · padding = 0</text>
  <text x="180" y="91" class="stage">Input 5×5</text>
  <text x="561" y="91" class="stage">Feature map 3×3</text>
  <text x="907" y="91" class="stage">Output 1×1</text>

  <path d="M627 176 L885 220 L885 264 L627 308 Z" fill="#f8eee1"/>
  <path d="M627 176 L885 220 M627 308 L885 264" fill="none" stroke="#bc7827" stroke-width="1.6" stroke-dasharray="5 5"/>

  {grid(70, 132, 5, '#e7f0f7')}
  <rect x="70" y="132" width="220" height="220" fill="none" stroke="#23658e" stroke-width="3"/>
  {grid(495, 176, 3, '#faedda')}
  <rect x="490" y="171" width="142" height="142" fill="none" stroke="#a96617" stroke-width="2.5" stroke-dasharray="7 5"/>
  {grid(885, 220, 1, '#d8933b')}

  <text x="393" y="228" class="operation">3×3 convolution</text>
  <path d="M318 242 H465" fill="none" stroke="#263541" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="756" y="228" class="operation">3×3 convolution</text>
  <path d="M659 242 H852" fill="none" stroke="#263541" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="561" y="342" font-size="18" style="fill:#96590f">3×3 window</text>

  <circle cx="907" cy="274" r="3" fill="#23658e"/>
  <path d="M907 274 V391 H180 V359" fill="none" stroke="#23658e" stroke-width="2.5" marker-end="url(#rf-arrow)"/>
  <text x="543" y="425" font-size="21" font-weight="600" style="fill:#23658e">Receptive field 5×5</text>
</svg>
'''

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(svg, encoding="utf-8")
print(OUTPUT)
