---
description: e3nn의 O(3) 등변성, irreps, tensor product와 원자계 모델에 적용할 때의 주의점을 설명한다.
---

# e3nn과 E(3) 등변 신경망

> 상태: 확인 중 — 출처 검토 및 독립 검토 미완료. 게시 전 검증 필요.

## 1. 무엇을 해결하는가

**e3nn (Euclidean neural networks)**은 PyTorch에서 3차원 회전 및 반사에 대한 등변(equivariant) 신경망을 구성하도록 돕는 라이브러리이다. 입력 원자 구조의 방향을 바꾸었을 때 에너지 같은 스칼라는 그대로이고, 힘 같은 벡터는 함께 회전해야 한다. e3nn은 이러한 변환 법칙을 명시한 특징 공간과 연산을 제공한다. 라이브러리의 주요 표현 API는 `e3nn.o3`이며, 공식 문서는 이 API를 O(3)의 기약표현으로 설명한다. [1, What is e3nn?; 2, Irreps]

### (1) 불변성과 등변성

변환 \(g\)와 함수 \(f\), 입력 및 출력 표현 \(\rho_{\mathrm{in}},\rho_{\mathrm{out}}\)에 대해 등변 조건은

\[
f(\rho_{\mathrm{in}}(g)x)=\rho_{\mathrm{out}}(g)f(x)
\]

이다. 출력 표현이 항등이면 불변(invariant)의 특수한 경우다. 이 식은 정확한 아키텍처 조건이지 학습된 예측값이 자동으로 물리적으로 정확하다는 보장은 아니다. [2, Irreps; 3, Equivariance Testing]

## 2. 기약표현과 패리티

O(3)의 irreducible representation(**irrep**, 기약표현)은 각운동량 차수 \(l=0,1,2,\ldots\), 반전 패리티 \(p=\pm1\)로 구분된다. 회전 부분의 차원은 \(2l+1\)이다. e3nn 표기에서 `0e`는 짝수 패리티 스칼라, `1o`는 홀수 패리티 벡터, `2e`는 5성분의 짝수 패리티 표현이다. `4x0e + 2x1o`는 4개 스칼라와 2개 벡터 채널을 뜻한다. 여기서 `e/o`는 even/odd이며 전하의 부호가 아니다. [2, Irreps; 1, Demonstration]

구현 예시는 다음과 같다.

```python
from e3nn import o3

irreps = o3.Irreps("4x0e + 2x1o")
assert irreps.dim == 10
```

## 3. Tensor product와 원자 그래프

서로 다른 표현의 정보를 결합할 때 tensor product를 사용한다. 적절한 기약표현으로 분해하는 이 연산은 입력 회전에 대해 출력도 정해진 표현대로 변환하도록 만든다. e3nn은 `FullTensorProduct`, `FullyConnectedTensorProduct` 등을 제공하며, 후자는 허용된 결합 경로에 학습 가능한 가중치를 둘 수 있다. [4, Tensor Product; 1, Demonstration]

원자 그래프에서는 원자 사이 상대벡터 \(\mathbf r_{ij}=\mathbf r_j-\mathbf r_i\)를 사용한다. 거리 \(r_{ij}\)의 방사형 함수와 방향 \(\hat{\mathbf r}_{ij}\)의 구면조화함수를 이웃 특징에 결합해 등변 메시지를 구성할 수 있다. 거리 cutoff, 특징 차수 \(l_{\max}\), 정규화 및 이웃 수는 구현과 오차·비용에 영향을 준다. [5, Convolution; 4, Tensor Product]

## 4. 무엇을 검증해야 하는가

- **등변성 검사:** 회전·반사된 입력의 출력과 원래 출력의 변환값을 수치적으로 비교한다. e3nn의 `equivariance_error` 또는 `assert_equivariant`를 사용할 수 있다. [3, Equivariance Testing]
- **공간 대칭과 성능은 별개:** 등변성만으로 에너지·힘·Hamiltonian의 예측 정확도, 긴 범위 상호작용 또는 새로운 화학 환경에서의 일반화가 보장되지 않는다.
- **기하 변환 구별:** O(3)은 회전·반사를, E(3)은 여기에 병진을 포함한다. 상대 좌표만 사용하는 모델은 병진 불변성을 별도로 구현할 수 있으므로 API의 군 표기와 모델 전체의 대칭성을 구별해야 한다. [1, What is e3nn?; 5, Convolution]

관련 문서: [LEM과 SLEM](lem-slem.md), [머신러닝 용어](machine-learning-glossary.md).

## 5. 참고 자료

1. e3nn 개발팀, [Euclidean neural networks 공식 문서](https://docs.e3nn.org/en/latest/), “What is e3nn?” 및 “Demonstration”.
2. e3nn 개발팀, [Irreps API](https://docs.e3nn.org/en/stable/api/o3/o3_irreps.html), “Irreps”.
3. e3nn 개발팀, [Equivariance Testing](https://docs.e3nn.org/en/latest/guide/equivar_testing.html).
4. e3nn 개발팀, [Tensor Product](https://docs.e3nn.org/en/stable/api/o3/o3_tp.html).
5. e3nn 개발팀, [Convolution guide](https://github.com/e3nn/e3nn/blob/main/docs/guide/convolution.rst).
