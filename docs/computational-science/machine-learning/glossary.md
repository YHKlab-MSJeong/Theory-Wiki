---
description: 머신러닝 용어를 영문·한글 이름으로 찾고 정의와 예제 및 관련 문헌으로 연결한다.
---

# Machine learning glossary

논문에서 만난 용어를 영문과 한글 이름으로 찾아볼 수 있도록 정리했다. 각 설명에서는 짧은 정의에 이어 사용 맥락, 수식이나 예제, 함께 확인할 개념과 출처를 제시한다. Fidelity, convolutional neural network (CNN), 학습·평가, 표현·대칭성 및 데이터 증강의 용어를 다룬다.

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
| Surrogate model · 대리모형 | 비용이 큰 계산 등의 입력–출력 관계를 근사하여 대신 평가하는 모형 | [정의와 과학 머신러닝 사례](fidelity.md#surrogate-model) |

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

## 3. 학습과 최적화

학습은 정의한 목적함수에 따라 매개변수를 갱신하는 과정이다. 자료를 묶는 단위와 갱신 횟수, 학습률과 정규화 규약을 함께 읽는다. [7, Chapters 7–8; 8, Linear regression and Optimization]

| 찾는 용어 | 짧은 뜻 | 설명 |
|---|---|---|
| Batch · mini-batch · batch size | 함께 읽는 샘플 묶음과 그 크기 | [샘플과 update 수](training-and-optimization.md#epoch-and-batch) |
| Epoch · 에포크 | 정한 학습 자료를 한 번 순회하는 단위 | [정의와 103개 샘플 예제](training-and-optimization.md#epoch) |
| Gradient · 기울기 | 매개변수별 편미분을 모은 벡터 | [미분과 갱신 예제](training-and-optimization.md#gradient) |
| Learning rate · 학습률 | 최적화 갱신의 크기를 조절하는 계수 | [갱신식](training-and-optimization.md#learning-rate) |
| Loss function · 손실 함수 | 예측과 표적의 차이에 비용을 부여하는 함수 | [목적함수와 관계](training-and-optimization.md#loss-function) |
| Regularization · 정규화 | 일반화 성능을 위해 제약·penalty 등을 적용하는 방법 | [L2와 weight decay](training-and-optimization.md#regularization) |
| Weight decay · 가중치 감쇠 | 갱신에서 가중치 크기를 줄이는 처리 | [알고리즘별 규약](training-and-optimization.md#weight-decay) |

## 4. 평가와 일반화

오차 지표는 비교할 출력과 평균 방식을, 일반화와 전이는 시험 자료와 사용 조건을 함께 지정한다. [9, §§2–3; 10, §2; 11, Leakage taxonomy]

| 찾는 용어 | 짧은 뜻 | 설명 |
|---|---|---|
| Data leakage · 데이터 누출 | 평가 때 사용할 수 없는 정보가 모델 구성에 유입되는 문제 | [전처리와 원본 그룹 분할](evaluation-and-transferability.md#data-leakage) |
| Distribution shift · 분포 변화 · out-of-distribution (OOD) | 학습과 사용 자료의 분포 변화와 정한 분포 밖의 평가 | [조건과 표현의 범위](evaluation-and-transferability.md#distribution-shift) |
| Extrapolation · 외삽 | 정한 학습 입력 범위를 넘어서는 값의 추정 | [함수 예제와 그림](evaluation-and-transferability.md#interpolation-extrapolation) |
| Fine-tuning · 미세조정 | 사전학습한 매개변수 일부 또는 전체를 목표 자료로 갱신하는 절차 | [전이 평가 조건](evaluation-and-transferability.md#transferability) |
| Generalization · 일반화 | 새로운 입력에서도 성능을 내는 성질 | [기대 위험도와 자료 분할](evaluation-and-transferability.md#generalization) |
| Interpolation · 보간 | 정한 입력 표현과 학습 범위 안에서의 값 추정 | [범위와 미관측점](evaluation-and-transferability.md#interpolation-extrapolation) |
| Mean absolute error (MAE) · 평균 절대 오차 | 절대 오차의 평균 | [단위와 숫자 예제](evaluation-and-transferability.md#mae-rmse) |
| Overfitting · 과적합 | 학습 자료에 맞춘 정도에 비해 같은 목표 분포의 새 자료에서 성능이 떨어지는 현상 | [검증 곡선과 조건](evaluation-and-transferability.md#overfitting) |
| Root mean squared error (RMSE) · 평균 제곱 오차의 제곱근 | 제곱 오차를 평균한 뒤 제곱근을 취한 값 | [MAE와 비교](evaluation-and-transferability.md#mae-rmse) |
| Transfer learning · 전이학습 | 기존 과제·도메인의 지식을 목표 학습에 활용하는 접근 | [고정 특징과 미세조정](evaluation-and-transferability.md#transferability) |
| Transferability · 전이 가능성 | 지정한 새 대상에 적용했을 때 유용한 성능을 유지하는 정도 | [과학 머신러닝의 평가 예](evaluation-and-transferability.md#transferability) |

## 5. 표현과 대칭성

입력을 수치 표현으로 바꾸는 방식과 출력의 변환 규칙은 모델의 구조와 적용 범위에 연결된다. [12, §3; 13, §2; 14, Equivariance]

| 찾는 용어 | 짧은 뜻 | 설명 |
|---|---|---|
| Attention · 어텐션 | 입력에서 계산한 가중치로 value를 모으는 연산 | [행렬 shape와 작은 계산](representation-and-symmetry.md#attention) |
| Descriptor · 기술자 | 입력의 특성을 수치로 표현한 것 | [원자 환경 예제](representation-and-symmetry.md#descriptor) |
| Embedding · 임베딩 | 입력을 벡터 등의 표현으로 대응시키는 사상 또는 그 결과 | [원자종과 학습 특징](representation-and-symmetry.md#embedding) |
| Equivariance · 등변성(공변성) | 입력 변환에 따라 출력도 정한 규칙으로 변하는 성질 | [벡터·텐서 회전](representation-and-symmetry.md#equivariance) |
| Invariance · 불변성 | 정한 입력 변환에 출력이 유지되는 성질 | [스칼라와 변환](representation-and-symmetry.md#invariance) |
| Locality · 국소성 | 모델의 연산이 정한 이웃 범위의 정보에 의존하는 성질 | [Cutoff와 출력의 범위](representation-and-symmetry.md#locality) |
| Message passing · 메시지 전달 | 그래프 이웃의 정보를 모아 노드 특징을 갱신하는 절차 | [Hop과 사슬 예제](representation-and-symmetry.md#message-passing) |

## 6. 데이터 증강

입력 변환과 대응 표적의 의미를 정하고, 평가 질문에 맞는 원본 그룹 분할을 유지하며 증강을 구성한다. [15, §3.1; 11, L1 and L3]

| 찾는 용어 | 짧은 뜻 | 설명 |
|---|---|---|
| Data augmentation · 데이터 증강 | 기존 자료에서 변환 입력과 대응 표적을 만들어 학습에 사용하는 방법 | [목적함수와 물리적 조건](data-augmentation.md#augmentation-objective) |
| Mixup · 혼합 증강 | 입력 쌍과 표적 쌍의 볼록결합으로 학습하는 방법 | [수식과 soft label](data-augmentation.md#noise-and-mixup) |
| Noise augmentation · 잡음 증강 | 정한 잡음 모형으로 입력을 섭동하는 방법 | [잡음과 원자 변위의 조건](data-augmentation.md#noise-and-mixup) |

## 7. 관련 연구 문서와 참고 자료

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
7. I. Goodfellow, Y. Bengio, A. Courville, *Deep Learning*, Chapters 5, 7–8 (2016). [공식 본문](https://www.deeplearningbook.org/)
8. A. Zhang, Z. C. Lipton, M. Li, A. J. Smola, *Dive into Deep Learning*, Linear regression and Optimization. [공식 본문](https://d2l.ai/)
9. T. Chai, R. R. Draxler, “Root mean square error (RMSE) or mean absolute error (MAE)?” (2014). [원문](https://gmd.copernicus.org/articles/7/1247/2014/)
10. S. J. Pan, Q. Yang, “A Survey on Transfer Learning” (2010). [원문](https://www.cse.cuhk.edu.hk/~sinnopan/publications/TLsurvey_0822.pdf)
11. S. Kapoor, A. Narayanan, “Leakage and the reproducibility crisis in machine-learning-based science” (2023). [원문](https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/)
12. A. Vaswani et al., “Attention Is All You Need” (2017). [원문](https://arxiv.org/abs/1706.03762)
13. J. Gilmer et al., “Neural Message Passing for Quantum Chemistry” (2017). [원문](https://arxiv.org/abs/1704.01212)
14. S. Batzner et al., “E(3)-Equivariant Graph Neural Networks for Data-Efficient and Accurate Interatomic Potentials” (2022). [원문](https://arxiv.org/pdf/2101.03164)
15. S. Chen, E. Dobriban, J. H. Lee, “A Group-Theoretic Framework for Data Augmentation” (2020). [원문](https://jmlr.org/papers/volume21/20-163/20-163.pdf)
