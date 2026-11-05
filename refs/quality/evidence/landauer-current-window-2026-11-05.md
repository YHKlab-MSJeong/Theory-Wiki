# landauer-transmission 그림 추가 검증 기록

대상 문서: docs/computational-materials-science/quantum-transport/landauer-transmission.md
대상 SHA-256: f38b0c54f37641c61d0b63c904d443ccc5948068133f1316f03f7f962ecf313b
기준 문서 SHA-256: 6813c06ec99cb1753640a9c20f4bbb99eaad46d7ee8b205c83feab444d8bd2d0
이전 검증 기록: refs/quality/evidence/landauer-2026-10-28-transition.md
이전 검증 기록 SHA-256: d890b076dc0505e4b271da1de93cfac1ef114bc1a7caf9b963d078c8b0042732

## 범위와 주장

본문의 정의·수식·조건은 수정하지 않았다. 새 그림은 기존에 독립 검증된 문서 주장을 원본 도식으로 재구성했다. 그림에 별도 수치 사례나 새로운 계산 결과는 넣지 않았다.

| 그림에서 확인할 주장 | 직접 대조한 근거 | 판정 |
|---|---|---|
| reservoir occupation difference weights energy-dependent transmission in finite-bias current; linear-response and zero-temperature limits yield thermal weighting and Fermi-energy conductance | Bruneau et al. §1.1, (1.2), (1.6); Kohler et al. §2.4, (16)–(18) | supported |

## 그림 재현 및 검토

- HTML source: refs/quality/figure-source/landauer-current-window.html
- HTML source SHA-256: 2a83db9b347217a4d34ab1083d06c92533ee1f142aae90d0fc911d47a045f1f7
- SVG: docs/assets/landauer-current-window.svg
- SVG SHA-256: 964fa82b36e851e57a58af26c5c3c4f40f3302b2d446a5b8c5fbc5f8db026115
- diagram-design 접근성 self-check와 SVG export를 통과했다. 원문에서 검토된 가정·부호·정규화만 나타내도록 확인했다.
- 대체 텍스트는 humanizer 점검 뒤 수식, 한계, 전문용어를 보존했다.
- 독립 최종 검토자: wiki_transport_diagram_review (그림의 의미·문서 주장·원문 위치, 2026-11-05).

## 이전 근거

refs/quality/evidence/landauer-2026-10-28-transition.md는 그림 전 문서 내용의 검증 기록으로 유지한다. 이 기록은 새 도식의 의미와 재현 파일만 추가로 확인한다.
