---
description: Loss·gradient·learning rate·epoch·mini-batch와 regularization을 수식과 작은 계산 예제로 연결한다.
---

# Training and optimization

학습에서는 예측 오차를 수로 나타내고, 그 수가 매개변수에 따라 변하는 방향을 계산한 뒤 매개변수를 갱신한다. 논문의 loss, learning rate, batch size, epoch는 이 과정의 서로 다른 부분을 가리킨다. 아래에서는 유한한 지도학습 자료와 미분 가능한 목적함수를 기준으로 정의한다. [1, §§8.1, 8.3.1](https://www.deeplearningbook.org/contents/optimization.html), [2, §3.1.1](https://d2l.ai/chapter_linear-regression/linear-regression.html)

<a id="loss-function"></a>
<a id="objective-function"></a>
<a id="loss-and-objective"></a>

## 1. Loss function과 objective function

**Loss function(손실함수)**은 예측과 표적의 차이 등 학습에서 줄이려는 비용을 수로 나타낸다. **Objective function(목적함수)**은 최적화 알고리즘이 실제로 최소화하는 함수다. 문헌에서는 loss와 cost를 전체 목적함수의 이름으로도 사용한다. 여기서는 샘플별 손실을 \(\ell_i\), 자료 전체의 평균을 \(J_{\mathrm{data}}\), 정규화까지 포함한 목적함수를 \(J\)로 구분한다. [1, §§8.1–8.1.2](https://www.deeplearningbook.org/contents/optimization.html), [2, §3.1.1.2](https://d2l.ai/chapter_linear-regression/linear-regression.html)

학습 자료가 \(\mathcal D=\{(x_i,y_i)\}_{i=1}^{N}\)이고 예측이 \(f_\theta(x_i)\)이면

\[
\ell_i(\theta)=\ell(f_\theta(x_i),y_i),\qquad
J_{\mathrm{data}}(\theta)=\frac{1}{N}\sum_{i=1}^{N}\ell_i(\theta),\qquad
J(\theta)=J_{\mathrm{data}}(\theta)+\lambda\Omega(\theta)
\]

로 쓸 수 있다. \(N\)은 학습 샘플 수, \(x_i\)는 입력, \(y_i\)는 표적, \(\theta\in\mathbb R^p\)는 \(p\)개 학습 매개변수의 벡터다. \(\Omega\)는 정규화 penalty, \(\lambda\ge0\)는 그 기여를 정하는 계수다. 마지막 두 항은 더할 수 있는 단위를 가져야 한다. 자료 평균을 최소화하는 설정을 empirical risk minimization(ERM), 즉 경험위험 최소화라 한다. [1, §8.1.1, Eq. (8.3)](https://www.deeplearningbook.org/contents/optimization.html), [2, Eqs. (3.1.6)–(3.1.7)](https://d2l.ai/chapter_linear-regression/linear-regression.html), [3, Eq. (7.1)](https://www.deeplearningbook.org/contents/regularization.html), [4, Eq. (3.7.2)](https://d2l.ai/chapter_linear-regression/weight-decay.html)

### (1) 제곱오차와 정규화 규약

스칼라 회귀의 한 선택은 \(\ell_i=\tfrac12[f_\theta(x_i)-y_i]^2\)다. 앞의 \(1/2\)는 미분할 때 생기는 2를 상쇄한다. Mean squared error(MSE, 평균제곱오차)를 \(N^{-1}\sum_i[f_\theta(x_i)-y_i]^2\)로 정의하면 위 \(J_{\mathrm{data}}\)는 MSE의 절반이다. 예측과 표적이 eV 단위이면 이 제곱오차의 단위는 \(\mathrm{eV}^2\)다. [2, Eqs. (3.1.5)–(3.1.6)](https://d2l.ai/chapter_linear-regression/linear-regression.html), [1, §8.1](https://www.deeplearningbook.org/contents/optimization.html)

합과 평균은 정규화항이 없을 때 같은 최소점을 갖지만 gradient 크기는 \(N\)배 차이 난다. 정규화항을 함께 쓰면 자료항의 합·평균 규약에 맞춰 \(\lambda\)도 확인해야 한다. 예를 들어 위 \(J\)에 \(N\)을 곱하면 \(\sum_i\ell_i+N\lambda\Omega\)가 된다. 이 관계는 위 정의를 대수적으로 정리한 것이다.

<a id="gradient"></a>
<a id="learning-rate"></a>

## 2. Gradient와 learning rate

**Gradient(기울기)** \(\nabla_\theta J\)는 각 매개변수에 대한 편미분을 모은 벡터다. 미분 가능한 \(J\)의 작은 변화는 \(J(\theta+\Delta\theta)\approx J(\theta)+\nabla_\theta J\cdot\Delta\theta\)로 주어진다. 유클리드 좌표에서 gradient의 반대 방향은 국소적으로 함숫값이 가장 빠르게 감소하는 방향이다. **Learning rate(학습률)** \(\eta_t>0\)는 갱신 크기에 곱하는 계수다. Gradient descent의 한 단계는 다음과 같다. [5, §4.3, Eq. (4.5)](https://www.deeplearningbook.org/contents/numerical.html), [6, §§12.3.1–12.3.2](https://d2l.ai/chapter_optimization/gd.html)

\[
\nabla_\theta J=
\left(\frac{\partial J}{\partial\theta_1},\ldots,
\frac{\partial J}{\partial\theta_p}\right)^{\!T},\qquad
\theta_t=\theta_{t-1}-\eta_t\nabla_\theta J(\theta_{t-1}).
\]

\(t=1,2,\ldots\)는 갱신 단계, \(\theta_0\)는 초기 매개변수, \(\Delta\theta\)는 매개변수의 변화 벡터이고 위 첨자 \(T\)는 전치다. 학습률은 단계에 따라 바뀔 수 있다. 아래 수치 예제에서는 입력·표적·매개변수를 모두 무차원으로 둔다. 실제 문제에서는 변수의 단위와 스케일을 정한 후 갱신식을 해석한다. [1, §8.3.1](https://www.deeplearningbook.org/contents/optimization.html), [6, §12.3.1](https://d2l.ai/chapter_optimization/gd.html)

### (1) 미분과 단일 갱신의 계산 예제

선형 예측 \(f_w(x)=wx\)에 입력 \(x=2\), 표적 \(y=6\)인 한 샘플을 주고 정규화항을 0으로 둔다. 제곱오차와 미분은 정확히

\[
J(w)=\frac12(2w-6)^2=2(w-3)^2,\qquad
\frac{dJ}{dw}=4(w-3)
\]

이다. 초기값 \(w_0=1\)에서 gradient는 \(-8\), 손실은 8이다. \(\eta=0.1\)이면 \(w_1=1-0.1(-8)=1.8\)이고 손실은 \(J(1.8)=2.88\)이 된다. 제곱오차와 gradient descent 정의에 대입한 자체 계산이다. [2, Eqs. (3.1.5), (3.1.11)](https://d2l.ai/chapter_linear-regression/linear-regression.html), [5, §4.3](https://www.deeplearningbook.org/contents/numerical.html)

학습률의 영향도 같은 식에서 구할 수 있다. 최솟값을 주는 \(w^*=3\)으로부터의 차이를 \(e_t=w_t-3\)이라 하면 \(e_t=(1-4\eta)e_{t-1}\)다. 이 예제에서 일정한 학습률로 임의의 초기 오차를 줄이려면 \(|1-4\eta|<1\), 즉 \(0<\eta<0.5\)여야 한다.

| 일정한 학습률 \(\eta\) | 첫 갱신 \(w_1\) | 첫 갱신 후 손실 | 오차의 단계별 배율 \(1-4\eta\) |
|---|---|---|---|
| 0.1 | 1.8 | 2.88 | 0.6 |
| 0.5 | 5.0 | 8.00 | \(-1\) |
| 0.6 | 5.8 | 15.68 | \(-1.4\) |

이 표와 수렴 구간은 지정한 1차원 이차함수의 자체 유도 결과다. \(\eta=0.5\)에서는 \(w=1\)과 5를 왕복한다. 곡률이 다른 함수나 신경망에 학습률 0.5라는 경계를 적용하려면 해당 목적함수를 새로 분석해야 한다. 일반적인 학습률과 곡률의 관계는 원문의 이차 근사에서 확인할 수 있다. [5, §4.3.1, Eqs. (4.8)–(4.9)](https://www.deeplearningbook.org/contents/numerical.html), [6, §12.3.1](https://d2l.ai/chapter_optimization/gd.html)

<a id="mini-batch"></a>
<a id="batch-size"></a>
<a id="epoch"></a>
<a id="epoch-and-batch"></a>

## 3. Mini-batch, batch size, epoch

**Mini-batch(미니배치)**는 한 번의 gradient 계산 등에 함께 사용하는 샘플 묶음이다. **Batch size(배치 크기)**는 그 묶음의 샘플 수다. \(t\)번째 묶음의 인덱스 집합을 \(\mathcal B_t\), 실제 크기를 \(b_t=|\mathcal B_t|\)라 하면 자료항의 gradient는 다음처럼 계산한다. [1, §8.1.3, Eq. (8.9)](https://www.deeplearningbook.org/contents/optimization.html), [7, §12.5.2, Eq. (12.5.2)](https://d2l.ai/chapter_optimization/minibatch-sgd.html)

\[
g_t=\frac{1}{b_t}\sum_{i\in\mathcal B_t}
\nabla_\theta\ell_i(\theta_{t-1}).
\]

매개변수를 고정한 상태에서 학습 자료의 인덱스를 균일하게 무작위 추출하면 이 평균은 전체 자료 gradient의 불편 추정량이다. 이 조건에서의 기대값은 \(\mathbb E[g_t]=\nabla_\theta J_{\mathrm{data}}\)다. 실제 학습에서는 매 단계 매개변수가 바뀌며 자료를 섞어 순서대로 읽는 방법도 사용하므로, 샘플링 조건을 함께 확인한다. [1, §§8.1.3, 8.3.1](https://www.deeplearningbook.org/contents/optimization.html), [7, §12.5.2](https://d2l.ai/chapter_optimization/minibatch-sgd.html)

**Epoch(에포크)**는 유한한 학습 자료를 한 차례 통과하는 학습량을 뜻한다. **Step 또는 iteration**은 갱신 등의 반복 단계다. 매 mini-batch에서 한 번 갱신하는 설정에서는 한 epoch에 여러 optimizer step이 들어간다. 무작위 복원추출이나 streaming 자료에서는 한 epoch를 셈하는 규약도 기록해야 한다. [1, §8.1.3의 multiple passes 논의](https://www.deeplearningbook.org/contents/optimization.html), [8, “Babysitting the learning process”](https://cs231n.github.io/neural-networks-3/)

### (1) 103개 샘플을 32개씩 읽는 예제

단일 프로세스에서 중복 없이 자료를 한 번씩 읽고, 마지막 불완전 batch를 유지하며, batch마다 한 번 갱신한다고 가정한다. \(N=103\), 지정 batch size \(B=32\)이면 batch들의 실제 크기는 32, 32, 32, 7이다. 갱신 횟수는 \(\lceil N/B\rceil=4\)이므로 10 epoch에 40 step을 수행한다. 이는 정의에 따른 자체 계산이다.

PyTorch의 map-style dataset에서 `drop_last=False`로 구성한 일반적인 `BatchSampler`가 이처럼 마지막 묶음을 유지한다. `drop_last=True`이면 이 예에서 마지막 7개를 제외해 3개 batch, 96개 샘플을 처리한다. 처리 샘플 수는 sampler, 분산 실행, worker별 iterable dataset 등의 설정에 따라 달라질 수 있다. [9, “Loading Batched and Non-Batched Data”, “BatchSampler”, “DistributedSampler”](https://docs.pytorch.org/docs/2.15/data.html)

Batch 평균을 모아 전체 자료의 평균 손실을 계산할 때도 크기를 반영한다. 같은 고정된 모델에서 네 batch의 평균 손실이 각각 \(\bar\ell_1,\ldots,\bar\ell_4\)라면 전체 평균은 \((32\bar\ell_1+32\bar\ell_2+32\bar\ell_3+7\bar\ell_4)/103\)이다. 네 평균을 같은 가중치로 더하는 방식은 각 batch에 1/4씩 가중치를 준다. 두 계산의 차이는 샘플 평균의 정의에서 직접 얻는다.

<a id="optimizer"></a>
<a id="sgd"></a>

## 4. Optimizer와 SGD·Adam

**Optimizer(최적화 알고리즘)**는 계산한 gradient 등을 이용해 매개변수를 갱신하는 규칙이다. **Stochastic gradient descent(SGD, 확률적 경사하강법)**의 가장 단순한 형태는 무작위 샘플이나 mini-batch의 gradient로 \(\theta_t=\theta_{t-1}-\eta_tg_t\)를 계산한다. 아래에서는 momentum이 없는 SGD를 기준으로 삼는다. [1, §8.3.1, Algorithm 8.1](https://www.deeplearningbook.org/contents/optimization.html), [2, §3.1.1.4](https://d2l.ai/chapter_linear-regression/linear-regression.html)

<a id="adam"></a>

### (1) Adam의 상태와 갱신

**Adaptive moment estimation(Adam)**은 gradient와 gradient 제곱의 지수이동평균을 유지하는 알고리즘이다. 아래는 Kingma와 Ba의 원 논문 Algorithm 1을 이 문서의 기호로 옮긴 것이다. \(m_0=v_0=0\)에서 시작한다. [10, §2, Algorithm 1](https://arxiv.org/pdf/1412.6980), [11, §12.10.1](https://d2l.ai/chapter_optimization/adam.html)

\[
\begin{aligned}
m_t&=\beta_1m_{t-1}+(1-\beta_1)g_t,\\
v_t&=\beta_2v_{t-1}+(1-\beta_2)(g_t\odot g_t),\\
\hat m_t&=\frac{m_t}{1-\beta_1^t},\qquad
\hat v_t=\frac{v_t}{1-\beta_2^t},\\
\theta_t&=\theta_{t-1}-\eta_t
\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}.
\end{aligned}
\]

\(m_t,v_t\)는 각각 1차 모멘트와 비중심 2차 모멘트의 추정 벡터다. \(\beta_1,\beta_2\in[0,1)\)는 이동평균 계수, \(\epsilon>0\)은 분모를 안정화하는 작은 상수다. \(\odot\), 제곱근, 나눗셈은 성분별 연산이다. Hat은 0으로 초기화한 이동평균의 편향을 보정한 값을 뜻한다. Adam에서도 학습률 \(\eta_t\)를 설정한다. [10, §§2–3](https://arxiv.org/pdf/1412.6980), [11, Eqs. (12.10.1)–(12.10.4)](https://d2l.ai/chapter_optimization/adam.html)

<a id="regularization"></a>
<a id="l2-regularization"></a>
<a id="weight-decay"></a>

## 5. Regularization과 weight decay

**Regularization(정규화)**은 일반화 오차를 줄이려는 목적에서 학습 규칙이나 모델에 제약을 가하는 방법을 가리킨다. 목적함수에 penalty를 더하는 방법이 한 예다. 효과는 validation 자료 등에서 평가하며 정규화 강도도 학습 설정으로 정한다. [3, 서두와 §7.1](https://www.deeplearningbook.org/contents/regularization.html), [4, §3.7.1](https://d2l.ai/chapter_linear-regression/weight-decay.html)

### (1) L2 penalty와 기본 SGD

설명을 위해 모든 매개변수에 같은 계수를 적용하고 \(\Omega(\theta)=\tfrac12\|\theta\|_2^2\)로 둔다. 여기서 \(\|\theta\|_2^2=\sum_{j=1}^{p}\theta_j^2\)는 유클리드 노름의 제곱이다. 이는 **L2 regularization**의 한 규약이다. Penalty의 gradient는 \(\lambda\theta\)이므로 기본 SGD에서는

\[
\theta_t
=\theta_{t-1}-\eta_t(g_t+\lambda\theta_{t-1})
=(1-\eta_t\lambda)\theta_{t-1}-\eta_tg_t
\]

가 된다. 따라서 동일한 gradient와 매개변수 집합을 쓰는 기본 SGD에서 L2 penalty는 이 곱셈형 **weight decay(가중치 감쇠)**와 같은 갱신을 만든다. \(0<\eta_t\lambda<1\)이면 gradient 갱신에 앞서 매개변수의 크기를 줄이는 계수가 된다. 실제 구현에서 bias 등을 제외한다면 적용 매개변수 집합도 명시한다. [3, §7.1.1, Eqs. (7.3)–(7.5)](https://www.deeplearningbook.org/contents/regularization.html), [4, §3.7.1, Eq. (3.7.3)](https://d2l.ai/chapter_linear-regression/weight-decay.html), [12, §2, Proposition 1](https://arxiv.org/html/1711.05101v3)

<a id="adamw"></a>

### (2) Adam에서 L2와 AdamW의 차이

Adam에 L2 penalty를 더하면 \(\tilde g_t=g_t+\lambda\theta_{t-1}\)가 위 \(m_t,v_t\) 계산에 들어간다. Penalty의 gradient가 이동평균과 성분별 재조정을 함께 거친다. **Adam with decoupled weight decay(AdamW)**는 자료항 gradient \(g_t\)로 모멘트를 계산하고 weight decay를 별도 항으로 적용한다. 아래에서는 decay 계수를 \(1-\eta_t\lambda\)로 표기하는 규약을 쓴다. [12, §2, Algorithm 2와 Proposition 2](https://arxiv.org/html/1711.05101v3), [13, “On Weight Decay for Adaptive Optimizers”](https://ojs.aaai.org/index.php/AAAI/article/download/16837/16644)

\[
\theta_t=(1-\eta_t\lambda)\theta_{t-1}
-\eta_t\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}.
\]

두 방식은 일반적으로 서로 다른 궤적을 만든다. 예를 들어 초기 모멘트가 0이고 \(g_1=0\), \(\theta_0=2\), \(\lambda=0.1\), \(\eta_1=0.01\)인 한 성분을 생각한다. Adam+L2에서는 \(\hat m_1=0.2\), \(\hat v_1=0.04\)이므로 변화량이 \(-0.01\times0.2/(0.2+\epsilon)\)다. AdamW에서는 자료 gradient의 모멘트가 0이고 decay에 의한 변화량은 \(-0.01\times0.1\times2=-0.002\)다. 이 값은 두 갱신식에 대입한 자체 계산이며, \(\epsilon\ll0.2\)일 때 첫 변화량은 약 \(-0.01\)이다. [10, Algorithm 1](https://arxiv.org/pdf/1412.6980), [12, Algorithm 2](https://arxiv.org/html/1711.05101v3), [13, “On Weight Decay for Adaptive Optimizers”의 모멘트 분석](https://ojs.aaai.org/index.php/AAAI/article/download/16837/16644)

같은 `weight_decay`라는 설정 이름을 읽더라도 L2 gradient를 모멘트에 넣는지, 별도 decay를 적용하는지와 계수 규약을 확인해야 갱신식을 정할 수 있다. Loshchilov와 Hutter의 Algorithm 2는 base learning rate와 schedule multiplier를 별도 기호로 쓴다. 이 문서의 \(\eta_t\)는 둘을 곱한 실제 학습률이며, decay 계수도 위 식에 맞춰 정의했다. [12, §2, Algorithms 1–2](https://arxiv.org/html/1711.05101v3), [13, “On Weight Decay for Adaptive Optimizers”](https://ojs.aaai.org/index.php/AAAI/article/download/16837/16644)

## 6. 관련 이론과 연구 문서

- [평가 자료와 일반화·전이 가능성](evaluation-and-transferability.md)은 학습에 사용하는 자료와 성능을 판단하는 자료의 역할을 설명한다.
- [데이터 증강](data-augmentation.md)은 학습 입력을 변환하는 방법과 물리적으로 허용되는 변환을 설명한다.
- [표현과 대칭성](representation-and-symmetry.md)은 모델에 주는 입력 표현과 변환 규칙을 설명한다.
- [Fidelity와 다중 충실도](fidelity.md)는 학습 표적이 참조하는 계산 수준을 읽을 때 연결된다.
- [CNN의 kernel과 receptive field](cnn-kernel-receptive-field.md)는 최적화되는 매개변수가 어떤 국소 연산을 구성하는지 설명한다.
- [DeePTB와 NEGF 수송](../../computational-materials-science/quantum-transport/deeptb-negf.md)은 전자구조를 학습한 뒤 수송 계산에 사용하는 연구 사례다.
- [머신러닝 용어 찾아보기](glossary.md)에서 영문·한글 용어를 함께 찾을 수 있다.

## 7. 참고 자료

1. I. Goodfellow, Y. Bengio, A. Courville, *Deep Learning*, Chapter 8, “Optimization for Training Deep Models” (2016). [원문](https://www.deeplearningbook.org/contents/optimization.html)
2. A. Zhang, Z. C. Lipton, M. Li, A. J. Smola, *Dive into Deep Learning*, §3.1, “Linear Regression” (온라인판). [원문](https://d2l.ai/chapter_linear-regression/linear-regression.html)
3. I. Goodfellow, Y. Bengio, A. Courville, *Deep Learning*, Chapter 7, “Regularization for Deep Learning” (2016). [원문](https://www.deeplearningbook.org/contents/regularization.html)
4. A. Zhang et al., *Dive into Deep Learning*, §3.7, “Weight Decay” (온라인판). [원문](https://d2l.ai/chapter_linear-regression/weight-decay.html)
5. I. Goodfellow, Y. Bengio, A. Courville, *Deep Learning*, §4.3, “Gradient-Based Optimization” (2016). [원문](https://www.deeplearningbook.org/contents/numerical.html)
6. A. Zhang et al., *Dive into Deep Learning*, §12.3, “Gradient Descent” (온라인판). [원문](https://d2l.ai/chapter_optimization/gd.html)
7. A. Zhang et al., *Dive into Deep Learning*, §12.5, “Minibatch Stochastic Gradient Descent” (온라인판). [원문](https://d2l.ai/chapter_optimization/minibatch-sgd.html)
8. Stanford CS231n, “Neural Networks Part 3”, “Babysitting the learning process”. [강의 노트](https://cs231n.github.io/neural-networks-3/)
9. PyTorch, `torch.utils.data`, “BatchSampler”와 “DistributedSampler”, 2.15 문서. [공식 문서](https://docs.pytorch.org/docs/2.15/data.html)
10. D. P. Kingma, J. Ba, “Adam: A Method for Stochastic Optimization”, *ICLR* (2015), §§2–3와 Algorithm 1. [원문](https://arxiv.org/pdf/1412.6980)
11. A. Zhang et al., *Dive into Deep Learning*, §12.10, “Adam” (온라인판). [원문](https://d2l.ai/chapter_optimization/adam.html)
12. I. Loshchilov, F. Hutter, “Decoupled Weight Decay Regularization”, *ICLR* (2019), §2와 Appendix A. [원문](https://arxiv.org/html/1711.05101v3)
13. J. Bjorck, K. Q. Weinberger, C. P. Gomes, “Understanding Decoupled and Early Weight Decay”, *AAAI* **35**, 6777–6785 (2021), “On Weight Decay for Adaptive Optimizers”. [원문](https://ojs.aaai.org/index.php/AAAI/article/download/16837/16644)
