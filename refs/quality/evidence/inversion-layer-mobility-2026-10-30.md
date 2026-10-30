# Inversion-layer mobility 검증 기록

대상: `docs/device-physics/mobility/inversion-layer-mobility.md`  
대상 SHA-256: `2602c765dcc8745ffce2086313e563198d5d823523531de0ba3243b6087ac7b6`

범위는 low-field, diffusive channel에서의 \(\mu_{\mathrm{eff}}=\sigma_s/(qn_s)\) 정의와 charge·series-resistance를 명시한 추출식이다. short-channel 또는 high-field mobility의 보편 추출법은 검토하지 않았다.

| 주장 | 대조 근거 | 판정 |
| --- | --- | --- |
| sheet conductivity 기반 유효 이동도와 linear-region 추출식 | Lundstrom–Sun §2–3 식 (4), (13)–(16); Yeh–Guo §III 식 (16)–(22) | supported |
| \(Q_{\mathrm{inv}}\)와 내부 \(V_{DS}\) 정의·series-resistance convention을 함께 기록해야 함 | Yeh–Guo §III; Lundstrom–Sun §2–3 | supported |

독립 검토자 `wiki_rules`가 초안에서 split-CV의 배타적 표현과 직접 근거 없는 세부 원인을 지적했다. 작성자는 이를 특정 추출식의 정의 일치 요구로 축소했고, 최종 변경에서 새 식·가정 오류가 없다는 검토를 받았다. humanizer 점검에서는 수식·조건·인용을 바꾸지 않고 과장·반복만 제거했다. 그림·수치 예제는 없다.

1. M. Lundstrom, X. Sun, *Some Useful Relations for Analyzing Nanoscale MOSFETs Operating in the Linear Region* (2016), §2–3, §6, https://arxiv.org/pdf/1603.03132.
2. K.-L. Yeh, J.-C. Guo, *A New Method for Layout-Dependent Parasitic Capacitance Analysis and Effective Mobility Extraction in Nanoscale Multifinger MOSFETs* (2011), §III, https://ir.lib.nycu.edu.tw/server/api/core/bitstreams/a0ea6421-70c5-4a1b-a274-35599989b584/content.
