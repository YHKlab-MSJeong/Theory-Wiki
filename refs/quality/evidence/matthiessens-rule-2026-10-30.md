# Matthiessen's rule 검증 기록

대상: `docs/device-physics/mobility/matthiessens-rule.md`  
대상 SHA-256: `23fbfaf51452a963572f3f4f0a3ec58f93b93b7e2167d5d7ccd9af9934ee0463`

범위는 independent-scatterer와 relaxation-time approximation 아래 rate 가산 및 mobility 역수 가산으로 넘어갈 때의 추가 근사다. 특정 재료의 multiband 오차 수치는 주장하지 않는다.

| 주장 | 대조 근거 | 판정 |
| --- | --- | --- |
| rate 가산과 energy-integrated response의 가산은 구별해야 함 | Wettstein Appendix A.1 pp. 105–107; Lundstrom–Sun §6 식 (31) | supported |
| apparent mobility의 역수 가산은 보편 법칙이 아니라 모형별 확인 대상 | Wettstein Appendix A.1; Lundstrom–Sun §6 Fig. 1 | supported |

독립 검토자 `wiki_rules`가 다중 subband 오류를 직접 입증하지 않는 인용을 지적했다. 작성자는 그 정량 주장을 삭제하고 위 범위로 한정했다. humanizer 점검은 과학적 의미를 바꾸지 않았다. 그림·수치 예제는 없다.

1. A. Wettstein, *Quantum Effects in MOS Devices* (2000), Appendix A.1, pp. 105–107, https://iis-people.ee.ethz.ch/~schenk/theses/wettstein.pdf.
2. M. Lundstrom, X. Sun, *Some Useful Relations for Analyzing Nanoscale MOSFETs Operating in the Linear Region* (2016), §6, https://arxiv.org/pdf/1603.03132.
