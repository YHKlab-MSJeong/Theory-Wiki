---
description: Hod 등의 유한 긴 분자에 대한 Hamiltonian 분할·복제와 coherent 수송 계산을 설명한다.
---

# 긴 분자 수송의 Divide and Conquer: Hod 등 (2006)

Hod, Peralta, Scuseria는 양 끝이 전극에 연결되고 가운데가 반복 단위로 이루어진 긴 분자의 투과도를 계산했다. 긴 분자 전체의 전자구조를 매번 계산하는 대신, 가운데는 무한 주기 사슬에서 얻은 행렬을 반복하고 양 끝과 접촉은 별도의 작은 계산에서 얻어 조립했다. 이 논문은 [Hamiltonian 블록 확장](hamiltonian-block-stitching.md)의 구체적인 제일원리 사례다. [1, Abstract, §§II.C–D]

원문의 모형과 분할은 [Figure 1–2](https://www.tau.ac.il/~odedhod/papers/paper8.pdf)에서, 투과도 비교는 Figure 4–5에서 볼 수 있다. 아래 설명은 논문에 보고된 방법과 결과이며, 별도로 독립 재현한 계산은 아니다.

## 1. 어떤 계산을 줄이는가

이 방법에서 소자는 전극과 직접 결합하는 왼쪽 끝 \(L\), 반복 단위 \(m\)이 여러 개 있는 가운데, 오른쪽 끝 \(R\)으로 나뉜다. \(L,R\)은 **소자의 끝부분**이며 무한 전극 자체가 아니다. 전극은 별도의 반무한계로 취급한다. 반복 단위의 행렬을 \(H_m\), 이웃 단위 사이 결합을 \(H_{m,m}\)이라 하면, 중간 부분은 개념적으로 다음과 같다. [1, §II.C, Eq. (17)]

\[
H_{\mathrm{mid}}=\begin{pmatrix}
H_m&H_{m,m}&0&\cdots\\
H_{m,m}^{\dagger}&H_m&H_{m,m}&\cdots\\
0&H_{m,m}^{\dagger}&H_m&\cdots\\
\vdots&\vdots&\vdots&\ddots
\end{pmatrix}.
\]

여기에 \(H_L,H_R,H_{L,m},H_{m,R}\)을 연결한다. 논문의 국소 Gaussian 궤도는 비직교이므로 overlap \(S\)와 블록 사이 \(S_{m,m},S_{L,m},S_{m,R}\)도 함께 조립한다. 이웃 밖의 결합은 무시할 만큼 블록을 크게 잡는다. 끝부분을 충분히 길게 선택해 접촉의 영향이 반복 중앙부에서는 작다는 근사도 필요하다. [1, §§II.B–D]

두 가지 절감이 서로 다르다. **행렬 구성**에서는 긴 유한계의 전자구조를 전체적으로 다시 계산하지 않고 짧은 분자와 주기계의 DFT 결과를 재사용한다. **수송 풀이**에서는 블록 구조를 이용해 투과도에 필요한 Green 함수 성분만 계산한다. 이 방법은 전체 장치의 DFT 자기일관 계산이 아니며, 큰 구조에 대해 선형 스케일링 DFT를 수행하는 [Order-N DFT](../../computational-science/atomistic-simulation/order-n-dft.md)와 구별된다. [1, §§II.C–D; 2, §14]

## 2. 논문에서 행렬을 얻는 과정

논문의 여섯 단계는 다음과 같이 묶을 수 있다. 각 단계에서 Hamiltonian과 이에 대응하는 overlap을 얻는다. [1, §II.D]

1. **전극:** 왼쪽과 오른쪽 전극에 대해 각각 1차원 주기 DFT를 수행한다. 전극 한 셀 내부와 인접 셀 사이의 행렬로 반무한 전극의 표면 Green 함수를 계산한다. 전극이 같으면 두 번째 전극 계산은 생략할 수 있다.
2. **가운데:** 반복 단위 \(m\)의 무한 주기 사슬을 별도로 계산하여 셀 내부 \(H_m,S_m\)과 인접 셀 사이 \(H_{m,m},S_{m,m}\)을 추출한다.
3. **양 끝:** 고립된 짧은 \(L+m+R\) 분자를 계산하여 양 끝 내부 블록과 끝–중앙 결합 블록을 추출한다. \(L\)과 \(R\)을 각각 독립 분자로 계산한다는 뜻이 아니다.
4. **전극–분자 결합:** 왼쪽 전극과 짧은 분자를 포함하는 계산, 오른쪽에 대한 대응 계산을 각각 수행해 접촉 결합 블록을 얻는다. 논문에서 이 계산의 주기 방향은 긴 분자 방향에 수직이며, 주기 이미지 사이 직접 결합을 무시할 만큼 셀을 선택한다.
5. **조립과 수송:** 가운데 블록을 필요한 횟수만큼 반복해 양 끝과 연결하고, 각 전극의 self-energy를 포함해 투과도를 구한다.

양 끝의 대각 블록은 고립 분자에서 얻으므로, 전극–소자 결합 행렬을 별도로 넣더라도 접촉에 의한 양 끝의 전하·전위 재조정 전체가 자기일관적으로 포함된 것은 아니다. [1, §II.D]

다른 계산에서 얻은 블록을 결합할 때는 궤도 순서와 위상, 기저 정의 및 에너지 기준이 서로 맞는지 확인해야 한다. 이는 일반적인 조립 조건이며, 논문이 특정 에너지 정렬 알고리즘을 명시적으로 수행했다고 주장하는 것은 아니다. 접촉에 따른 밀도와 전위가 멀리까지 바뀌면 주기 사슬 블록의 대표성이 떨어질 수 있다. [1, §§II.D, III; 3, §III]

## 3. 전극과 Green 함수

에너지 \(E\)에서 \(z=E+i0^+\)로 두면 조립한 장치의 retarded Green 함수는

\[
G^r(E)=\left[zS_d-H_d-\Sigma_L^r(E)-\Sigma_R^r(E)\right]^{-1}
\]

이다. \(H_d,S_d\)는 유한 장치의 행렬이고 \(\Sigma_{L,R}^r\)은 각각 전극 표면 Green 함수와 접촉 결합으로 만든 self-energy다. 비직교 기저에서는 접촉 결합도 \(zS_{d,\alpha}-H_{d,\alpha}\)를 사용한다. 전극이 각각 소자의 왼쪽·오른쪽 끝에만 결합한다면, 투과도는 끝과 끝을 잇는 Green 함수 블록으로 표현할 수 있다. [1, §§II.A–C, Eqs. (3), (6)–(8), (16)]

\[
T(E)=\operatorname{Tr}\!\left[\Gamma_L G^r_{LR}\Gamma_R G^a_{RL}\right],\qquad
\Gamma_\alpha=i(\Sigma^r_\alpha-\Sigma^a_\alpha).
\]

여기서 \(\Gamma_L,\Gamma_R\)은 각 끝부분에 제한한 행렬이고 \(G^a_{RL}=(G^r_{LR})^\dagger\)이다. 논문은 블록 삼중대각 행렬의 재귀 관계로 필요한 \(G^r_{LR}\)을 구한다. 재귀 풀이의 조건과 비용은 [RGF 설명](hamiltonian-block-stitching.md)을 참고한다. [1, §§II.B–C, Eqs. (16)–(24); 3, §III.C]

## 4. 논문의 비교와 해석

저자들은 Al 전극 사이 trans-polyacetylene 사슬을 LDA와 최소 STO-3G 기저로 계산했다. 30개 단위 사슬을 대상으로 한 Figure 4–5에서는 \(6-6\times3-6\), 즉 양 끝 각 6개 단위와 세 번 반복한 가운데 6개 단위를 사용한 결과를 같은 길이의 직접 계산과 비교했다. 원문에 별도로 나오는 \(6+6+6=18\) 단위 구성과 혼동하지 않는다. [1, §III, Figs. 3–5]

전극 Fermi 준위 부근 1 eV 폭의 비교에서는 에너지 이동이 없는 Pearson 상관계수 \(r=0.98\)을 보고했다. 무한 사슬의 Fermi 준위 부근 0.8 eV 폭에서는 일부 피크가 이동하고, 이동을 허용한 최대 상관계수는 0.86이었다. 상관계수는 곡선 모양의 유사성을 보여 주지만 전류 오차나 모든 에너지에서의 최대 오차를 보증하지 않는다. 이는 특정 모델과 에너지 구간의 저자 보고값이다. [1, §III, Figs. 4–6]

## 5. 적용할 때 주의할 점

- **결합 범위:** 블록 밖의 \(H,S\) 결합을 자르는 오차는 블록 크기를 바꾸어 확인한다. 더 먼 결합이 크면 인접 블록만 연결한 행렬이 부적절하다. [1, §III]
- **끝의 영향:** 모든 가운데 블록을 무한 주기 사슬로 대체하면 접촉 인근의 전하 재분포와 다른 국소 환경을 놓칠 수 있다. 논문은 양 끝에 포함하는 반복 단위를 늘려 이 근사를 개선할 수 있다고 설명한다. [1, §III]
- **전압과 산란:** 논문의 식은 저전압에서 bias에 따른 \(T(E)\) 변화가 무시되고 전압 강하가 접합에 집중된다는 가정 아래 coherent conductance를 다룬다. 이를 유한 전압에서 전하·전위를 자기일관적으로 갱신한 NEGF–Poisson이나 비탄성 산란 계산으로 해석하지 않는다. [1, §II.A, Summary]
- **새 환경:** 결함이나 변형을 자동 예측하지 않는다. 학습 모델이 환경에 따라 행렬을 새로 구성하는 접근은 [DeePTB-NEGF](deeptb-negf.md)에서 비교한다. [1, §§II.C–D; 4, §§II–III]

## 6. 참고 자료

1. O. Hod, J. E. Peralta, G. E. Scuseria, “First-principles electronic transport calculations in finite elongated systems: A divide and conquer approach,” *J. Chem. Phys.* **125**, 114704 (2006), [원문](https://www.tau.ac.il/~odedhod/papers/paper8.pdf), [DOI](https://doi.org/10.1063/1.2349482).
2. J. M. Soler et al., “The SIESTA method for ab initio order-N materials simulation,” *J. Phys.: Condens. Matter* **14**, 2745 (2002), [§14](https://doi.org/10.1088/0953-8984/14/11/302).
3. N. Papior et al., “Improvements on non-equilibrium and transport Green function techniques: The next-generation TRANSIESTA,” *Comput. Phys. Commun.* **212**, 8–24 (2017), [§III](https://arxiv.org/abs/1607.04464).
4. J. Zou et al., “Deep learning accelerated quantum transport simulations in nanoelectronics,” *npj Comput. Mater.* **11**, 375 (2025), [논문](https://doi.org/10.1038/s41524-025-01853-6).
