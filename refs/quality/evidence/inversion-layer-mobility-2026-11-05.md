# inversion-layer-mobility 그림 추가 검증 기록

대상 문서: docs/device-physics/mobility/inversion-layer-mobility.md
대상 SHA-256: 3af4ae637eb2dd32dc0ec9da5e683d4e6d4cc540bc45ed70b0c8a8d5e942c62b
기준 문서 SHA-256: 2602c765dcc8745ffce2086313e563198d5d823523531de0ba3243b6087ac7b6
이전 검증 기록: refs/quality/evidence/inversion-layer-mobility-2026-10-30.md
이전 검증 기록 SHA-256: 32e9a9be4edea65f3a675edcc91e7c048207d3af9f1614db59958784ba491138

## 범위와 주장

본문의 정의·수식·조건은 수정하지 않았다. 새 그림은 기존에 독립 검증된 문서 주장을 원본 도식으로 재구성했다. 그림에 별도 수치 사례나 새로운 계산 결과는 넣지 않았다.

| 그림에서 확인할 주장 | 직접 대조한 근거 | 판정 |
|---|---|---|
| gate-induced inversion sheet conducts laterally and the low-field diffusive effective mobility is sheet conductivity divided by q times sheet carrier density | Lundstrom–Sun §2–3, (4), (13)–(16); Yeh–Guo §III, (16)–(22) | supported |

## 그림 재현 및 검토

- HTML source: refs/quality/figure-source/inversion-layer-mobility.html
- HTML source SHA-256: 60a27df0e90ed6f401e10e2315c0c9e4f18c4a62436311cd97679e24a6f644a8
- SVG: docs/assets/inversion-layer-mobility.svg
- SVG SHA-256: ba1228b23fc91dc7710ae5780f8ccc1b812aedc9d38d3b4018bb4164dbdddb74
- diagram-design 접근성 self-check와 SVG export를 통과했다. 원문에서 검토된 가정·부호·정규화만 나타내도록 확인했다.
- 대체 텍스트는 humanizer 점검 뒤 수식, 한계, 전문용어를 보존했다.
- 독립 최종 검토자: wiki_device_diagram_review (그림의 의미·문서 주장·원문 위치, 2026-11-05).

## 이전 근거

refs/quality/evidence/inversion-layer-mobility-2026-10-30.md는 그림 전 문서 내용의 검증 기록으로 유지한다. 이 기록은 새 도식의 의미와 재현 파일만 추가로 확인한다.
