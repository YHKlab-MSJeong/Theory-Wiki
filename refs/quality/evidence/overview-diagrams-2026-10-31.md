# 메인 개요 그림 검증 기록

## 범위

두 그림은 논문 그림을 재사용한 것이 아니라, 위키의 메인 이론 간 관계를 설명하기 위해 새로 만든 개념도다. 수치 결과나 특정 계산의 증거를 나타내지 않으며, SVG 원본은 `docs/assets/`에 저장한다.

## 그림별 확인

| 그림 | 확인한 관계 | 독립 근거 |
|---|---|---|
| `open-transport-overview.svg` | reservoir 점유, 전극 self-energy와 열린 경계, 중심 산란영역, transmission/current, NEGF·QTBM·Landauer의 역할 구분 | Brandbyge et al. §II, §V; Papior et al. §II, §IV.A |
| `mobility-overview.svg` | inversion-layer charge와 sheet conductivity로부터 유효 이동도를 정의하고, phonon·roughness·defect 산란을 결합하기 전에 rate-level 가정과 적용 범위를 확인 | Lundstrom–Sun §2–3, §6; Yeh–Guo §III; Wettstein Appendix A.1 |

## 재현·무결성

- diagram-design `self_check.py`와 SVG export를 각 HTML source에 대해 통과시켰다.
- `open-transport-overview.svg` SHA-256: `1056e10c8cd8be91663c463f424fd9b3130c30b540b8232741302c4fdd79d355`
- `mobility-overview.svg` SHA-256: `d3c83ee959d8d86e478155eaded95776bd209b0da80d2b85b0062acce1555e5d`

## 참고문헌

1. M. Brandbyge et al., *Physical Review B* **65**, 165401 (2002), https://arxiv.org/pdf/cond-mat/0110650.
2. N. Papior et al., *Computer Physics Communications* **212**, 8–24 (2017), https://arxiv.org/pdf/1607.04464.
3. M. Lundstrom, X. Sun, *Some Useful Relations for Analyzing Nanoscale MOSFETs Operating in the Linear Region* (2016), https://arxiv.org/pdf/1603.03132.
4. K.-L. Yeh, J.-C. Guo, *A New Method for Layout-Dependent Parasitic Capacitance Analysis and Effective Mobility Extraction in Nanoscale Multifinger MOSFETs* (2011), https://ir.lib.nycu.edu.tw/server/api/core/bitstreams/a0ea6421-70c5-4a1b-a274-35599989b584/content.
5. A. Wettstein, *Quantum Effects in MOS Devices* (2000), Appendix A.1, https://iis-people.ee.ethz.ch/~schenk/theses/wettstein.pdf.
