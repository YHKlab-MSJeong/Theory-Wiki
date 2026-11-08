---
description: 비직교 기저의 스펙트럼을 Chebyshev moments로 근사하고 전자수 조건에서 Fermi 준위를 찾는다.
---

# 비직교 KPM으로 Fermi 준위 찾기

비직교 국소기저에서는 Kohn–Sham 문제를 \(H\mathbf{c}_i=\epsilon_i S\mathbf{c}_i\)로 쓴다. Kernel polynomial method (KPM)은 이 일반화 고유값 문제의 모든 고유값을 직접 구하는 대신, Chebyshev 다항식 moments로 상태밀도(density of states, DOS)를 근사한다. DOS를 점유 함수와 적분해 목표 전자수를 맞추면 Fermi 준위 \(\mu_F\)를 찾을 수 있다. HamGNN-NEGF 논문은 이 절차를 비직교 기저로 확장해 대규모 장치의 Fermi 준위 결정에 사용한다. [1, Eqs. (1)–(9); 2, §§II–III]

![비직교 KPM의 연산자 적용, Chebyshev moments, kernel로 평활화한 DOS와 전자수 조건을 통한 Fermi 준위 탐색 흐름.](../../assets/nonorthogonal-kpm-workflow.svg)

## 1. 무엇을 계산하는가

\(H\)는 Hamiltonian 행렬이고 \(S\)는 overlap 행렬이다. \(S\)가 양의 정부호이면 일반화 고유값 \(\epsilon_i\)는 적절한 직교화 표현에서 Hermitian 연산자의 고유값으로 바꿔 볼 수 있다. KPM은 개별 \(\epsilon_i\)와 고유벡터를 모두 출력하는 고유값 solver가 아니라, 이 스펙트럼을 kernel로 평활화한 DOS를 계산한다. 따라서 고립된 한 고유상태의 에너지나 파동함수가 필요하면 별도의 방법을 써야 한다. [1, Eq. (1); 3, §§2–3]

여기서 찾아내는 \(\mu_F\)는 지정된 Hamiltonian·overlap·전자수·점유 조건에 해당한다. 수송 전류나 transmission을 KPM 자체가 계산하는 것은 아니다. HamGNN-NEGF workflow에서는 KPM이 \(\mu_F\)를 정한 다음 RGF가 \(T(E)\)를 구한다. [2, §II, Fig. 1]

## 2. 일반화 고유값 문제를 KPM 연산으로 바꾼다

문제는

\[
H\mathbf{c}_i=\epsilon_i S\mathbf{c}_i
\]

이다. 양변에 \(S^{-1}\)을 곱하면 형식적으로

\[
X\mathbf{c}_i=\epsilon_i\mathbf{c}_i,\qquad X=S^{-1}H
\]

를 얻는다. 이 표기는 기저의 선형종속성이 제거되어 \(S\)가 가역인 경우의 수학적 설명이다. \(X\)는 원래 일반화 문제와 같은 고유값을 갖지만, \(S^{-1}\)은 보통 조밀해지므로 만들어 저장하면 국소 희소 구조의 이점을 잃을 수 있다.

KPM의 각 행렬–벡터 곱에서 \(X\mathbf{v}\)가 필요할 때는 \(S\mathbf{y}=H\mathbf{v}\) 선형계를 풀어 \(\mathbf{y}=X\mathbf{v}\)를 얻는다. Röder 등의 비직교 KPM은 이 overlap 선형계를 전처리 켤레기울기법 (preconditioned conjugate gradient, PCG)으로 풀며, \(S^{-1}\)을 명시적으로 만들지 않는다. 이는 generalized eigenproblem을 직접 대각화한다는 뜻이 아니라, 그 스펙트럼을 반복적인 행렬–벡터 연산으로 근사한다는 뜻이다. [1, Eqs. (7)–(9)]

\(S^{-1}H\)는 보통의 유클리드 내적에서 Hermitian 행렬이 아니다. \(S\)가 잘 조건화되지 않거나 높은 moment 차수가 필요할 때 수치적 비-Hermitian 오차가 문제가 될 수 있다. Röder 등의 원 논문은 moment 수가 많거나 overlap 행렬의 조건이 좋지 않을 때 \(S^{-1/2}HS^{-1/2}\) 형태를 고려해야 한다고 경고한다. 따라서 구체적인 구현에서는 overlap 선형계의 잔차와 대칭성 오차를 함께 확인해야 한다. [1, pp. 15384–15385]

## 3. Chebyshev moments로 DOS를 복원한다

먼저 스펙트럼 구간 \([E_{\min},E_{\max}]\)을 \([-1,1]\)로 보낸다. \(a=(E_{\max}-E_{\min})/2\), \(b=(E_{\max}+E_{\min})/2\)라 두면

\[
\widetilde{X}=\frac{X-bI}{a}, \qquad x=\frac{E-b}{a}.
\]

Chebyshev 다항식은 \(T_0(x)=1\), \(T_1(x)=x\), \(T_m(x)=2xT_{m-1}(x)-T_{m-2}(x)\)로 재귀 정의된다. 스펙트럼을 알고 있는 범위 안에 넣는 rescaling은 수치 안정성에 중요하다. [1, Eqs. (2), (6); 3, §2]

DOS의 moments는

\[
\mu_m=\operatorname{Tr}\!\left[T_m(\widetilde{X})\right]
\]

이다. trace를 직접 계산하는 비용을 줄이기 위해, 무작위 벡터의 외적 평균이 \(\mathbb{E}[\mathbf{r}\mathbf{r}^\dagger]=I\)가 되도록 벡터 분포를 정하고, 그 표본 \(\mathbf{r}_q\)들로

\[
\mu_m \approx \frac{1}{N_{\mathrm{rand}}}
\sum_{q=1}^{N_{\mathrm{rand}}}
\mathbf{r}_q^\dagger T_m(\widetilde{X})\mathbf{r}_q
\]

처럼 추정할 수 있다. 각 vector에 대해 \(\mathbf{v}_{0,q}=\mathbf{r}_q\), \(\mathbf{v}_{1,q}=\widetilde{X}\mathbf{r}_q\), \(\mathbf{v}_{m,q}=2\widetilde{X}\mathbf{v}_{m-1,q}-\mathbf{v}_{m-2,q}\)를 반복하면 필요한 내적을 얻는다. [1, Eqs. (3), (5)–(8); 2, §II; 3, §§2–3]

유한한 moment 수 \(N_{\mathrm{mom}}\)에서 생기는 Gibbs 진동은 Jackson kernel 등의 감쇠 계수 \(g_m\)를 적용해 줄인다. 스케일된 에너지에서의 DOS 근사는 표준 정규화에서

\[
\rho_K(E)\approx
\frac{g_0\mu_0+2\sum_{m=1}^{N_{\mathrm{mom}}-1}g_m\mu_mT_m(x)}
{\pi a\sqrt{1-x^2}},\qquad -1<x<1.
\]

이 식의 kernel은 각 고유값의 delta 함수 피크를 유한 폭으로 넓혀 DOS를 근사한다. moment 수를 늘리면 보통 에너지 해상도가 좋아지지만, overlap 선형계 풀이 오차나 확률적 trace 추정 오차가 자동으로 사라지는 것은 아니다. [1, Eqs. (2)–(5); 3, §§3–4]

## 4. 전자수 조건으로 Fermi 준위를 찾는다

계산한 DOS를 점유 함수 \(f(E;\mu,T)\)와 곱해 적분한다.

\[
N(\mu,T)=\int \rho_K(E) f(E;\mu,T)\,dE.
\]

목표 전자수 \(N_{\mathrm{target}}\)에 대해 \(N(\mu_F,T)=N_{\mathrm{target}}\)이 되도록 \(\mu_F\)를 찾는다. \(T=0\)에서는 \(f(E;\mu,0)=\Theta(\mu-E)\)라서 \(\mu\) 아래 DOS의 적분값이 전자수를 정한다. 유한 온도에서는 Fermi–Dirac 점유를 사용한다. 실제 계산에서는 DOS에 spin 축퇴도와 k-point 가중치가 포함되는 방식이 목표 전자수 정의와 일치해야 한다. [1, p. 15384; 2, §II]

KPM으로 복원한 DOS는 kernel로 broaden된 근사량이므로 좁은 상태나 band edge 부근에서 \(\mu_F\)가 moment 수, kernel, 무작위 벡터 수에 민감할 수 있다. HamGNN 논문은 \(2\times2\times5\) Si 구조에서 \(N_{\mathrm{mom}}\)과 \(N_{\mathrm{rand}}\)를 수렴시킨 뒤 meV 수준의 Fermi 준위 정확도를 보고한다. 이는 해당 구조와 설정에 관한 결과다. [2, Results, p. 5 and Supplementary Table 1]

## 5. HamGNN-NEGF에서 맡는 역할

논문이 제시하는 경로는 장치 Hamiltonian과 overlap \(H_C,S_C\)에서 비직교 KPM으로 \(\mu_F\)를 정하고, 그 다음 전극 self-energy와 RGF를 사용해 transmission을 계산하는 것이다. KPM 단계가 \(T(E)\)나 열린 계 transmission을 계산한다고 읽으면 안 된다. 또한 논문은 KPM DOS 계산에 에너지 의존 전극 self-energy를 포함하는지 명확히 설명하지 않는다. 따라서 이를 “전극이 열린 상태의 DOS”라고 단정할 근거는 부족하다. [2, §II, Fig. 1]

Results p. 5는 \(2\times2\times5\) Si 사례에서 KPM의 수렴을 확인하고 KPM으로 얻은 Fermi 준위를 이후 NEGF 계산에 사용했다고 적는다. 반면 Methods p. 12는 benchmark systems의 Fermi 준위를 일반화 고유값 문제의 직접 대각화로 얻었다고 적는다. 프리프린트는 두 진술의 적용 대상 관계를 설명하지 않는다. 따라서 KPM을 사용했다고 명시된 해당 Si 사례와 Methods의 직접 대각화 보고를 구분해 기록하며, 모든 transmission benchmark에서 실제 사용한 절차를 하나로 단정하지 않는다. [2, Results, p. 5; Methods, p. 12]

## 6. 수렴과 스케일링에서 확인할 항목

- \(N_{\mathrm{mom}}\): 에너지 해상도와 kernel에 의한 broaden 폭에 주로 영향을 준다.
- \(N_{\mathrm{rand}}\): 확률적 trace 추정의 통계 오차에 영향을 준다.
- 스펙트럼 경계 \(E_{\min},E_{\max}\): 실제 전체 스펙트럼을 포함해야 한다.
- overlap 선형계 수렴: PCG 잔차와 전처리 조건을 확인한다.
- 최종 기준: \(\mu_F\) 변화뿐 아니라 전자수 잔차와 관심 에너지 구간의 DOS 변화를 확인한다. 작은 계에서는 직접 대각화 결과와 비교할 수 있다.

HamGNN 논문은 희소 행렬에서 KPM 비용을 \(O(N_{\mathrm{mom}}N_{\mathrm{rand}}N)\)으로 제시한다. 비직교 문제에서는 각 moment의 연산자 적용에 overlap 선형계 풀이가 더해진다. 따라서 실제 시간은 단순히 원자 수만으로 정해지지 않고 PCG 반복 수와 전처리 효율에도 좌우된다. 선형 스케일링은 희소성, 제한된 국소 결합, 고정된 moment·random-vector·수렴 설정을 유지하는 범위에서 해석해야 한다. [1, pp. 15383–15385; 2, §II]

## 7. 함께 보기

- [DFTH-NEGF: 고정 DFT Hamiltonian으로 계산하는 수송](dfth-negf.md)
- [HamGNN-NEGF](hamgnn-negf.md)
- [NEGF와 전극 self-energy](negf.md)
- [긴 채널 Hamiltonian 확장과 수송](long-channel-transport.md)

## 8. 참고 자료

1. H. Röder, R. N. Silver, D. A. Drabold, and J. J. Dong, “Kernel polynomial method for a nonorthogonal electronic-structure calculation of amorphous diamond,” *Physical Review B* **55**, 15382–15385 (1997), [DOI](https://doi.org/10.1103/PhysRevB.55.15382), [author PDF](https://people.ohio.edu/drabold/pubs/45.pdf), Eqs. (1)–(9).
2. B. Liu et al., “Linear-Scaling Quantum Transport from Machine-Learning Density Functional Theory Hamiltonians,” arXiv:2609.37058v1 (2026), [Abstract](https://arxiv.org/abs/2609.37058), [PDF](https://arxiv.org/pdf/2609.37058v1), §§II–III, Methods, p. 12.
3. A. Weiße, G. Wellein, A. Alvermann, and H. Fehske, “The kernel polynomial method,” *Reviews of Modern Physics* **78**, 275–306 (2006), [DOI](https://doi.org/10.1103/RevModPhys.78.275), §§2–4.

