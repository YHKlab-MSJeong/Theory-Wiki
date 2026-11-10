---
description: DeePTB-E3에서 쓰는 LEM과 SLEM의 국소성 가정, 등변 메시지 전달과 적용 범위를 구분한다.
---

# LEM과 SLEM: 국소 등변 메시지 전달

> 상태: 확인 중 — 독립 검토 미완료. 게시 전 검증 필요.

## 1. 용어와 문제 설정

**LEM (Localized Equivariant Message-Passing)**과 **SLEM (Strictly Localized Equivariant Message-Passing)**은 DeePTB-E3 계열에서 국소 원자 환경을 이용해 양자 연산자 행렬을 나타내기 위한 등변 그래프 신경망 방법이다. LEM의 이름은 모든 메시지 전달 신경망의 일반 명칭이 아니라 해당 연구·구현에서 사용한 모델 명칭이다. [1, Appendix G; 2, Advanced input]

원자 구조 \(X=\{(Z_i,\mathbf r_i)\}\)와 LCAO 기저로 표현한 Hamiltonian \(H_{i\alpha,j\beta}\)를 생각한다. 회전 시 방향에 의존하는 기저 성분과 행렬 블록은 정해진 표현에 따라 변환해야 한다. 등변 특징과 Clebsch–Gordan 결합을 이용하면 이 변환 성질을 반영하는 모델을 구성할 수 있다. 정확한 기저 순서, 궤도함수의 패리티, 에너지 기준은 실제 계산에서 따로 검증한다. [1, Main text and Appendix; 3, DeePTB-E3 discussion]

## 2. LEM과 SLEM의 핵심 차이

| 구분 | LEM | SLEM |
|---|---|---|
| 국소성 처리 | 거리에 따라 감소하는 학습 가능 의존성을 사용해 semi-local 정보를 허용 | 멀리 있는 이웃으로부터 전파되는 정보의 범위를 엄격하게 제한 |
| 의도 | 먼 원자와의 의존성이 필요한 구조를 더 유연하게 표현 | 강한 국소성 가정에서 전이성과 자료 효율을 추구 |
| 주의점 | 모델의 유효 의존 범위를 학습 설정과 자료로 검증 | 선택한 국소 범위 밖의 물리를 놓칠 가능성 검증 |

이 대비는 논문의 방법 설명과 공식 구현 가이드를 요약한 것이며, 어느 방법이 모든 물질에서 우수하다는 일반 결론은 아니다. 논문은 SLEM의 국소성 가정이 주기계에 잘 맞을 수 있으나 스크리닝이 약한 제한된 분자계에서는 충분하지 않을 수 있다고 논의한다. LEM에는 거리의존성을 학습 가능한 감쇠로 넣는다. [1, Appendix G; 2, Advanced input; 4, Bulk Silicon]

## 3. 연산자 예측과 메시지 전달

DeePTB-E3에서는 원자 종류, 상대 거리 및 방향에서 node/edge의 등변 표현을 구성하고, 메시지 전달을 반복한 뒤 Hamiltonian과 같은 연산자 블록을 복원한다. 방향 정보는 구면조화함수와 기약표현을 통해 전달하며, 블록을 다시 조립할 때 각운동량 결합 규칙을 사용한다. [3, Model Architecture; 5, Methods/Training settings]

이 접근을 단순히 원자당 스칼라 에너지를 예측하는 모델과 동일하게 취급하면 안 된다. 예측 표적은 구현 및 학습 설정에 따라 Hamiltonian, density 또는 overlap 연산자 블록일 수 있으며, downstream band/transport의 정확도는 추가 검증해야 한다. [3, More Method; 5, Training settings]

## 4. 실제 설정에서 볼 항목

DeePTB 공식 입력 문서에서 `model_options.embedding.method`는 `"lem"` 또는 `"slem"`을 지원한다. `r_max`, `irreps_hidden`, `n_layers`, cutoff, neighbor 설정을 학습자료 및 DFT 기저와 함께 기록한다. 설정의 숫자는 모델·원소·대상에 따라 달라지며 문서의 예제값을 무조건 재사용하지 않는다. [2, Advanced input; 4, Bulk Silicon]

검증에서는 회전 등변성뿐 아니라 구조별 Hamiltonian/overlap 오차, band 구조, 에너지 기준, 그리고 필요하다면 transmission까지 비교한다. 특히 전극·소자 정합이 필요한 NEGF에서는 operator 요소 오차만으로 수송 정확도를 판정하지 않는다. [5, Methods and Results; 6, 학습 Hamiltonian 기반 장채널 수송]

## 5. 한계와 연결

국소 cutoff와 학습된 감쇠는 장거리 정전기적 상호작용을 자동으로 정확히 처리한다는 뜻이 아니다. 결함, 표면, 비주기 구조, 장거리 분극이 있는 대상은 학습 분포 및 전기정역학 처리 방식을 따로 검토한다. 본 문서의 LEM·SLEM은 [e3nn과 등변 신경망](e3nn.md)의 일반적인 군 표현 원리를 활용하는 **특정 방법**이다.

## 6. 참고 자료

1. Z. Zhouyin et al., “Learning local equivariant representations for quantum operators,” [ICLR 2025 논문 원문](https://openreview.net/pdf?id=kpq3IIjUD3), Appendix G “LIMITATION” 및 관련 방법 절.
2. DeePTB 개발팀, [E3TB advanced input](https://github.com/deepmodeling/DeePTB/blob/main/docs/advanced/e3tb/advanced_input.md), “model_options”.
3. DeePTB 개발팀, [Tutorial 4: DeePTB-E3](https://deeptb.readthedocs.io/en/latest/quick_start/hands_on/tutorial4_E3_si.html), “More Method”, “Model Architecture”.
4. DeePTB 개발팀, [DeePTB-E3: Bulk Silicon](https://deeptb.readthedocs.io/en/latest/quick_start/hands_on/e3tb_hands_on.html), “model_options”.
5. J. Zou et al., [Deep learning accelerated quantum transport simulations in nanoelectronics](https://doi.org/10.1038/s41524-025-01853-6) (2025), “Training settings” 및 LEM/DeePTB-E3 기술.
6. 이 Wiki, [학습 Hamiltonian 기반 장채널 수송](../../computational-materials-science/quantum-transport/ml-hamiltonian-transport.md).
