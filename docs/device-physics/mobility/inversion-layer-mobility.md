---
description: MOSFET inversion layer에서 유효 이동도의 정의와 추출 범위를 정리한다.
---

# Inversion-layer mobility

## 1. 무엇을 이동도라고 부르는가

Inversion layer mobility는 gate 전계로 형성된 반전층의 횡방향 전도도를 전하 밀도로 나눈 유효 수송 계수다. 낮은 drain 전계, 국소 평형, 확산 수송이라는 기준 모형에서 sheet conductivity \(\sigma_s\)와 sheet electron density \(n_s\)에 대해

\[
\mu_{\mathrm{eff}}=\frac{\sigma_s}{q n_s}
\]

로 정의한다. 여기서 \(q>0\)이고 \(\sigma_s\)의 단위는 S, \(n_s\)는 m\(^{-2}\)이므로 \(\mu_{\mathrm{eff}}\)의 단위는 m\(^2\) V\(^{-1}\) s\(^{-1}\)이다. 이 정의는 channel의 전도도를 표현하는 것이며, ballistic 또는 quasi-ballistic 소자에서 얻는 apparent mobility와 자동으로 같지 않다. [Lundstrom–Sun, §2–3, 식 (4), (13)–(16)](https://arxiv.org/pdf/1603.03132), [Yeh–Guo, §III, 식 (16)–(22)](https://ir.lib.nycu.edu.tw/server/api/core/bitstreams/a0ea6421-70c5-4a1b-a274-35599989b584/content)

## 2. 선형영역 추출과 전하의 선택

접촉 밖의 channel 전압 \(V_{DS,\mathrm{int}}\)가 작고 \(Q_{\mathrm{inv}}=-q n_s\)를 독립적으로 알면,

\[
I_D \simeq \frac{W}{L}\mu_{\mathrm{eff}}\lvert Q_{\mathrm{inv}}\rvert V_{DS,\mathrm{int}}
\]

에서 \(\mu_{\mathrm{eff}}\)를 얻는다. \(W,L\)은 유효 channel 폭·길이이다. \(\lvert Q_{\mathrm{inv}}\rvert\)의 산출법과 \(V_{DS,\mathrm{int}}\)의 접촉 보정은 추출식의 정의와 일치해야 한다. split-CV는 \(Q_{\mathrm{inv}}\)를 직접 정하는 한 방법이며, contact/series resistance 보정은 그 저항 모형과 부호 convention을 함께 쓸 때 적용한다. [Yeh–Guo, §III, 식 (16)–(22)](https://ir.lib.nycu.edu.tw/server/api/core/bitstreams/a0ea6421-70c5-4a1b-a274-35599989b584/content), [Lundstrom–Sun, §2–3](https://arxiv.org/pdf/1603.03132)

## 3. 전계와 산란의 역할

\(\mu_{\mathrm{eff}}\) 하나는 특정 산란률을 직접 측정한 값이 아니다. 전계 의존성을 해석하려면 \(n_s\), 온도, vertical field, channel 방향, 접촉 보정과 사용하는 산란 모형을 함께 고정해야 한다. 여러 산란률을 한 mobility로 결합하는 근사의 조건은 [Matthiessen's rule](matthiessens-rule.md)에서 따로 다룬다. [Lundstrom–Sun, §2–3](https://arxiv.org/pdf/1603.03132), [Yeh–Guo, §III](https://ir.lib.nycu.edu.tw/server/api/core/bitstreams/a0ea6421-70c5-4a1b-a274-35599989b584/content)

## 4. 적용 한계와 보고 기준

이 문서의 식은 low-field, diffusive channel을 기준으로 정의한 effective quantity에 한정된다. 따라서 보고할 때는 \(Q_{\mathrm{inv}}\) 산출법, 적용한 series-resistance 보정, \(V_{DS,\mathrm{int}}\), 온도와 추출 구간을 함께 제시해야 한다. [Lundstrom–Sun, §2–3](https://arxiv.org/pdf/1603.03132), [Yeh–Guo, §III](https://ir.lib.nycu.edu.tw/server/api/core/bitstreams/a0ea6421-70c5-4a1b-a274-35599989b584/content)

## 5. 참고 문헌

1. M. Lundstrom, X. Sun, *Some Useful Relations for Analyzing Nanoscale MOSFETs Operating in the Linear Region* (2016), §2–3, §6, https://arxiv.org/pdf/1603.03132.
2. K.-L. Yeh, J.-C. Guo, *A New Method for Layout-Dependent Parasitic Capacitance Analysis and Effective Mobility Extraction in Nanoscale Multifinger MOSFETs* (2011), §III, https://ir.lib.nycu.edu.tw/server/api/core/bitstreams/a0ea6421-70c5-4a1b-a274-35599989b584/content.
