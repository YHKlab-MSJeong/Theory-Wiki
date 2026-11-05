# surface-roughness-scattering 그림 추가 검증 기록

대상 문서: docs/device-physics/mobility/surface-roughness-scattering.md
대상 SHA-256: 99bf846e6177c964a251de04f9827700335db754d041c584653c48dd28125cb2
기준 문서 SHA-256: 35380d50d6c935f2aaf907e8636ba427ffe25be2f5be017679273e16d4ba0675
이전 검증 기록: refs/quality/evidence/surface-roughness-scattering-2026-10-30.md
이전 검증 기록 SHA-256: 41d5db4adf56e8ad8a19e5fa7de386c3314e9d96e6b5b379ffd64443f5fb1a85

## 범위와 주장

본문의 정의·수식·조건은 수정하지 않았다. 새 그림은 기존에 독립 검증된 문서 주장을 원본 도식으로 재구성했다. 그림에 별도 수치 사례나 새로운 계산 결과는 넣지 않았다.

| 그림에서 확인할 주장 | 직접 대조한 근거 | 판정 |
|---|---|---|
| roughness correlation spectrum contributes to perturbation matrix elements and transition rates, but height and correlation length alone do not determine a universal mobility | Badami Ch. 2, §2.1–2.2.2, (2.1)–(2.2), (2.24)–(2.26); Sano §II.A, §II.C, (3)–(5), (11) | supported |

## 그림 재현 및 검토

- HTML source: refs/quality/figure-source/surface-roughness-scattering.html
- HTML source SHA-256: ed31ce2a49ddbf1b1e81dd5618c359c2315f944e9893beca3946061bbec6aa72
- SVG: docs/assets/surface-roughness-scattering.svg
- SVG SHA-256: f0667f494f871c5ca3e9060da06c7a9a767e32e71fb6c6dad3ba563690824b25
- diagram-design 접근성 self-check와 SVG export를 통과했다. 원문에서 검토된 가정·부호·정규화만 나타내도록 확인했다.
- 대체 텍스트는 humanizer 점검 뒤 수식, 한계, 전문용어를 보존했다.
- 독립 최종 검토자: wiki_device_diagram_review (그림의 의미·문서 주장·원문 위치, 2026-11-05).

## 이전 근거

refs/quality/evidence/surface-roughness-scattering-2026-10-30.md는 그림 전 문서 내용의 검증 기록으로 유지한다. 이 기록은 새 도식의 의미와 재현 파일만 추가로 확인한다.
