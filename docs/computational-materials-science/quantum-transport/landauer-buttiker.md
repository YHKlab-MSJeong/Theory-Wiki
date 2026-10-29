---
description: 다중 전극 Landauer–Büttiker 수송에서 전하·열 전류와 선형 열전 응답을 다룬다.
---

# Landauer–Büttiker transport

Landauer–Büttiker formalism은 두 전극 Landauer 식을 여러 평형 reservoir로 확장한다. 이 글은 각 전극이 화학 퍼텐셜과 온도를 가진 정상상태의 비상호작용 reservoir이고, 중심영역의 수송이 탄성·위상결맞음이라는 기준 모형을 다룬다. 다중 단자 전하 전류, 열 전류, 선형 열전 응답, 그리고 probe 전극의 경계조건을 연결한다. 상호작용 self-energy나 비탄성 산란을 미시적으로 풀어내는 일반식은 이 범위 밖에 둔다. [1, §IV.A; 2, 식 (1)–(3); 3, 식 (1)–(4)]

## 1. 전극, 전송 계수와 부호

\(M\)개의 전극을 \(\alpha,\beta=1,\ldots,M\)로 표시한다. 전극 \(\alpha\)는 Fermi 분포

\[
f_\alpha(E)=\frac{1}{1+\exp[(E-\mu_\alpha)/(k_B\Theta_\alpha)]}
\]

를 유지한다고 둔다. 이 글에서는 \(T_{\alpha\beta,\sigma}(E)\)를 스핀 \(\sigma\)의 전자가 전극 \(\alpha\)에서 나와 전극 \(\beta\)로 들어갈 transmission으로 정의한다. 문헌과 프로그램은 두 아래첨자의 순서를 반대로 쓸 수 있으므로, 전송 곡선을 비교할 때 방향 정의를 함께 확인해야 한다. [1, §IV.A, 식 (24)–(25); 2, 식 (1a); 4, 식 (4)–(7)]

아래의 \(\sigma\) 표기는 spin-conserving 기저를 전제한다. 이때 NEGF 표현에서 \(\alpha\ne\beta\)이면

\[
T_{\alpha\beta,\sigma}(E)
=\operatorname{Tr}\!\left[
G^r_\sigma(E)\Gamma_{\alpha,\sigma}(E)
G^a_\sigma(E)\Gamma_{\beta,\sigma}(E)
\right]
\]

로 쓸 수 있다. 여기서 \(G^a=(G^r)^\dagger\), \(\Gamma_\alpha=i(\Sigma_\alpha^r-\Sigma_\alpha^a)\)이다. 횡방향 주기계에서는 이 transmission을 Brillouin zone 가중치로 평균한다. spin-mixing이 있으면 \(\sigma\)별 식 대신 전체 spinor 기저에서 모든 입사·출사 spin을 합한 \(T_{\alpha\beta}\)를 사용한다. [1, §IV.A, 식 (24)–(25); 5, §II; 6, §2]

## 2. 다중 전극 전하 전류

\(J_\alpha^N\)를 전극 \(\alpha\)에서 중심영역으로 들어오는 전자 입자 유량으로 정한다. 그러면

\[
J_\alpha^N
=\frac{1}{h}\sum_\sigma\sum_{\beta=1}^{M}
\int dE\,
\left[
T_{\alpha\beta,\sigma}(E)f_\alpha(E)
-T_{\beta\alpha,\sigma}(E)f_\beta(E)
\right]
\]

이다. 전자의 전하가 \(-e\)이고 \(e>0\)이므로, 위 전자 유량에 \(+e\)를 곱한 \(I_\alpha=eJ_\alpha^N\)는 관례적인 양전하 전류와 반대 방향이다. 다른 부호 규약을 쓴 자료와 비교할 때는 이 정의부터 맞춰야 한다. [2, 식 (1a)와 부호 정의; 3, 식 (1); 4, 식 (2)–(4)]

전체 전류 \(\sum_\alpha J_\alpha^N=0\)은 위 식에서 유입·유출 항의 전극 인덱스를 바꾸면 바로 얻는다. 추가로 unitary scattering matrix를 전제하면 각 전극에 대해 전체 유출 transmission과 전체 유입 transmission이 같다. 그러므로 모든 \(\mu_\alpha\)와 \(\Theta_\alpha\)가 같을 때에도 각 전극 전류가 0이 된다. 자기장이 있을 때 일반적으로 \(T_{\alpha\beta}(B)=T_{\beta\alpha}(B)\)라고 둘 수는 없으며, spin을 합산한 transmission에서는 미시적 시간반전 관계에 따라 자기장과 자화처럼 시간반전에 홀수인 변수를 함께 반전해 \(T_{\alpha\beta}(B)=T_{\beta\alpha}(-B)\)의 관계를 쓴다. [1, §IV.A, 식 (25)–(27); 3, 식 (1)–(4); 4, 식 (4)]

## 3. 에너지·열 전류와 에너지 보존

같은 부호 규약에서 전극 \(\alpha\)에서 중심영역으로 들어오는 에너지 전류와 열 전류는

\[
J_\alpha^E
=\frac{1}{h}\sum_\sigma\sum_{\beta}
\int dE\,E
\left[T_{\alpha\beta,\sigma}f_\alpha
-T_{\beta\alpha,\sigma}f_\beta\right],
\qquad
J_\alpha^Q=J_\alpha^E-\mu_\alpha J_\alpha^N
\]

로 정의한다. 정상상태 탄성 수송에서는 \(\sum_\alpha J_\alpha^E=0\)이지만, 유한 바이어스에서는 \(\sum_\alpha J_\alpha^Q=-\sum_\alpha\mu_\alpha J_\alpha^N\)가 일반적으로 0이 아니다. 열 전류는 각 reservoir의 화학 퍼텐셜을 뺀 에너지 흐름이므로, 기준을 명시하지 않은 ‘에너지 전류’와 바꾸어 쓰면 안 된다. [2, 식 (1a)–(1b)와 부호 정의; 4, 식 (2)–(7)]

## 4. 선형 전기·열전 응답

양의 공통 평형 온도 \(\Theta>0\)에서 \(\mu_\alpha=\mu+\delta\mu_\alpha\), \(\Theta_\alpha=\Theta+\delta\Theta_\alpha\)라고 하자. 이 절의 transmission은 이 평형점에서 평가한다. 1차까지 Fermi 분포는

\[
f_\alpha(E)=f_0(E)
-\frac{\partial f_0}{\partial E}
\left[
\delta\mu_\alpha+\frac{E-\mu}{\Theta}\delta\Theta_\alpha
\right]+O(\delta^2)
\]

로 전개된다. \(B=0\)이고 \(T_{\alpha\beta}=T_{\beta\alpha}\)인 경우, \(V_\alpha=\delta\mu_\alpha/e\)를 써서 전하 전류를

\[
I_\alpha
=\sum_{\beta\ne\alpha}
\left[
\mathcal{G}_{\alpha\beta}(V_\alpha-V_\beta)
+\mathcal{L}_{\alpha\beta}(\delta\Theta_\alpha-\delta\Theta_\beta)
\right]
\]

로 쓸 수 있다. 이때

\[
\mathcal{G}_{\alpha\beta}
=\frac{e^2}{h}\sum_\sigma\int dE\,
T_{\alpha\beta,\sigma}(E)
\left(-\frac{\partial f_0}{\partial E}\right),
\quad
\mathcal{L}_{\alpha\beta}
=\frac{e}{h\Theta}\sum_\sigma\int dE\,
(E-\mu)T_{\alpha\beta,\sigma}(E)
\left(-\frac{\partial f_0}{\partial E}\right)
\]

이다. \(\mathcal{G}\)는 전기적 응답, \(\mathcal{L}\)은 온도차가 만드는 전류를 나타낸다. 같은 1차 근사에서 열 전류는

\[
J_\alpha^Q
=\sum_{\beta\ne\alpha}
\left[
\Theta\mathcal{L}_{\alpha\beta}(V_\alpha-V_\beta)
+\mathcal{K}_{\alpha\beta}(\delta\Theta_\alpha-\delta\Theta_\beta)
\right],
\qquad
\mathcal{K}_{\alpha\beta}
=\frac{1}{h\Theta}\sum_\sigma\int dE\,
(E-\mu)^2T_{\alpha\beta,\sigma}(E)
\left(-\frac{\partial f_0}{\partial E}\right)
\]

로 쓸 수 있다. 이 식에서 \(J_\alpha^Q=J_\alpha^E-\mu_\alpha J_\alpha^N\)의 \(\mu_\alpha\)를 \(\mu\)로 바꾸어도 1차 응답은 변하지 않는다. \((\mu_\alpha-\mu)J_\alpha^N\)가 2차이기 때문이다. 자기장이 있거나 전송의 방향 대칭을 쓰지 않을 때에는 이 차이 형태 대신 전류식 전체를 선형화한 conductance 행렬을 사용해야 한다. [2, 식 (2)–(3); 4, 식 (2)–(7); 5, §II]

공통 전압을 모든 전극에 더해도 선형 전류가 바뀌지 않으려면 conductance 행렬의 각 행의 합이 0이어야 한다. 전체 전류 보존은 각 열의 합이 0이라는 별도 조건으로 나타난다. 유한 바이어스에서 transmission과 중심영역 전위가 바이어스에 의존하면, gauge covariance는 전극 전압과 내부 전위를 함께 이동했을 때 관측 전류가 변하지 않도록 요구한다. self-consistent 전위 계산은 이를 구현하는 한 방법이다. 반면 0 V transmission을 고정하는 근사는 물리적인 전위 재배열을 빠뜨릴 수 있다는 문제이며, 에너지 기준과 transmission을 함께 이동하는 단순 좌표변환의 gauge invariance와는 구별해야 한다. [3, 식 (1)–(4); 2, 식 (4)–(6)]

## 5. Probe 전극이 나타내는 것

추가 전극 \(p\)를 voltage probe로 쓸 때는 보통 주어진 \(\Theta_p\)에서 적분된 입자 유량 \(J_p^N=0\)이 되도록 \(\mu_p\)를 정한다. 이는 probe와의 순 전하 교환이 없다는 경계조건이며, \(J_p^Q=0\)을 뜻하지는 않는다. 에너지마다 \(J_p^N(E)=0\)을 강제하는 dephasing probe와도 구별해야 한다. 두 조건은 위상 손실과 에너지 교환을 서로 다르게 모형화한다. [5, §II; 4, isothermal case]

probe의 화학 퍼텐셜과 온도를 모두 미지수로 두고 \(J_p^N=J_p^Q=0\)을 풀면 thermoelectric probe 또는 voltage–temperature probe가 된다. 이 조건은 ‘국소 전압’이나 ‘국소 온도’를 직접 측정한 값이 아니라, 약결합된 이상 probe 모형이 만족하는 값으로 해석해야 한다. [4, 식 (2)–(10) 및 adiabatic case; 6, 초록 및 §II]

## 6. 적용 범위와 계산 점검

- 각 전극의 \(\mu_\alpha\), \(\Theta_\alpha\), 전송 인덱스 방향, 전자 유량 또는 양전하 전류의 부호, 스핀과 \(k\)-점 평균의 포함 방식을 함께 기록한다.
- 수치적으로는 \(\sum_\alpha J_\alpha^N\)과, 계산 범위 안에서 \(\sum_\alpha J_\alpha^E\)가 0인지 확인한다. 이 검사는 energy mesh, \(k\)-점, 전극 self-energy, 중심영역 길이의 수렴을 대신하지 않는다.
- 전자–포논·전자–전자 상호작용, 비탄성 산란, 강한 상관을 포함하면 적절한 \(\Sigma_\mathrm{int}^{r,<,>}\)와 그에 맞는 전류식을 사용해야 한다. probe는 이 물리를 하나의 경계조건으로 대체하는 모형이지 미시적 산란 기작의 증명은 아니다.
- 비선형 바이어스에서의 charge conservation, gauge invariance, 계산 수렴, 특정 exchange–correlation 근사의 물리적 타당성은 서로 다른 검증 대상이다.

## 7. 참고 자료

1. N. Papior, N. Lorente, T. Frederiksen, A. García, M. Brandbyge, “Improvements on non-equilibrium and transport Green function techniques: the next-generation transiesta,” *Computer Physics Communications* **212**, 8–24 (2017), [§IV.A, 식 (24)–(31)](https://arxiv.org/pdf/1607.04464).
2. J. Meair, P. Jacquod, “Scattering Theory of Nonlinear Thermoelectricity in Quantum Coherent Conductors,” *Journal of Physics: Condensed Matter* **25**, 082201 (2013), [식 (1)–(6)](https://arxiv.org/pdf/1211.5583).
3. T. Christen, M. Büttiker, “Gauge invariant nonlinear electric transport in mesoscopic conductors,” *Europhysics Letters* **35**, 523–528 (1996), [식 (1)–(4)](https://arxiv.org/pdf/cond-mat/9604029).
4. D. Sánchez, L. Serra, “Thermoelectric transport of mesoscopic conductors coupled to voltage and thermal probes,” *Physical Review B* **84**, 201307(R) (2011), [식 (2)–(10)](https://arxiv.org/pdf/1107.3576).
5. H. Förster, P. Samuelsson, S. Pilgram, M. Büttiker, “Voltage and dephasing probes: a full counting statistics discussion,” *Physical Review B* **75**, 035340 (2007), [§II](https://arxiv.org/pdf/cond-mat/0609544).
6. A. Shastry, C. A. Stafford, “Temperature and voltage measurement in quantum systems far from equilibrium,” *Physical Review B* **94**, 155433 (2016), [§II](https://arxiv.org/pdf/1603.00096).
7. H. Ness, L. K. Dash, R. W. Godby, “Generalization and applicability of the Landauer formula for non-equilibrium current in the presence of interactions,” *Physical Review B* **82**, 085426 (2010), [§II, 식 (4)](https://arxiv.org/pdf/1007.1104).
