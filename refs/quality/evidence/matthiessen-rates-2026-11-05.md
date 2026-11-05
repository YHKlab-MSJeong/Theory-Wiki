# matthiessens-rule 그림 추가 검증 기록

대상 문서: docs/device-physics/mobility/matthiessens-rule.md
대상 SHA-256: e0631d508f9f3a02fb0169599562329ec1e1854f971d6eca56402b32ef56ce00
기준 문서 SHA-256: 23fbfaf51452a963572f3f4f0a3ec58f93b93b7e2167d5d7ccd9af9934ee0463
이전 검증 기록: refs/quality/evidence/matthiessens-rule-2026-10-30.md
이전 검증 기록 SHA-256: c0a1afd4e1451417e93016aeba26a5e8e4d2d7347cbc186aad17c2511a44974f

## 범위와 주장

본문의 정의·수식·조건은 수정하지 않았다. 새 그림은 기존에 독립 검증된 문서 주장을 원본 도식으로 재구성했다. 그림에 별도 수치 사례나 새로운 계산 결과는 넣지 않았다.

| 그림에서 확인할 주장 | 직접 대조한 근거 | 판정 |
|---|---|---|
| fixed-energy independent scattering rates may be added in the stated approximation, while inverse energy-averaged effective mobilities require additional transport-weighting assumptions | Wettstein Appendix A.1, pp. 105–107; Lundstrom–Sun §6, (31) | supported |

## 그림 재현 및 검토

- HTML source: refs/quality/figure-source/matthiessen-rates.html
- HTML source SHA-256: 5f1ef53918f454d4c35925c3bffb8e7720d0a7e275723a320851a5f0112be32b
- SVG: docs/assets/matthiessen-rates.svg
- SVG SHA-256: 80afbfd99df77a72f3e255191225e7a9e30a0df59ba01f7c66063bc12ce480cb
- diagram-design 접근성 self-check와 SVG export를 통과했다. 원문에서 검토된 가정·부호·정규화만 나타내도록 확인했다.
- 대체 텍스트는 humanizer 점검 뒤 수식, 한계, 전문용어를 보존했다.
- 독립 최종 검토자: wiki_device_diagram_review (그림의 의미·문서 주장·원문 위치, 2026-11-05).

## 이전 근거

refs/quality/evidence/matthiessens-rule-2026-10-30.md는 그림 전 문서 내용의 검증 기록으로 유지한다. 이 기록은 새 도식의 의미와 재현 파일만 추가로 확인한다.
