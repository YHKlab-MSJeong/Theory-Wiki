---
description: DeePTB-NEGF와 HamGNN-NEGF가 작은 DFT 자료에서 긴 채널의 수송 행렬을 만드는 방식과 검증 범위를 비교한다.
---

# 학습 Hamiltonian 기반 장채널 수송

작은 원자구조에서 DFT 전자구조를 학습하고, 긴 구조의 각 국소 환경에 모델을 적용해 Hamiltonian을 예측한 뒤 NEGF로 수송을 계산하는 방법이 보고되어 있다. 이 방식은 대표 Hamiltonian 블록을 그대로 반복하는 것과 다르다. 새 구조의 각 국소 환경에 따라 행렬 요소를 다시 예측한다. 그렇다고 예측 행렬이 DFT 자기일관 계산과 동등하거나 학습 범위 밖에서도 정확하다는 뜻은 아니다. [1, §§II–III; 2, Abstract, Introduction, Results, and Discussion]

DeePTB-NEGF 논문의 Figure 1은 [출판사 논문 페이지](https://www.nature.com/articles/s41524-025-01853-6)에서 확인할 수 있다. [1, Fig. 1]

## 1. 학습 모델이 Hamiltonian을 만드는 두 방식

| 접근 | 학습·예측 대상 | 긴 구조로의 확장 | 수송 자기일관성 |
|---|---|---|---|
| DeePTB-SK | 국소 환경에 따라 보정된 Slater–Koster 적분. CNT 장채널 예시에서는 DFT band energy를 학습표적으로 사용한다. | 각 원자쌍의 환경을 보고 hopping/onsite 모형을 평가해 행렬을 조립한다. | CNT-FET 예시는 DeePTB가 예측한 환경 의존 SK Hamiltonian과 NEGF–Poisson 반복을 사용한다. |
| DeePTB-E3 | LCAO 기저의 Kohn–Sham Hamiltonian·overlap 등 quantum operator를 E(3)-equivariant 네트워크로 예측한다. | DFT-NEGF로 구한 수렴 행렬을 학습자료로 사용한다. DeePTB-SK와 학습 표적 및 비용이 다른 경로다. | 적용 사례와 모델 버전의 범위에 따라 확인해야 한다. 두 DeePTB 경로를 한 모델로 섞어 설명하지 않는다. |
| HamGNN-NEGF | 작은 구조의 통상 DFT Hamiltonian을 학습한 E(3)-equivariant graph neural network가 큰 구조의 Hamiltonian을 예측한다. | 각 국소 원자 환경에서 행렬 블록을 예측한 뒤 DFT 전극 self-energy, 비직교 KPM, RGF를 연결한다. | 논문 방법은 수송 전하를 DFT-NEGF에 되먹임하는 완전 자기일관 계산이 아니다. |

DeePTB 논문은 환경 descriptor \(\mathcal D^{ij}\)에 따른 보정 \(\Phi\)를 넣어

\[
h^{\mathrm{env}}_{ll'\zeta}
=h_{ll'\zeta}(r_{ij})
\left[1+\Phi_{ll'\zeta}^{o_i,o_j}(r_{ij},\mathcal D^{ij})\right]
\]

형태의 SK 적분을 만든다. 반면 DeePTB-E3는 LCAO Hamiltonian과 overlap 행렬 등 연산자를 직접 예측한다. CNT를 180 nm까지 확장한 예는 DeePTB-SK 경로이며, 이를 DeePTB-E3로 설명하면 방법이 바뀐다. [1, §II.A, Eqs. (1)–(2), §III.2]

## 2. 두 대표 장채널 사례에서 보고한 것

### (1) DeePTB-NEGF

저자들은 zigzag CNT 밴드구조를 학습·검증하고 더 긴 원자 구조에 SK 모형을 적용했다. 180 nm CNT 계산은 약 3만 원자 규모의 **영바이어스 transmission** 사례다. 같은 논문의 게이트 CNT-FET 사례는 별도 계산으로, local-bottom-gate 구조에서 최대 41 nm, 7,820개 원자 규모의 NEGF–Poisson transfer characteristic을 제시한다. 따라서 “180 nm FET” 결과로 합쳐 쓰면 안 된다. [1, §III.2, Fig. 5 and Supplementary §S8]

이 FET 계산은 DeePTB가 예측한 환경 의존 SK Hamiltonian을 사용한다. Poisson 방정식에서 얻은 전위로 onsite Hamiltonian을 갱신하며, Mulliken 전하와 전위를 NEGF–Poisson 반복으로 맞춘다. 이는 매 반복에서 DFT Kohn–Sham 전자구조를 다시 수렴하는 full DFT-NEGF 계산과는 다르다. [1, §§II.A, III.C–III.D, Eqs. (1), (7)–(8), Fig. 5]

### (2) HamGNN-NEGF

2026년 arXiv 원고는 작은 주기 구조의 ground-state DFT Hamiltonian으로 모델을 훈련하고 큰 장치의 \(H\)를 예측한다. 이후 DFT에서 얻은 전극 self-energy, 비직교 kernel polynomial method (KPM)의 Fermi 준위 탐색, recursive Green's function (RGF)을 연결한다. 저자들은 채널 길이에 대한 선형 스케일링이 **단면 크기와 계산 설정을 고정했을 때** 성립한다고 보고한다. 이 방법은 full DFT-NEGF training data나 매 transport iteration의 DFT 자기일관 계산을 요구하지 않는다고 설명한다. [2, Abstract, Introduction, and Results]

Pt–Si–Pt 사례에서 저자들은 \(1\times1\times2\), \(1\times1\times3\), \(1\times1\times4\) Si supercell 자료로 학습하고 더 긴 구조를 평가했다. zero-bias transmission의 보고된 평균 절대 오차는 \(2\times2\times5\)에서 1.71%, \(2\times2\times7\)에서 3.86%, \(2\times2\times10\)에서 6.25%였다. 이 값은 해당 자료 분할과 모델의 원문 보고값이지 독립 재현값이나 다른 물질의 오차 범위가 아니다. [2, Results, Fig. 3, Supplementary Fig. S4(b,c)]

저자들은 10,000개가 넘는 원자계도 계산했다. 1,000배를 넘는 속도 향상은 320–480 원자 크기에서 fully self-consistent DFT-NEGF와 비교해 보고한 값이다. 이 속도비를 10,000개 이상 계산에서 직접 측정한 비교값으로 해석하지 않는다. [2, Abstract, Results p. 6 and Supplementary Fig. S8]

## 3. 적용 범위와 확인할 한계

- **모델에 없는 전기정역학:** DeePTB의 게이트 FET 예시처럼 Poisson 되먹임을 명시한 계산은 전위 변화를 반영한다. 일반적인 Hamiltonian 예측 모델이나 HamGNN의 비자기일관 수송 계산이 자동으로 gate-induced charge redistribution을 처리하는 것은 아니다. [1, §III.2; 2, Introduction]
- **유한 바이어스:** HamGNN 논문은 영바이어스 Hamiltonian 근사를 약한 비선형 구간에 한정하며, 강한 비선형성이나 음의 미분저항 같은 현상은 이 근사로 다루지 않는다. 강한 비선형성이나 공명 이동이 중요하면 별도 검증이 필요하다. [2, Discussion pp. 8–9, Method p. 12 and Supplementary §VIII, Figs. S16–S28]
- **학습 범위 밖의 환경:** 결함·도핑·strain·접촉 화학이 학습자료와 다르면 Hamiltonian 예측과 transmission을 다시 검증해야 한다. 높은 matrix-element 점수만으로 수송 오차를 대신하지 않는다. [1, §§II–III; 2, Results and Method]
- **수송 물리의 생략:** DeePTB 논문의 CNT 장채널 예시는 탄성 ballistic 수송 범위다. 저자들은 산란 효과를 향후 포함할 항목으로 둔다. 전자–포논 또는 결함 산란이 중요한 소자에 그 결과를 그대로 일반화하지 않는다. [1, §III.2 and Discussion]
- **행렬 정합:** 비직교 기저의 수송에는 \(H\)뿐 아니라 overlap \(S\)도 필요하므로 전극과 소자의 기저 순서·에너지 기준·전위 정합을 확인한다. HamGNN 논문은 큰 장치의 \(H\) 예측과 비직교 수송 계산을 설명하지만, 장치 overlap \(S\)의 구성 경로는 본문에서 충분히 구체화하지 않는다. 실제 구현을 재현할 때 이 부분을 확인한다. [1, §II; 2, Results and Method; 3, “TBT.Elec.<>.HS”]

실무적으로는 짧은 DFT-NEGF 기준계에서 band와 transmission을 먼저 비교하고, 그 뒤 길이·결함·게이트 조건을 하나씩 바꾸어 모델의 적용 범위를 확인한다. 문헌의 큰 원자 수 결과는 알고리즘 규모를 보여주는 사례이지 모든 계산 조건에서 같은 정확도를 보장하지 않는다.

HamGNN-NEGF의 학습 자료, 비직교 KPM의 Fermi 준위 탐색, RGF 복잡도, 유한 바이어스 근사와 benchmark 오차는 [HamGNN-NEGF 독립 문서](hamgnn-negf.md)에서 자세히 다룬다.

## 4. 참고 자료

1. J. Zou et al., “Deep learning accelerated quantum transport simulations in nanoelectronics: from break junctions to field-effect transistors,” *npj Computational Materials* **11**, 375 (2025), [§§II–III, Figs. 1, 2, 5](https://doi.org/10.1038/s41524-025-01853-6).
2. B. Liu et al., “Linear-Scaling Quantum Transport from Machine-Learning Density Functional Theory Hamiltonians,” arXiv:2609.37058v1 (2026), [Abstract, Introduction, Results, and Discussion; Figs. 1–4](https://arxiv.org/pdf/2609.37058v1).
3. SIESTA developers, [TBtrans User Guide](https://docs.siesta-project.org/projects/siesta/en/5.4/reference/tbtrans.html), “TBT.Elec.<>.HS” and “Principal layer interactions.”
