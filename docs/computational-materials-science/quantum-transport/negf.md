---
description: 정상상태 NEGF에서 전극 self-energy, Green 함수, 전하밀도와 전류를 연결한다.
---

# Non-equilibrium Green's function (NEGF)

Non-equilibrium Green's function (NEGF)은 개방된 양자계에서 전극의 점유와 결합을 경계조건으로 넣어 전하밀도와 전류를 구하는 틀이다. 이 글은 정상상태의 두 전극 소자를 대상으로 하며, 전극은 비상호작용 평형 reservoir, 중심영역은 유한한 기저로 기술한다고 둔다. Landauer 전송식은 이 틀의 탄성·단일입자 극한에서 얻어지는 결과로 다룬다. 시간 의존 구동, 강한 상관, 그리고 유한한 전극 자체의 비평형은 여기서 유도하지 않는다. [1, §2; 2, §§II–III; 3, §1]

## 1. 소자와 전극의 분할

전체 계를 왼쪽 전극 \(L\), 중심영역 \(C\), 오른쪽 전극 \(R\)로 나눈다. 각 전극은 자체 화학 퍼텐셜 \(\mu_\alpha\)와 온도 \(\Theta_\alpha\)를 가진 평형 분포

\[
f_\alpha(E)=\frac{1}{1+\exp[(E-\mu_\alpha)/(k_B\Theta_\alpha)]}
\]

를 유지한다고 가정한다. 중심영역에는 산란이 일어나는 부분과 전극–소자 접합 근처의 screening을 나타낼 만큼의 원자층을 포함해야 한다. 이 분할은 계산 편의를 위한 것이지만, 너무 짧은 중심영역은 전극의 평형 가정과 계산 결과를 분리할 수 없게 한다. [1, §II; 3, §1; 4, p. 3]

국소 원자 궤도처럼 비직교 기저를 쓰면 중심영역의 Hamiltonian \(H_C\)와 overlap 행렬 \(S_C\)를 함께 보존해야 한다. 복소 에너지 \(z=E+i0^+\)에서 retarded Green 함수는

\[
G^r(E)=\left[zS_C-H_C-\sum_{\alpha=L,R}\Sigma_\alpha^r(E)\right]^{-1}
\]

이다. \(\Sigma_\alpha^r\)는 무한 전극을 유한 중심영역에 접속한 효과를 나타내는 retarded self-energy이다. 전극 표면 Green 함수 \(g_\alpha^r\)와 결합 \(\tau_{C\alpha}(z)=H_{C\alpha}-zS_{C\alpha}\), \(\tau_{\alpha C}(z)=H_{\alpha C}-zS_{\alpha C}\)를 쓰면

\[
\Sigma_\alpha^r(E)=\tau_{C\alpha}(z)g_\alpha^r(E)\tau_{\alpha C}(z)
\]

로 쓸 수 있다. 실축의 retarded 극한에서는 \(\tau_{\alpha C}(E+i0^+)=\tau_{C\alpha}(E-i0^+)^\dagger\)이므로, 같은 복소 \(z\)에서 단순 켤레전치를 취하는 것으로 바꾸면 안 된다. 비직교 기저에서는 \(zS\)와 \(H\)를 분리해 놓거나 결합에서 overlap 항을 빠뜨리면 같은 물리계를 표현하지 못한다. [2, §VI.C, 식 (102)–(103), (117)–(119); 3, NEGF equations]

## 2. 전극 결합과 상태의 폭넓이

전극 \(\alpha\)가 만드는 broadening 행렬은

\[
\Gamma_\alpha(E)=i\left[\Sigma_\alpha^r(E)-\Sigma_\alpha^a(E)\right],
\qquad \Sigma_\alpha^a=(\Sigma_\alpha^r)^\dagger
\]

로 정의한다. \(\Gamma_\alpha\)는 중심영역의 상태가 전극 \(\alpha\)로 열려 있는 정도를 나타내며, 단순한 국소 density of states나 고립된 소자의 고유상태와 같지 않다. [1, 식 (2)–(3); 2, §VI.C; 3, NEGF equations]

spectral function은 \(A=i(G^r-G^a)\), \(G^a=(G^r)^\dagger\)이다. 중심영역의 모든 감쇠가 전극에서 오고, 전극과 완전히 분리된 bound state가 없으며 \(0^+\to0\) 극한을 취할 때에는

\[
A(E)=G^r(E)[\Gamma_L(E)+\Gamma_R(E)]G^a(E)
\]

가 성립한다. 이 식은 상태가 존재할 수 있는 에너지 구조를 말할 뿐 점유를 뜻하지 않는다. bound state가 있으면 전극 self-energy만으로 그 점유가 유일하게 정해지지 않을 수 있으므로, 위 등식과 아래의 점유식에 그 예외를 그대로 적용해서는 안 된다. [1, 식 (2)–(3), (6), §III.B; 2, §VI.C; 5, 초록 및 §§II–IV]

## 3. Lesser Green 함수와 전하밀도

비상호작용 전극에서 오는 lesser self-energy는

\[
\Sigma_\alpha^<(E)=i f_\alpha(E)\Gamma_\alpha(E)
\]

이다. 중심영역에 별도 상호작용 self-energy가 없고 bound state의 초기 점유 문제가 없으면 Keldysh 식은

\[
G^<(E)=G^r(E)\,[\Sigma_L^<(E)+\Sigma_R^<(E)]\,G^a(E)
\]

가 된다. 이 식에서 \(G^r\)은 허용된 상태와 전극 결합을, \(\Sigma^<\)는 각 전극이 공급하는 점유를 함께 넣는다. [1, 식 (4), §III.B; 2, §VI.C; 3, NEGF equations]

single-particle density matrix는

\[
\rho=-i\int_{-\infty}^{\infty}\frac{dE}{2\pi}\,G^<(E)
\]

로 얻는다. 비직교 기저에서 중심영역 기저에 사영한 전자 수는 \(\rho\)의 대각합으로 읽지 않고 \(N_C=\operatorname{Tr}(\rho S_C)\)로 계산한다. 원자별 population은 전극–중심 경계 overlap을 어떻게 나누는지에 따라 추가 규약이 필요할 수 있다. 전자밀도가 Hamiltonian 또는 전위에 되먹임되는 DFT-NEGF·Poisson-NEGF 계산은 이 \(\rho\)를 사용한 self-consistency가 수렴할 때까지 반복한다. 수렴은 전류 보존이나 모델의 물리적 타당성과 별개의 검사 대상이다. [2, §VI.D, 식 (121)–(122); 3, NEGF equations; 4, pp. 8–10]

## 4. 전류와 Landauer 극한

\(L\to C\) 방향의 전자 입자 유량에 \(+e\)를 곱한 양을 \(I_L\)로 정하면, 일반적인 Keldysh 전류식은

\[
I_L=\frac{e}{h}\int dE\,\operatorname{Tr}
\left[\Sigma_L^<(E)G^>(E)-\Sigma_L^>(E)G^<(E)\right]
\]

처럼 쓸 수 있다. 여기서 \(e>0\), \(h\)는 Planck 상수이며, \(G^>\), \(\Sigma^>\)는 greater Green 함수와 self-energy이다. \(G^>-G^<=G^r-G^a\), \(\Sigma_L^<=if_L\Gamma_L\), \(\Sigma_L^>=-i(1-f_L)\Gamma_L\)를 쓰면 Jauho–Wingreen–Meir의 lead current 식으로 바꿀 수 있다. 전자의 실제 전하는 \(-e\)이므로 이 \(I_L\)의 방향은 관례적인 양전하 전류와 반대다. 다른 자료는 전류 방향이나 전하 부호를 다르게 정할 수 있으므로, 식을 비교할 때 부호 관례를 먼저 맞춰야 한다. [6, 식 (18)–(19); 2, §VI.D, 식 (126)–(127)]

중심영역이 탄성·단일입자 문제이고 전극만이 점유와 감쇠를 제공하면, 위 식은

\[
I=\frac{e}{h}\int dE\,T(E)[f_L(E)-f_R(E)],
\qquad
T(E)=\operatorname{Tr}[\Gamma_LG^r\Gamma_RG^a]
\]

로 줄어든다. 이때 \(I\)는 위에서 정의한 \(L\to C\) 방향 전자 유량과 같은 부호로 잡았고, spin이 기저와 trace에 이미 포함되어 있으면 별도 2를 곱하지 않는다. 횡방향 주기계에서는 각 \(k\)-점의 \(T(E,k)\)를 Brillouin zone 가중치로 평균한 뒤 적분한다. 이 Landauer 표현의 적용 범위와 선형 응답은 [Landauer transport and transmission](landauer-transmission.md)에서 이어서 다룬다. [1, §IV.A, 식 (30); 4, §V, 식 (42)–(44); 2, §VI.D]

## 5. 상호작용, bound state와 계산의 한계

전자–포논 또는 전자–전자 상호작용을 포함하면 \(\Sigma_\mathrm{int}^{r,<,>}\)가 \(G\)와 전류식에 추가된다. 이 경우 \(G^<\)에는 전극 항뿐 아니라 \(\Sigma_\mathrm{int}^<\)가 들어가며, 단순한 \(T=\operatorname{Tr}[\Gamma_LG^r\Gamma_RG^a]\) 하나가 항상 전체 전류를 나타내지는 않는다. 근사 self-energy를 쓸 때는 어떤 산란 기작과 diagram 또는 self-consistent 절차를 포함했는지 밝혀야 한다. [6, §§II–III; 7, 초록 및 §II]

전극과 분리된 bound state는 별도의 경계 사례다. 연속 상태의 density는 lead self-energy로 정할 수 있지만, 평형화 기작이 없으면 bound state의 density matrix는 초기 조건 또는 약하게 도입한 보조 reservoir에 의존할 수 있다. 따라서 계산에서 매우 좁은 공명, 전극 결합이 0인 상태, 혹은 비정상적인 charge가 나타나면 에너지 mesh를 미세화하는 것만으로 해결됐다고 판단하지 말고 해당 상태의 점유 규칙을 따로 확인해야 한다. [5, 초록 및 §§III–V; 2, §IV; 3, §2]

## 6. 계산 결과를 읽을 때

- \(H\), \(S\), 전극 self-energy, 화학 퍼텐셜, 온도, 전류 부호와 스핀 처리의 규약을 함께 기록한다.
- 유한 바이어스에서는 실제 바이어스에서 얻은 전위·전하밀도·Green 함수를 썼는지, 0 V Hamiltonian을 고정하는 근사를 썼는지 구별한다.
- 좌우 전극 전류의 합, energy mesh·contour·횡방향 \(k\)-점, 중심영역 길이를 각각 수렴 검사한다. 이 절차는 수치적 일관성을 검사할 뿐 특정 exchange–correlation 근사나 전극 모형의 물리적 적합성을 증명하지 않는다.
- 이 글의 식은 정상상태 열린계의 전자 수송을 위한 것이다. transient, 열수송, 강한 비평형 전극, 비보존 근사는 별도의 formalism과 검증이 필요하다.

## 7. 참고 자료

1. N. Papior, N. Lorente, T. Frederiksen, A. García, M. Brandbyge, “Improvements on non-equilibrium and transport Green function techniques: the next-generation transiesta,” *Computer Physics Communications* **212**, 8–24 (2017), [§2, 식 (1)–(4)](https://arxiv.org/pdf/1607.04464).
2. R. K. Lake, R. R. Pandey, “Non-Equilibrium Green Functions in Electronic Device Modeling” (2006), [§VI.C, 식 (102)–(103), (117)–(120); §VI.D, 식 (121)–(122), (126)–(135)](https://arxiv.org/pdf/cond-mat/0607219).
3. SIESTA developers, “[NEGF equations](https://docs.siesta-project.org/projects/siesta/en/5.4/reference/siesta.html#negf-equations),” SIESTA 5.4 Reference Manual, 확인일 2026-10-28.
4. M. Brandbyge, J.-L. Mozos, P. Ordejón, J. Taylor, K. Stokbro, “Density-functional method for nonequilibrium electron transport,” *Physical Review B* **65**, 165401 (2002), [§II 및 §V, 식 (42)–(44)](https://arxiv.org/pdf/cond-mat/0110650).
5. A. Dhar, D. Sen, “Non-equilibrium Green's function formalism and the problem of bound states,” *Physical Review B* **73**, 085119 (2006), [§§II–V](https://arxiv.org/pdf/cond-mat/0510303).
6. A.-P. Jauho, N. S. Wingreen, Y. Meir, “Time-dependent transport in interacting and noninteracting resonant-tunneling systems,” *Physical Review B* **50**, 5528–5544 (1994), [식 (18)–(19)](https://arxiv.org/pdf/cond-mat/9404027).
7. H. Ness, L. K. Dash, R. W. Godby, “Generalization and applicability of the Landauer formula for non-equilibrium current in the presence of interactions,” *Physical Review B* **82**, 085426 (2010), [§II, 식 (4)](https://arxiv.org/pdf/1007.1104).
