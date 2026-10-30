---
description: 산란률과 이동도의 역수 가산이 성립하는 조건을 구분한다.
---

# Matthiessen's rule

## 1. 두 형태를 구별해야 한다

Matthiessen's rule은 독립 산란 메커니즘의 momentum-relaxation rate가 더해진다는 근사

\[
\frac{1}{\tau_{\mathrm{tot}}(E)}\simeq\sum_i\frac{1}{\tau_i(E)}
\]

를 가리킨다. 여기서 \(i\)는 phonon, charged impurity, roughness 같은 산란 채널이다. 이것은 independent-scatterer, relaxation-time approximation 및 같은 carrier 상태에서 rate를 정의할 수 있다는 조건의 명제다. 실험 또는 소자에서 얻는 유효 이동도에 대해 \(1/\mu\simeq\sum_i1/\mu_i\)를 쓰는 것은 위 식을 energy·subband·공간 분포에 대해 평균한 뒤에도 가산이 유지된다는 더 강한 가정이다. [Wettstein, Appendix A.1, pp. 105–107](https://iis-people.ee.ethz.ch/~schenk/theses/wettstein.pdf), [Lundstrom–Sun, §6, 식 (31)](https://arxiv.org/pdf/1603.03132)

## 2. 왜 이동도 역수는 일반적으로 더해지지 않는가

선형 응답 전도도는 상태 밀도, 속도, \(\tau_{\mathrm{tot}}(E)\), distribution의 energy weighting을 포함한 적분이다. 따라서 rate-level 가산을 energy-averaged mobility의 역수 가산으로 바꾸는 단계는 별도의 근사다. 이 문서는 그 근사가 성립한다고 가정하지 않으며, 사용한 수송 모형에서 total response와 직접 비교해야 한다. [Wettstein, Appendix A.1, pp. 105–107](https://iis-people.ee.ethz.ch/~schenk/theses/wettstein.pdf), [Lundstrom–Sun, §6](https://arxiv.org/pdf/1603.03132)

## 3. 사용할 때의 최소 검증

역수 가산을 사용한다면 각 \(\mu_i\)의 전하 밀도·온도·field·subband 정의를 일치시켜야 한다. 합산값이 전체 계산 또는 측정과 맞는지 확인하고, 맞지 않으면 scattering correlation, screening 변화, nonparabolicity, nonequilibrium distribution 중 무엇을 생략했는지 검토한다. 일치는 각 산란 모형이 유일하게 옳다는 증거가 아니며, 불일치는 어느 하나의 rate만 바꾸어 해결할 수 있다고 가정할 근거도 아니다.

## 4. 참고 문헌

1. A. Wettstein, *Quantum Effects in MOS Devices* (2000), Appendix A.1, pp. 105–107, https://iis-people.ee.ethz.ch/~schenk/theses/wettstein.pdf.
2. M. Lundstrom, X. Sun, *Some Useful Relations for Analyzing Nanoscale MOSFETs Operating in the Linear Region* (2016), §6, https://arxiv.org/pdf/1603.03132.
