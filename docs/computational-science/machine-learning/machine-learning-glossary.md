---
description: 원자계 머신러닝과 학습 Hamiltonian 논문을 읽을 때 반복해서 등장하는 핵심 용어를 구분한다.
---

# 머신러닝 핵심 용어: 원자계 모델과 물리 계산

> 상태: 확인 중 — 지표별 추가 출처 검토 및 독립 검토 미완료. 게시 전 검증 필요.

## 1. 모델과 자료

| 용어 | 의미 | 원자계 계산에서 확인할 점 |
|---|---|---|
| **Feature / descriptor** | 모델 입력을 표현하는 수치 특징 | 원자 종류, 거리, 방향, 이웃 정보가 무엇인지 |
| **Embedding / latent representation** | 입력을 학습용 내부 공간으로 나타낸 표현 | 단순 scalar인지, 회전 시 변하는 equivariant feature인지 |
| **Target / label** | 학습에서 맞추려는 정답 자료 | 에너지, 힘, Hamiltonian 행렬 등 대상과 단위 |
| **Training / validation / test set** | 매개변수 학습 / 모델 선택 / 최종 평가 자료 | 같은 구조의 유사 프레임이 서로 다른 분할에 새는지 |
| **Generalization** | 훈련에 사용하지 않은 자료에서의 성능 | 새로운 조성·결함·strain·크기에 대해서도 시험했는지 |
| **Transferability** | 다른 조건·시스템으로 적용했을 때의 유효성 | 논문에서 실제로 시험한 전이 범위가 어디까지인지 |
| **Overfitting** | 훈련 자료의 특징에 지나치게 맞춰 다른 자료에서 성능이 떨어지는 현상 | train과 validation/test 오차 차이 |
| **Inductive bias** | 모델 구조가 미리 도입한 가정 | 국소성, 대칭성, cutoff, 기저 선택 |

이들은 논문마다 구체적인 측정 및 실험 분할 정의를 확인해야 하는 개념이다. 특히 구조가 상관된 원자계 데이터에서는 무작위 샘플 분할만으로 새로운 물질에 대한 일반화 성능을 보장하지 않는다.

## 2. Fidelity는 무엇인가

**Fidelity**는 문맥에 따라 '기준 계산·측정·현상을 얼마나 충실히 재현하는가'라는 뜻이거나 **multi-fidelity modeling**에서 계산비용과 근사 수준이 다른 데이터 출처의 등급을 뜻한다. 따라서 “high fidelity”가 항상 정확도가 더 높다는 실측 결과인 것은 아니다.

- **Low-fidelity model/data:** 일반적으로 비용이 낮지만 단순화되거나 정확도에 제한이 있는 계산·측정.
- **High-fidelity model/data:** 일반적으로 비용이 높고 연구의 목표 기준에 더 가깝다고 간주하는 계산·측정.
- **Multi-fidelity learning:** 여러 수준의 자료를 결합하거나 고비용 자료의 예측을 보완하는 전략.
- **Electronic-structure fidelity:** 예를 들어 ML Hamiltonian이 참조 DFT Hamiltonian이나 band를 얼마나 재현하는지에 관한 서술. 데이터 수준 구분과는 다른 뜻이므로 어떤 observables와 기준을 썼는지 확인한다.

DFT는 비교 대상과 목표에 따라 high-fidelity 참조가 될 수도 있지만, 실험의 완전한 정답과 동일하지 않다. 같은 ‘fidelity’라는 단어라도 기준 DFT, 더 높은 수준의 전자구조 계산, 실험 측정 중 무엇을 말하는지 명시해야 한다.

## 3. 오차와 손실 함수

기준값 \(y_i\), 예측값 \(\hat y_i\), 표본 수 \(N\)에 대해

\[
\mathrm{MAE}=\frac{1}{N}\sum_{i=1}^{N}|\hat y_i-y_i|,\qquad
\mathrm{RMSE}=\sqrt{\frac{1}{N}\sum_{i=1}^{N}(\hat y_i-y_i)^2}.
\]

MAE와 RMSE의 단위는 \(y\)와 같고, RMSE는 큰 잔차의 제곱에 더 민감하다. **Loss**는 학습 중 최적화하는 목적함수이고 **metric**은 성능 보고 지표이므로 동일하지 않을 수 있다. 행렬 원소 단위의 MAE와 band gap, transmission 등의 관측량 오차도 서로 다른 평가다.

## 4. 대칭성과 그래프 학습

| 용어 | 뜻 |
|---|---|
| **Invariant** | 입력을 변환해도 출력이 변하지 않음. 예: 방향을 바꾸어도 같은 에너지 |
| **Equivariant** | 입력 변환에 맞추어 출력이 정해진 법칙대로 변함. 예: 회전된 힘 벡터 |
| **GNN (Graph Neural Network)** | 노드와 에지의 관계를 이용해 정보를 계산하는 신경망 |
| **Message passing** | 이웃에서 노드 또는 에지로 정보를 전달·집계하는 갱신 방식 |
| **Receptive field** | 특정 출력에 영향을 줄 수 있는 입력의 범위 |
| **Cutoff radius** | 이웃 관계나 상호작용 범위를 정하는 거리 기준 |
| **Irrep** | 대칭 변환에서 더 작게 분해되지 않는 표현 |
| **Tensor product** | 여러 표현의 정보를 대칭 변환 법칙을 유지하면서 결합하는 연산 |

관련 설명: [e3nn](e3nn.md), [LEM/SLEM](lem-slem.md).

## 5. 학습·배포 결과 해석

**Data efficiency**는 원하는 성능을 얻는 데 필요한 학습자료의 양과 관련된다. 모델 사이 비교 시 같은 데이터 분할과 성능 기준을 쓰는지 확인한다. **Inference**는 학습된 모델로 예측하는 단계이며, 추론 속도와 학습 비용은 별개이다. **Out-of-distribution (OOD)**은 학습 및 통상 평가 분포와 다른 입력·조건을 뜻하고, 단순히 이전에 보지 않은 표본과는 구별해야 한다.

논문에서 “DFT-level fidelity”라고 할 때는 구체적으로 무엇을 비교했는지(행렬, 밴드, 힘, 수송), 어느 구조를 시험했는지, 기준이 무엇인지를 먼저 확인한다. 지표 이름보다 **표적·단위·자료 분할·기준 계산·평가 범위**가 중요하다.

## 6. 참고 자료

1. e3nn 개발팀, [공식 문서](https://docs.e3nn.org/en/latest/), “What is e3nn?” 및 “Irreps”.
2. e3nn 개발팀, [Equivariance Testing](https://docs.e3nn.org/en/latest/guide/equivar_testing.html), equivariance error의 정의와 수치 검사.
3. DeePTB 개발팀, [E3TB advanced input](https://github.com/deepmodeling/DeePTB/blob/main/docs/advanced/e3tb/advanced_input.md), 모델 옵션, loss 설정과 embedding 정의.
4. J. Zou et al., [학습 Hamiltonian과 수송 계산](https://doi.org/10.1038/s41524-025-01853-6) (2025), 학습 표적과 관측량 기반 검증 사례.

> 편집 메모: fidelity의 multi-fidelity 정의, 자료 분할·OOD 및 오차 지표에 대해서는 별도 독립 원문 대조를 완료한 다음에만 게시한다.
