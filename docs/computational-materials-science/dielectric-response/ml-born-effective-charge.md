---
description: SevenNet-Polar가 예측하는 Born 유효전하와 그것이 유전율 계산에서 맡는 역할을 구분한다.
---

# Machine learning for Born effective charges: SevenNet-Polar

SevenNet-Polar는 에너지·힘·응력 예측을 확장해 Born 유효전하(BEC)도 예측하도록 만든 등변 그래프 신경망 프레임워크다. BEC 전용 모델과 에너지·힘·응력·BEC 다중과제 모델은 출력과 학습 자료 범위가 다르다. 2026년 7월 21일 갱신된 arXiv v3를 기준으로 한다. [1, Abstract and §2; 2, model and usage documentation]

## 1. 모델 출력과 유전 응답의 연결

BEC는 원자 변위에 따른 분극 응답을 나타낸다. SevenNet-Polar의 BEC 출력은 극성 격자 응답 계산의 중요한 입력이지만, BEC만으로 전체 유전 텐서가 정해지는 것은 아니다. 이온 유전율에는 포논 주파수와 고유벡터도 필요하고, 전자 기여 \(\varepsilon^\infty\)도 따로 포함된다. [1, Abstract; 3, §§V, VIII]

논문에서 예측하는 항목은 BEC와 에너지·힘·응력이다. BEC 전용 모델의 최저 보고 RMSE는 \(0.0043e\), 다중과제 모델의 BEC RMSE는 \(0.0029e\)이며, 각각 논문에 정의한 자료 분할과 시험 조건에 대한 원문 보고값이다. 독립 재현값이 아니며, 다른 데이터셋의 수치와 직접 비교하거나 유전율 텐서 예측 오차로 읽어서는 안 된다. [1, Abstract and §2–4]

논문은 유전율 텐서 자체나 포논 힘상수를 예측한다고 주장하지 않는다. 전체 유전율을 구하려면 예측 BEC를 포논 계산과 결합하고, 구조 및 적용 범위에 맞는 전자 응답을 별도로 다뤄야 한다. [1, Abstract and Methods; 3, §VIII]

## 2. 검증에서 확인할 것

모델 적용 전에는 학습 자료와 대상 구조의 화학 조성·배위·상태가 겹치는 범위, BEC 텐서 오차, 대칭성·전하 중성·acoustic sum rule, 구조 이완 후 물성의 일관성을 확인해야 한다. 시험 분할의 예측 정확도와 학습 분포가 달라지는 조건의 일반화는 서로 다른 검증 질문이다. 따라서 테스트 자료의 점수만으로 학습 범위 밖 구조의 외삽 신뢰성을 주장할 수는 없다. [1, Methods and Results; 5, Abstract]

실제 high-\(\kappa\) 후보 탐색에서는 모델의 계산 속도 이점과 함께 phonon stability, \(\varepsilon^\infty\), 결정상, 온도·비조화 효과의 미포함 여부를 분리해서 기록한다. [1, Methods; 4, §2–4]

## 3. 참고 문헌

1. A. K. A. Lu et al., “SevenNet-Polar for MultiTask Prediction of Energy, Forces, Stress, and Born Effective Charges: Development and Application to ZrO\(_2\), Li\(_3\)PO\(_4\), and Perovskites,” arXiv:2607.14827v3 (2026), https://arxiv.org/abs/2607.14827.
2. SevenNet-Polar project repository and usage documentation, https://github.com/AugustinLu/SevenNet-Polar.
3. X. Gonze and C. Lee, *Physical Review B* **55**, 10355 (1997), https://doi.org/10.1103/PhysRevB.55.10355.
4. J. Robertson, *European Physical Journal Applied Physics* **28**, 265–291 (2004), https://doi.org/10.1051/epjap:2004206.
5. P. W. Koh et al., “WILDS: A Benchmark of in-the-Wild Distribution Shifts,” *Proceedings of Machine Learning Research* **139**, 5637–5664 (2021), https://proceedings.mlr.press/v139/koh21a.html.
