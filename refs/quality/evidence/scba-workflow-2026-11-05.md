# SCBA 고정점 흐름도 검증 기록

대상: docs/computational-materials-science/quantum-transport/scba-convergence.md
대상 SHA-256: 8279202afd0c89a08125c565e9a2354fb7c9037c6030e53bc02a4647082d27ca
기준 문서 SHA-256: 6a194a73c50ecd4b9abf8548b28d7f6d5e43c6af4f33db5d5d32f8e82b889021
이전 검증 기록: refs/quality/evidence/scba-convergence-2026-10-30.md
이전 기록 SHA-256: fd3efd70bfaaee033d8665c3612f5c5c699d1b7a55ef3a44b463b31965508d81

## 변경 범위와 판정

SCBA 도식과 함께 “Born” 및 “self-consistent”의 뜻을 첫 절에서 분리해 설명하고, bath·상호작용·diagram 선택은 별도 산란 모형에 달렸음을 명시했다. 혼합 전 fixed-point residual은 수렴 후보 또는 다음 혼합 반복을 고르는 것으로 한정했다. 후보 표시 뒤에도 전류, grid/window 안정성, 인과성, 결합된 경우의 Poisson residual 검사가 별도로 남는다는 본문 설명은 유지했다.

| 검토 주장 | 원문 위치 | 판정 |
|---|---|---|
| SCBA scattering self-energy는 현재 Green 함수에서 계산하고 Dyson–Keldysh 방정식을 반복해 푼다. | Bescond et al. §II 식 (1)–(2); Mera et al. §I–II, §V.1–2 | supported |
| “Born”은 선택한 상호작용의 섭동 self-energy 근사를, “self-consistent”는 갱신 Green function에 대한 self-energy 재계산을 뜻하며 상호작용·bath·diagram 선택은 별도 모형이다. | Lee–Sanvito 초록; Mera et al. §I–II; Bescond et al. §II 식 (1)–(2) | supported |
| 혼합 전 fixed-point residual은 작은 update와 구분되며, 잔차 기준 통과는 검증 후보이지 전체 검사 완료가 아니다. | Lee–Sanvito §III.B 식 (41), (44); Bescond et al. §II | supported |
| current mismatch, grid/window 안정성, causality 및 결합된 electrostatics는 서로 별도 검사다. | Lee–Sanvito §II.B, §V; Mera et al. §V.2; Bescond et al. §II | supported |

## 그림 재현 및 무결성

- HTML source: refs/quality/figure-source/scba-fixed-point.html
- HTML source SHA-256: 539643e8bff107129381cfbf42ed7a320a493f25f79b596f419c44c2b204acb4
- SVG: docs/assets/scba-fixed-point.svg
- SVG SHA-256: b9b63a2c647e08f820d3fd710dd4520c0df36eb6c62b400595a044d8b09a9285
- diagram-design self-check와 SVG export가 통과했다. Inkscape 미리보기에서 yes/no 분기, update loop, 별도 diagnostic label과 캔버스 잘림을 확인했다.
- 최종 독립 검토자: diagram_final_review (SCBA 도식과 본문, 2026-11-05). 수렴 후보와 별도 검사 구분에 차단 사항 없음.

## 참고 자료

1. M. Bescond et al., “One-shot Current Conserving Approach of Phonon Scattering Treatment in Nano-transistors” (2013), §II, https://in4.iue.tuwien.ac.at/pdfs/sispad2013/21-3.pdf.
2. W. Lee and S. Sanvito, “Exploring the limits of the self consistent Born approximation for inelastic electronic transport” (2008), abstract, §II.B, §III.B, §V, https://arxiv.org/pdf/0804.3389.
3. H. Mera, T. G. Pedersen, and B. K. Nikolić, “Hypergeometric resummation of self-consistent sunset diagrams for electron-boson quantum many-body systems out of equilibrium” (2016), §I–II, §V, https://arxiv.org/html/1512.06846.
