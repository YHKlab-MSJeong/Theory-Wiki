---
description: Takigawa, Kiyohara와 Kumagai의 2026년 PRX 물리 기반 이온 유전 텐서 ML 접근을 정리한다.
---

# Takigawa et al. 2026: factorized ML for ionic dielectric tensors

Takigawa, Kiyohara와 Kumagai는 이온 유전 텐서를 예측하기 위해 BEC와 포논 물성을 분리 예측한 뒤 물리식으로 결합하는 기계학습 접근을 제안했다. 논문은 2026년 *Physical Review X*에 발표됐다. [1, Abstract and publication record]

<figure markdown="span">

  ![논문의 Figure 2. (a) 결정 구조에서 EGNN이 Born 유효전하 텐서를, MLP가 force-constant matrix를 예측하고 두 결과로 이온 유전율을 계산하는 흐름. (b) DFPT와 EGNN이 계산한 Born 유효전하 텐서 고유값 비교.](images/takigawa-2026-prx-fig2.png)

  <figcaption markdown="1">
  **그림 1.** A. Takigawa, S. Kiyohara, Y. Kumagai, “Physics-Based Factorized Machine Learning for Predicting Ionic Dielectric Tensors,” *Physical Review X* 16, 021006 (2026), Fig. 2, [DOI](https://doi.org/10.1103/28wr-w896). 논문은 CC BY 4.0으로 공개됐고 APS는 일부 그림에 제3자 권리 예외가 있을 수 있다고 안내한다. Fig. 2 캡션에는 별도 권리자 표기가 없다. 원문 PDF에서 페이지 여백과 논문 캡션을 덜어 내고 도판 영역을 수록했으며 데이터·표식·색상은 수정하지 않았다.
  </figcaption>
</figure>


## 1. 연구 질문과 기존 접근의 어려움

High-\(\kappa\) 후보를 찾을 때는 정적 유전율과 밴드갭을 함께 본다. 정적 유전율은 전자 응답과 원자의 변위가 만드는 이온 응답의 합이다. 산화물에서는 이온 기여가 클 수 있는데, 이를 구조에서 직접 예측하는 모델은 특정 진동 모드와 원자별 전하 응답을 동시에 학습해야 한다. 저자들은 이 두 물리량을 나누어 예측한 뒤 알려진 물리식으로 합치면 예측이 개선되는지 질문했다. [1, Introduction and §II.A; 2, §VIII]

관련 개념은 [유전 텐서와 전자·이온 응답](dielectric-response.md), [Born 유효전하](born-effective-charge.md), [DFPT 유전 응답](dfpt-dielectric-response.md), [high-κ 후보 선별](high-k-screening.md)에서 먼저 볼 수 있다.

## 2. 이온 유전율을 계산하는 경로

### (1) Born 전하와 격자 진동

[Born 유효전하](born-effective-charge.md)는 원자 변위에 따른 거시 분극의 변화율이다. 이온 유전 응답은 이 전하 텐서와 힘상수 행렬로 결정된다. 힘상수는 원자를 조금 움직였을 때 힘이 어떻게 바뀌는지를 나타내고, 동역학 행렬과 포논 모드로 연결된다. 힘상수와 동역학 행렬의 관계는 [전자–포논 결합 문서](../electron-phonon-coupling/electron-phonon-coupling.md)에도 설명돼 있다. [1, §II.A, §IV.A–B; 2, §VIII]

논문의 정적 조화 근사에서 한 극성 진동 모드의 유전 응답 기여는 해당 모드의 유효전하 크기의 제곱에 비례하고 주파수 제곱에 반비례한다. 따라서 원자 변위가 큰 분극을 만들거나 모드 주파수가 낮으면 그 모드의 기여가 커질 수 있다. 낮은 주파수의 예측 오차는 유전율에 크게 반영될 수 있으므로, 강한 응답을 보이는 후보에서 특히 주의해야 한다. 이 관계는 정규화와 단위 규약을 정한 조화 선형 응답에 적용된다. [1, §IV.B, Eq. (7); 2, §VIII]

### (2) Joint model의 두 입력

논문의 **joint model**은 결정 구조에서 두 항목을 별도로 구한다. 등변 그래프 신경망(E(3)-equivariant graph neural network, EGNN)은 각 원자의 Born 유효전하 텐서를 예측한다. 사전학습된 원자간 기계학습 퍼텐셜은 변위에 따른 힘을 계산하며, 저자들은 원자를 0.01 Å 변위시키는 유한차분으로 힘상수 행렬을 얻었다. 이후 두 결과를 유전 응답 식에 넣어 이온 유전 텐서를 계산한다. [1, §II.A, Fig. 2 and §IV.A]

그림 1의 왼쪽 패널은 이 두 경로가 식에서 합쳐지는 과정을, 오른쪽 패널은 EGNN의 Born 전하 예측과 [밀도범함수 섭동이론(DFPT)](dfpt-dielectric-response.md) 기준값을 비교한다. 등변성은 좌표계를 회전했을 때 텐서 출력도 그에 맞게 변하도록 모델을 구성하는 성질이다. 이 모델의 Born 전하와 포논은 서로 다른 경로에서 나온다. [1, §II.A and Fig. 2]

## 3. 학습 자료와 모델 성능

### (1) Born 전하와 포논을 따로 평가

EGNN의 자료는 45개 원소로 구성된 산화물 928개다. 논문은 Born 전하 텐서의 고유값에 대해 5-fold 교차 검증에서 평균 \(R^2=0.982\), RMSE 0.373을 보고했다. 이는 해당 자료와 분할에서 얻은 값으로, 모든 산화물의 오차를 보증하는 값은 아니다. 저자들은 음향 합 규칙을 EGNN에 명시적으로 강제하지 않았다고도 밝혔다. [1, §II.A, Fig. 2 and Appendix C]

저자들은 포논 성분의 영향을 살피기 위해 네 가지 사전학습 퍼텐셜을 비교했다. 이때 Born 전하는 DFPT 값으로 고정하고, 퍼텐셜마다 얻은 힘상수로 이온 유전율을 계산했다. 네 모델 모두 Γ점에서 안정하다고 판정한 산화물 786개에서 SevenNet-MF-ompa의 \(\log_{10}\) 이온 유전 텐서 고유값 \(R^2\)와 RMSE는 각각 0.968과 0.059로 보고됐다. 모델을 공정하게 비교하기 위한 이 부분집합은 아래 joint model 평가 집합과 크기가 다르다. [1, §II.A and Table I]

### (2) Direct model과 joint model의 비교

저자들은 SevenNet-MF-ompa가 Γ점에서 안정하다고 판정한 산화물 839개에 대해 이온 유전 텐서를 직접 예측하는 direct model과 joint model을 비교했다. 표의 값은 텐서 고유값에 \(\log_{10}\) 변환을 적용하고 5-fold 교차 검증으로 평가한 논문 보고치다. [1, §II.A and Fig. 3]

| 모델 | 예측 경로 | 평균 \(R^2\) | 평균 RMSE |
|---|---|---:|---:|
| Direct | 구조에서 이온 유전 텐서를 직접 예측 | 0.411 | 0.254 |
| Joint | Born 전하와 포논을 따로 구해 물리식으로 결합 | 0.911 | 0.099 |

저자들은 오차 원인을 살피기 위해 ML Born 전하에 DFPT 포논을 결합하는 경우와 DFPT Born 전하에 ML 포논을 결합하는 경우를 따로 계산했다. 높은 이온 유전 응답 구간에서는 포논 쪽 오차의 영향이 더 컸다. 두 오차가 부분적으로 상쇄될 수 있으므로 이 분해값을 단순히 더한 것이 전체 오차는 아니다. [1, §II.A and Table II]

## 4. High-κ 산화물 스크리닝

저자들은 Materials Project 자료 중 기존 유전율 자료가 없고 밴드갭이 있는 산화물에서 출발했다. 학습에 쓴 928개와 모델이 다루지 않는 원소를 포함한 구조를 제외하고, 금속 및 자성 산화물도 제외해 8,717개 후보를 구성했다. 따라서 최종 숫자는 전체 물질공간이 아닌 이 논문이 정한 후보 집합에 대한 것이다. [1, §II.B and Fig. 4]

| 단계 | 조건 | 남은 후보 |
|---|---|---:|
| Γ점 안정성 | SevenNet의 Γ점 네 번째 최저 주파수 \(f_4\ge 0.2\) THz | 4,654개 |
| 1차 물성 선별 | ML 정적 유전율과 r2SCAN 밴드갭의 곱 ≥ 200 | 142개 |
| 제일원리 확인 | PBEsol 기반 DFPT 유전율·Γ점 안정성 확인 및 수렴 실패 제외 | 121개 |
| 최종 선별 | DFPT 유전율과 유전율 의존 hybrid functional(DDH) 밴드갭의 곱 ≥ 350 | 31개 |

저자들은 Γ점에서 네 번째 최저 주파수가 0.2 THz보다 작으면 불안정으로 분류했다. 이는 논문의 구체적인 수치 선별 기준이다. [1, §II.A]

여기서 비교 지표는 구면 평균 정적 유전율 \(\varepsilon_{\mathrm{ave}}\)와 eV 단위 밴드갭 \(E_g\)의 곱이다. ML 단계의 기준 200과 최종 DFPT·DDH 기준 350은 서로 다른 방법으로 계산한 값이다. 최종 후보를 ML 예측만으로 확정했다고 읽으면 안 된다. [1, §II.B and Fig. 4]

## 5. 결과 해석과 한계

- **안정성의 범위:** 이 논문의 초기 안정성 조건은 Γ점 포논에 적용된다. 전 브릴루앙 영역의 동역학적 안정성이나 유한 온도에서의 상 안정성을 자동으로 보장하지 않는다. [1, §§II.A–B]
- **자료와 모델의 범위:** 45개 원소와 비자성 산화물이라는 후보 조건이 있다. 학습 구조와 화학 환경이 크게 다르면 예측 정확도를 따로 확인해야 한다. [1, §§II.A–B]
- **실험과 소자:** 저자들은 최종 31개 중 9개 산화물의 합성이 이미 보고됐고, 그중 4개에 실험 유전율 자료가 있다고 설명한다. 이는 나머지 후보 전부의 합성이나 박막·계면·누설 특성이 검증됐다는 뜻은 아니다. [1, §II.B and Table III]
- **관련 모델의 범위:** [SevenNet-Polar 문서](ml-born-effective-charge.md)는 Born 전하 출력에 초점을 둔다. 이 논문은 별도로 예측한 Born 전하와 포논을 결합해 이온 유전 텐서를 계산한다. [1, Abstract; 3, Abstract]

## 6. 참고 문헌

1. A. Takigawa, S. Kiyohara, and Y. Kumagai, “Physics-Based Factorized Machine Learning for Predicting Ionic Dielectric Tensors,” *Physical Review X* **16**, 021006 (2026), [논문 PDF](https://journals.aps.org/prx/pdf/10.1103/28wr-w896), https://doi.org/10.1103/28wr-w896.
2. X. Gonze and C. Lee, *Physical Review B* **55**, 10355 (1997), https://doi.org/10.1103/PhysRevB.55.10355.
3. A. Lu et al., “SevenNet-Polar…,” arXiv:2607.14827v3 (2026), https://arxiv.org/abs/2607.14827.
