---
description: 머신러닝 용어를 영문·한글 이름으로 찾고 정의와 예제 및 관련 문헌으로 연결한다.
---

# 머신러닝 용어 찾아보기

논문에서 만난 용어를 영문과 한글 이름으로 찾아볼 수 있도록 정리했다. 각 설명에서는 짧은 정의에 이어 사용 맥락, 수식이나 예제, 함께 확인할 개념과 출처를 제시한다. 현재 수록한 항목은 fidelity와 과학 모델링, CNN의 국소 연산과 수용영역이다.

## 1. Fidelity와 모델링

Fidelity는 참조 대상에 따라 의미와 평가 방법이 달라진다. 과학 모형에서는 근사 수준과 관심 물리량을, 설명 모델에서는 재현하려는 원 모델과 입력 범위를 함께 확인한다. [1, §§1–2; 2, §3; 3, §3 “Empirical Evaluation”]

| 찾는 용어 | 짧은 뜻 | 설명 |
|---|---|---|
| Accuracy · 정확도 | 분류에서는 정답 레이블과 예측이 일치하는 비율 | [정의와 예제](fidelity.md#explanation-fidelity) |
| Fidelity · 충실도 | 특정 참조 대상의 특성·동작을 충실하게 표현하는 정도 | [문맥별 정의](fidelity.md) |
| High fidelity · 고충실도 | 해당 문제의 기준으로 삼는 모형·자료의 수준 | [수준과 비교 기준](fidelity.md#fidelity-levels) |
| Local fidelity · 국소 충실도 | 특정 입력 주변에서 원 모델을 재현하는 정도 | [LIME의 손실](fidelity.md#local-fidelity) |
| Low fidelity · 저충실도 | 같은 관심 출력을 낮은 비용으로 근사하는 모형·자료의 수준 | [수준과 적용 범위](fidelity.md#fidelity-levels) |
| Multi-fidelity · 다중 충실도 | 서로 다른 수준의 모형·자료를 결합하는 접근 | [다중 충실도 학습](fidelity.md#fidelity-levels) |
| Surrogate model · 대리모형 | 비용이 큰 계산 등의 입력–출력 관계를 근사하여 대신 평가하는 모형 | [정의와 과학 ML 사례](fidelity.md#surrogate-model) |

## 2. CNN의 연산과 수용영역

CNN의 크기와 범위를 읽을 때는 해당 층의 입력 feature map과 원 입력의 좌표를 함께 확인한다. 공간 크기와 채널 수를 명시하면 어떤 값을 가중합하는지 알 수 있다. [4, 연산식과 Shape; 5, Problem setup and Single-path networks; 6, §§2–3]

| 찾는 용어 | 짧은 뜻 | 설명 |
|---|---|---|
| Channel · 채널 | 동일한 공간 위치의 성분을 구분하는 축 | [채널과 배열 shape](cnn-kernel-receptive-field.md#kernel-and-channel) |
| CNN · 합성곱 신경망 | 격자 자료의 국소 연산을 사용하는 신경망 | [연산과 예제](cnn-kernel-receptive-field.md) |
| Dilation · 팽창률 | 이웃 kernel 원소가 참조하는 입력 격자점 사이 간격 | [유효 kernel 폭](cnn-kernel-receptive-field.md#stride-padding-dilation) |
| Effective receptive field · 유효 수용영역 | 출력에 상당한 영향을 주는 입력 영역 | [기울기 기반 분석](cnn-kernel-receptive-field.md#effective-receptive-field) |
| Feature map · 특징 맵 | 공간 좌표에 특징 값을 배열한 출력 | [단일 채널과 전체 출력](cnn-kernel-receptive-field.md#kernel-and-channel) |
| Filter · 필터 | Convolution 가중치에 사용하는 이름 | [Kernel과 shape](cnn-kernel-receptive-field.md#kernel-and-channel) |
| Kernel · 커널 | 국소 가중합에 사용하는 가중치 배열 | [정의와 매개변수 수](cnn-kernel-receptive-field.md#kernel-and-channel) |
| Padding · 패딩 | 해당 층 입력의 경계를 확장하는 처리 | [경계와 출력 크기](cnn-kernel-receptive-field.md#stride-padding-dilation) |
| Receptive field · 수용영역 | 출력에서 연결을 추적해 얻는 원 입력의 영역 | [도식과 점화식](cnn-kernel-receptive-field.md#receptive-field) |
| Stride · 보폭 | 출력 위치를 한 칸 옮길 때 입력 window를 이동하는 간격 | [정의와 크기 예제](cnn-kernel-receptive-field.md#stride-padding-dilation) |

## 3. 관련 연구 문서와 참고 자료

학습 모델이 원자 환경에서 행렬을 구성하는 실제 사례와, 벡터·텐서 물리량을 예측하는 사례도 이어서 읽을 수 있다.

- [DeePTB와 NEGF 수송](../../computational-materials-science/quantum-transport/deeptb-negf.md)
- [HamGNN-NEGF](../../computational-materials-science/quantum-transport/hamgnn-negf.md)
- [Born 유효전하의 머신러닝](../../computational-materials-science/dielectric-response/ml-born-effective-charge.md)

1. B. Peherstorfer, K. Willcox, M. Gunzburger, “Survey of Multifidelity Methods in Uncertainty Propagation, Inference, and Optimization” (2018). [원문](https://arxiv.org/abs/1806.10761)
2. M. T. Ribeiro et al., “Why Should I Trust You? Explaining the Predictions of Any Classifier” (2016). [원문](https://ucinlp.github.io/files/papers/lime-kdd16.pdf)
3. M. W. Craven, J. W. Shavlik, “Extracting Tree-Structured Representations of Trained Networks” (1995). [원문](https://proceedings.neurips.cc/paper_files/paper/1995/file/45f31d16b1058d586fc3be7207b58053-Paper.pdf)
4. PyTorch, `Conv2d`. [공식 문서](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html)
5. A. Araujo, W. Norris, J. Sim, “Computing Receptive Fields of Convolutional Neural Networks” (2019). [원문](https://distill.pub/2019/computing-receptive-fields/)
6. W. Luo et al., “Understanding the Effective Receptive Field in Deep Convolutional Neural Networks” (2016). [원문](https://proceedings.neurips.cc/paper_files/paper/2016/file/c8067ad1937f728f51288b3eb986afaa-Paper.pdf)
