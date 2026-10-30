---
description: 전하·중성 결함의 수송 산란 모형과 적용 범위를 정리한다.
---

# Defect scattering model

## 1. defect라는 말만으로는 모형이 정해지지 않는다

수송에서 defect model은 보통 \(H=H_0+\sum_jV_j\)의 disorder potential \(V_j\)와 결함 ensemble을 지정한다. charged impurity, neutral vacancy, substitutional defect, trapped charge는 같은 defect density라는 말로 묶을 수 없다. 전하 상태, 위치·분포, dielectric environment, carrier density와 screening이 달라지면 같은 구조 결함도 다른 scattering potential을 만든다. [Hwang–Das Sarma, pp. 1–2, 식 (1)–(3)](https://arxiv.org/pdf/cond-mat/0608645), [Kaasbjerg–Low–Jauho, §II.A–B](https://arxiv.org/pdf/1612.00469)

## 2. 약한 disorder의 수송률

독립 결함과 Born 근사에서는 Fermi golden rule로 단일-defect matrix element의 disorder average와 final-state sum을 사용해 transition 및 momentum-relaxation rate를 만든다. 이때 결함 밀도를 포함하는 방식은 \(V_{kk'}\)의 finite-area 또는 single-defect normalization에 따라 달라지므로, \(n_d|V_{kk'}|^2\)만의 식을 context 없이 보편식으로 쓰면 단위와 계수를 잃는다. charged impurity의 경우 결함 plane과 channel 사이 거리와 screening function이 결과를 바꾸므로, carrier density를 모른 채 \(n_d\)만 조정하는 것은 물리적으로 불충분하다. [Hwang–Das Sarma, 식 (1)–(3)](https://arxiv.org/pdf/cond-mat/0608645), [Kaasbjerg–Low–Jauho, §II.B, 식 (10)–(13)](https://arxiv.org/pdf/1612.00469)

## 3. 재료별 defect model을 분리한다

주기적 DFT supercell의 한 vacancy는 ordered array의 전자 구조를 주며, 무작위 dilute defect ensemble의 mobility를 바로 주지 않는다. 수송 예측에는 결함 생성 에너지·전하 상태와 별도로, 실제 농도, spatial correlation, scattering matrix element, carrier distribution을 연결해야 한다. Si(111) surface charged-impurity 모형과 MoS\(_2\) vacancy 모형은 위 일반 관계는 공유하지만 parameter를 서로 이전할 수 없다. [Hwang–Das Sarma](https://arxiv.org/pdf/cond-mat/0608645), [Kaasbjerg–Low–Jauho](https://arxiv.org/pdf/1612.00469)

## 4. 참고 문헌

1. E. H. Hwang, S. Das Sarma, *Transport properties of two-dimensional electron systems on silicon (111) surfaces* (2006), pp. 1–2, https://arxiv.org/pdf/cond-mat/0608645.
2. K. Kaasbjerg, T. Low, A.-P. Jauho, *Electron and hole transport in disordered monolayer MoS2: atomic vacancy-induced short-range and Coulomb disorder scattering* (2016), §II, https://arxiv.org/pdf/1612.00469.
