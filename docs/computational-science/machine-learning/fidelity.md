---
description: 머신러닝에서 fidelity가 가리키는 참조 대상과 다중 충실도·설명 충실도의 차이를 설명한다.
---

# Fidelity와 다중 충실도

**Fidelity(충실도)**는 데이터·모형·설명이 참조 대상의 특성이나 동작을 얼마나 충실하게 표현하는지를 나타내는 말이다. 과학 시뮬레이션에서는 모형과 데이터의 근사 수준, 설명 가능한 머신러닝에서는 원 모델의 예측을 재현하는 정도에 쓰인다. 논문을 읽을 때는 fidelity의 **참조 대상, 평가 범위, 측정 방법**을 함께 확인한다. 아래 정의는 각 문헌의 용례를 종합한 것이다. [1, Introduction; 2, §2; 3, §3 “Empirical Evaluation”]

<a id="fidelity-levels"></a>

## 1. High fidelity와 low fidelity

과학 머신러닝의 **high-fidelity model**은 해당 문제의 기준 역할을 하는 모형이고, **low-fidelity model**은 같은 관심 물리량을 더 적은 비용으로 근사하는 모형으로 구성되는 경우가 많다. 물리 근사, 공간·시간 해상도, 전자구조 계산 수준 등을 다르게 선택할 수 있다. 두 수준의 관계는 어떤 물리량과 입력 범위를 다루는지에 따라 달라진다. [1, Introduction and §2; 4, §§1–2]

**Multi-fidelity learning(다중 충실도 학습)**은 서로 다른 수준의 자료나 모형을 결합해 관심 대상의 예측을 개선하는 접근이다. 많은 저비용 자료에 소량의 고비용 자료를 결합하는 구성이 사용된다. 수준 사이의 관계를 활용하므로, 저충실도 결과가 어떤 입력 구간에서 유효하고 어떤 구간에서 잘못된 추세를 보이는지도 확인한다. [1, Abstract and §§2–3; 4, §§1–3]

재료 연구의 실제 예로 Chen 등은 많은 PBE 밴드갭 자료와 더 높은 수준의 전자구조 계산 및 실험 자료를 결합한 그래프 신경망을 제시했다. 이 논문에서 PBE 자료는 low-fidelity 자료로 사용되었다. 여기서 붙인 수준 이름은 해당 밴드갭 학습 문제와 자료 구성에 따른다. [5, Abstract and Results]

<a id="surrogate-model"></a>

### (1) Surrogate model

**Surrogate model(대리모형)**은 비용이 큰 계산 등의 입력–출력 관계를 근사하여 대신 평가하는 모형이다. 신경망이나 Gaussian process로 구성할 수 있다. 대리모형을 평가할 때는 기준 계산과의 차이뿐 아니라 입력 범위와 관심 출력도 함께 정한다. [1, §2(a); 4, §1.3; 5, Introduction and Results “Multi-fidelity Graph Networks”]

위키의 DeePTB 사례에서는 DFT 자료에서 학습한 모형으로 Hamiltonian을 구성한 뒤 수송을 계산한다. 이때 밴드, Hamiltonian 원소, transmission은 각각 비교할 수 있는 출력이다. 해당 논문의 학습 표적과 수송 검증은 관련 문서에서 살펴본다. [DeePTB와 NEGF 수송](../../computational-materials-science/quantum-transport/deeptb-negf.md)

<a id="explanation-fidelity"></a>

## 2. 설명의 fidelity

설명 가능한 인공지능(explainable artificial intelligence, XAI)에서 fidelity는 설명 모델 \(g\)가 설명 대상 모델 \(f\)의 동작을 재현하는 정도를 가리킨다. 분류 모델 추출의 한 지표는 다음과 같다. [2, §2; 3, §3 “Empirical Evaluation”]

\[
\operatorname{Fidelity}(g,f)
=\frac{1}{N}\sum_{i=1}^{N}\mathbf 1[g(x_i)=f(x_i)].
\]

\(x_i\)는 평가 입력, \(N\)은 입력 수, \(\mathbf 1\)은 조건이 참이면 1인 지시함수다. 비교 대상이 원 모델의 예측인 지표다. 정답 레이블을 \(y_i\)라 하면 분류 **accuracy(정확도)**는 \(N^{-1}\sum_i\mathbf1[g(x_i)=y_i]\)로 정의한다. Craven과 Shavlik은 추출한 결정트리를 평가할 때 이 두 비율을 구분했다. [3, §3 “Empirical Evaluation”]

### (1) 작은 예제

원 모델과 설명 모델이 다음처럼 예측했다고 가정한다. 아래 값은 정의를 보여 주기 위한 자체 예제다.

| 입력 | 정답 \(y\) | 원 모델 \(f\) | 설명 모델 \(g\) |
|---|---|---|---|
| \(x_1\) | 0 | 0 | 0 |
| \(x_2\) | 1 | 0 | 0 |
| \(x_3\) | 0 | 1 | 1 |
| \(x_4\) | 1 | 1 | 1 |

설명 모델은 원 모델의 예측 네 개를 모두 재현하므로 fidelity가 100%다. 정답 두 개를 맞혔으므로 accuracy는 50%다. 두 수치를 읽을 때는 각각의 비교 대상을 확인한다. [3의 정의를 적용한 자체 계산]

<a id="local-fidelity"></a>

### (2) Local fidelity

LIME(Local Interpretable Model-agnostic Explanations)은 특정 입력 \(x\) 주변에서 원 모델을 근사하는 설명 모델을 구한다. 논문은 근접도 가중치 \(\pi_x(z)\)로 주변 샘플 \(z\)에 가중치를 주는 local fidelity 손실을 사용한다. 설명용 표현을 \(z'\)라 하면 [2, §§3.1–3.2 and Eq. (2)]

\[
\mathcal L(f,g,\pi_x)
=\sum_{(z,z')\in\mathcal Z}\pi_x(z)\,[f(z)-g(z')]^2
\]

이다. \(\mathcal Z\)는 섭동 입력과 이에 대응하는 설명용 표현 \((z,z')\)의 샘플 집합이다. \(f(z)\)는 설명할 클래스의 예측 점수이고 \(g(z')\)는 해석 가능한 표현에서 얻은 근사값이다. 어느 입력 근처인지, 주변 입력을 어떻게 만들고 가중하는지가 평가 범위를 정한다. 넓은 평가 자료에서 일치 비율을 구하는 앞의 예와 함께 사용 맥락을 확인한다. [2, §§3.1–3.4; 3, §3 “Empirical Evaluation”]

## 3. 논문에서 확인할 항목

| 표현 | 확인할 내용 |
|---|---|
| High-fidelity data | 어떤 계산·측정을 기준 자료로 삼았는가 |
| High-fidelity prediction | 어떤 출력과 입력 구간에서 어떤 오차로 비교했는가 |
| Multi-fidelity | 어떤 수준들을 결합하고 수준 사이 관계를 어떻게 학습했는가 |
| Explanation fidelity | 어떤 원 모델의 동작을 어느 범위에서 재현하는가 |
| Accuracy | 분류 정답률을 말하는가, 분야의 일반적인 예측 정확성을 말하는가 |

이 표는 위 정의들을 논문 독해에 적용하기 위한 확인 항목이다. 검색할 관련 용어는 용어 찾아보기에도 모아 두었다. [머신러닝 용어 찾아보기](glossary.md)

## 4. 참고 자료

1. P. Perdikaris et al., “Nonlinear information fusion algorithms for data-efficient multi-fidelity modelling,” *Proc. R. Soc. A* **473**, 20160751 (2017). [원문](https://pmc.ncbi.nlm.nih.gov/articles/PMC5332612/)
2. M. T. Ribeiro, S. Singh, C. Guestrin, “Why Should I Trust You? Explaining the Predictions of Any Classifier,” *KDD* (2016), §§2–3. [원문](https://ucinlp.github.io/files/papers/lime-kdd16.pdf)
3. M. W. Craven, J. W. Shavlik, “Extracting Tree-Structured Representations of Trained Networks,” *NIPS 8* (1995), §3 “Empirical Evaluation”. [원문](https://proceedings.neurips.cc/paper_files/paper/1995/file/45f31d16b1058d586fc3be7207b58053-Paper.pdf)
4. B. Peherstorfer, K. Willcox, M. Gunzburger, “Survey of Multifidelity Methods in Uncertainty Propagation, Inference, and Optimization,” *SIAM Review* **60**, 550–591 (2018). [원문](https://arxiv.org/abs/1806.10761)
5. C. Chen et al., “Learning properties of ordered and disordered materials from multi-fidelity data,” *Nature Computational Science* **1**, 46–53 (2021). [논문](https://doi.org/10.1038/s43588-020-00002-x)
