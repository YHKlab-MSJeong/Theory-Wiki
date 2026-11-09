---
description: DeePTB의 Slater–Koster 적분, 국소 환경 학습과 NEGF–Poisson 수송 사례를 설명한다.
---

# DeePTB와 NEGF 수송

DeePTB는 원자 종류와 배치에서 tight-binding (TB) Hamiltonian을 구성하는 학습 모델이다. DeePTB-NEGF는 여기에 [NEGF](negf.md)를 연결하여 열린 전극 사이의 수송을 계산한다. Zou 등의 2025년 논문은 환경 의존 Slater–Koster (SK) 모형과 행렬을 직접 예측하는 모형을 모두 다루지만, 긴 탄소나노튜브(CNT) 사례에는 **DeePTB-SK**를 사용했다. 아래에서 Hamiltonian의 구조를 먼저 설명한 뒤 학습과 수송 계산을 연결한다. [1, Results “Theoretical framework and workflow” and “Application 2: CNT FET”; 2, Results]

논문의 계산 흐름과 결과는 [원문 Figure 1, 2, 5](https://doi.org/10.1038/s41524-025-01853-6)에서 볼 수 있다. 여러 접근을 비교하려면 [학습 Hamiltonian 기반 장채널 수송](ml-hamiltonian-transport.md), 정적 DFT 행렬을 직접 수송에 사용하는 방법은 [DFTH-NEGF](dfth-negf.md)를 참고한다.

## 1. Tight-binding 행렬과 SK 적분

TB는 국소 궤도 \(|i\alpha\rangle\)를 기저로 사용한다. \(i,j\)는 원자, \(\alpha,\beta\)는 원자에 붙은 궤도를 나타낸다. \(H_{i\alpha,j\beta}=\langle i\alpha|\hat H|j\beta\rangle\)에서 같은 원자에 속하는 블록은 onsite, 서로 다른 원자 사이의 원소는 hopping이라 부른다. SK 방법은 두 원자를 잇는 방향과 궤도의 각운동량 대칭을 이용해 이러한 hopping 행렬을 적은 수의 적분으로 표현한다. [2, Results “Theoretical framework of DeePTB”; 3, §III]

두 원자 사이의 단위 벡터 방향 코사인을 \((l,m,n)\)이라 하자. 실수 \(p\) 궤도 사이 결합에 대한 예는 다음과 같다.

\[
H_{p_xp_x}=l^2V_{pp\sigma}+(1-l^2)V_{pp\pi},\qquad
H_{p_xp_y}=lm(V_{pp\sigma}-V_{pp\pi}).
\]

\(V_{pp\sigma}\)와 \(V_{pp\pi}\)는 결합축에 대해 각각 \(\sigma\), \(\pi\) 대칭을 갖는 두 중심 적분으로 에너지 단위를 갖는다. 방향이 \(x\)축이면 \((l,m,n)=(1,0,0)\)이므로 \(H_{p_xp_x}=V_{pp\sigma}\), \(H_{p_yp_y}=V_{pp\pi}\), \(H_{p_xp_y}=0\)이다. 방향이 \((1/\sqrt2,1/\sqrt2,0)\)이면 \(H_{p_xp_y}=(V_{pp\sigma}-V_{pp\pi})/2\)가 된다. 같은 적분을 써도 결합 방향이 바뀌면 전역 좌표계의 행렬 원소가 바뀌는 이유다. 이는 SK 각도 규칙을 적용한 자체 예제이며 특정 물질의 계산 결과가 아니다. [2, Eqs. (1)–(2); 3, §III and Table I]

일반적으로 원자쌍 \(i,j\), 궤도 각운동량 \(l,l'\) 및 대칭 채널 \(\zeta=\sigma,\pi,\delta,\ldots\)에 대해, SK 적분 \(h_{ll'\zeta}\)를 방향에 따른 계수와 조합하여 궤도별 행렬 원소를 얻는다. 예컨대 \(s\)-\(p\)에는 \(sp\sigma\), \(d\)-\(d\)에는 \(dd\sigma,dd\pi,dd\delta\) 채널이 있다. 부호와 행렬 원소의 형태는 궤도 위상과 원자쌍 방향 규약에 따라 확인해야 한다. [2, Eqs. (1)–(2); 3, Table I]

## 2. DeePTB-SK는 무엇을 학습하나

기본적인 두 중심 SK 모형에서는 각 적분을 주로 원자 종류와 원자 사이 거리 \(r_{ij}\)의 함수로 정한다. DeePTB-SK는 같은 거리의 결합이라도 주변 원자 환경이 다르면 전자구조가 달라질 수 있도록, 국소 환경 descriptor \(\mathcal D^{ij}\)를 신경망에 입력해 적분을 보정한다. 수송 논문의 표기에서는 [1, Results “Theoretical framework and workflow”, Eq. (1); 2, Eq. (5)]

\[
h^{\mathrm{env}}_{ll'\zeta}(i,j)=h_{ll'\zeta}(r_{ij})
\left[1+\Phi^{o_i,o_j}_{ll'\zeta}(r_{ij},\mathcal D^{ij})\right].
\]

\(o_i,o_j\)는 원자 종류, \(h(r)\)는 거리 의존 기준 적분, 무차원 \(\Phi\)는 학습한 환경 보정이다. 보정은 결합별 SK 매개변수에 적용되고, 위의 방향 규칙으로 실제 행렬에 반영된다. Descriptor는 원자쌍 주변의 기하학 정보를 담는다. 모델의 cutoff 밖 원자와 학습에서 다루지 않은 장거리 전위가 자동으로 정확히 표현되는 것은 아니다. [1, Results “Theoretical framework and workflow”, Eq. (1), and Methods; 2, Results “Neural network architecture of DeePTB”]

Onsite에는 원자 궤도 에너지뿐 아니라 이웃 환경에 따른 보정도 들어갈 수 있다. 2024년 DeePTB 모델은 이웃에 따른 onsite 변형 항과 선택적인 spin–orbit coupling을 제시한다. 따라서 환경 보정이 hopping 하나에만 적용된다고 생각하면 안 된다. 사용한 궤도, cutoff, onsite 및 spin 처리는 구체적인 모델 설정을 확인해야 한다. [2, Eqs. (3)–(5)]

### (1) 학습 표적과 행렬의 관계

2025년 CNT 사례에서는 SIESTA/PBE/SZP로 얻은 zigzag \((7,0),(10,0),(13,0),(16,0)\) CNT의 밴드를 학습 자료로 쓰고 \((17,0)\) 밴드를 검증에 사용했다. 모델은 각 구조에서 Hamiltonian을 만들어 예측 고유값과 DFT 밴드의 차이를 줄이는 방향으로 매개변수를 조정한다. 학습된 모델은 더 긴 CNT의 각 원자와 원자쌍에 적용되어 행렬을 조립한다. [1, Methods “Datasets” and “Training settings”, Results “Application 2: CNT FET”]

밴드 고유값은 행렬의 모든 원소와 고유벡터를 유일하게 정하지 않는다. 그러므로 밴드가 비슷하다는 사실만으로 접촉 결합이나 \(T(E)\)가 정확하다고 결론 내릴 수 없다. 논문도 CNT의 짧은 구조에서 직접 DFT-NEGF 투과도와 비교한다. 새 접촉·결함·변형 구조에는 해당 환경을 포함한 검증이 필요하다. [1, Results “Application 2: CNT FET” and Supplementary §S4; 3, §III]

### (2) DeePTB-SK와 DeePTB-E3

| 구분 | DeePTB-SK | DeePTB-E3 |
|---|---|---|
| 표현 | SK 각도 규칙과 환경 의존 적분으로 행렬 조립 | E(3) 대칭을 고려한 신경망으로 LCAO 연산자 블록 예측 |
| 학습 자료 | CNT 사례에서는 DFT 밴드 고유값 | 2025 논문의 접합 사례에서는 DFT-NEGF의 Hamiltonian·overlap 자료 |
| 기저 | 2024 SK 모형은 직교 기저를 사용 | 논문의 LCAO 행렬은 비직교 overlap을 함께 다룬다 |
| 수송 사례 | 긴 CNT와 CNT-FET | 분자 break junction |

이 두 경로의 표적과 기저 가정을 섞으면 안 된다. 일반적인 DeePTB 기능 전체가 항상 직교 또는 항상 비직교라는 뜻도 아니다. 모델과 데이터에 따라 \(S\)가 단위행렬인지 별도로 필요한지 확인한다. [1, Results “Theoretical framework and workflow”, “Open Boundary Conditions Treatment” and applications; 2, Results “Theoretical framework of DeePTB”]

## 3. 예측 행렬을 전극에 연결하기

원자 구조에서 얻은 \(H\)와 필요한 경우 \(S\)를 전극 및 장치 블록으로 나눈다. 전극 표면 Green 함수로부터 self-energy \(\Sigma_{L,R}\)를 계산하면 coherent NEGF의 장치 Green 함수는

\[
G^r(E)=[(E+i0^+)S-H-\Sigma_L^r-\Sigma_R^r]^{-1}
\]

이며, 탄성 단일입자 모형의 투과도는 \(T(E)=\operatorname{Tr}[\Gamma_LG^r\Gamma_RG^a]\)로 구한다. \(\Gamma_\alpha=i(\Sigma_\alpha^r-\Sigma_\alpha^a)\)이다. 고정된 전위와 탄성 단일입자 모형에서의 식이며, 산란 self-energy나 전기정역학 갱신은 따로 지정해야 한다. [1, Results “NEGF formalism”, Eqs. (4)–(6); 4, §III]

전극과 장치가 동일한 기저 및 에너지 기준을 쓰는지, 결합 블록이 모델의 cutoff 안에서 제대로 포함되는지 확인해야 한다. 논문은 bulk 전극과 산란 영역의 에너지 기준 차이를 다루기 위해 \(H\to H+\lambda S\) 자유도를 도입한다. \(\lambda\)는 DeePTB-E3 접합 모형의 학습 중 예측 행렬과 DFT 행렬을 비교해 정하며, cutoff 내 전극 연장부의 환경이 bulk-like하도록 학습 구조를 준비한다. 이는 해당 접합 사례의 절차이지 모든 DeePTB 모델에 동일하게 적용된다고 가정할 수는 없다. [1, Results “Open Boundary Conditions Treatment”, Eq. (3), Fig. 2]

### (1) 게이트 FET의 Poisson 반복

CNT-FET 사례에서는 고정된 학습 Hamiltonian \(H^0\)만으로 gate 효과를 대신하지 않는다. NEGF에서 전하를 구하고 Poisson 방정식에서 전위 \(\phi\)를 구한 다음, 그 전위를 onsite에 반영해 다시 수송을 계산한다. 전자 전하의 크기를 \(e>0\), onsite 블록의 단위행렬을 \(I_i\)로 쓰면 onsite 전위 에너지의 갱신은 \(H_{ii}=H^0_{ii}-e\phi(\mathbf r_i)I_i\) 형태다. 전하와 전위가 정해진 수치 기준에 이를 때까지 반복한다. 이는 NEGF–Poisson 자기일관성이며, 반복할 때마다 Kohn–Sham DFT를 다시 푸는 것은 아니다. [1, Results “NEGF-Poisson Self-Consistency”, Eqs. (7)–(8)]

## 4. 2025년 논문에서 긴 CNT를 어떻게 다뤘나

| 사례 | 저자들이 계산한 것 | 해석할 범위 |
|---|---|---|
| 짧은 CNT | 약 9 nm 구조의 투과도를 DFT-NEGF와 비교 | 해당 구조에서의 비교이며 모든 접촉·길이의 오차를 뜻하지 않는다. |
| 긴 CNT | 최대 180 nm, 약 3만 원자 규모의 영바이어스 \(T(E)\) | 게이트 FET의 유한 전압 전류 계산과 구분한다. |
| CNT-FET | local bottom gate와 NEGF–Poisson을 적용한 최대 41 nm, 7,820원자 장치 | 18·41 nm 사례는 \(V_{DS}=0.4\) V에서 제시된다. |

CNT-FET에서는 Pd–CNT 원자 계면을 직접 표현하지 않고 도핑된 접촉으로 계면 밴드 굽힘을 모사했다. Figure 5(a)의 9 nm 직경 비교에서는 gate 일함수를 조정해 ON 전류를 맞췄으므로, 그 비교를 아무 보정 없는 독립 예측으로 읽지 않는다. [1, Results “Application 2: CNT FET”, Fig. 5(a)]

이는 논문이 보고한 크기와 조건이다. 저자들은 ballistic 모델을 사용했으며, 계산과 실험 차이에 영향을 줄 수 있는 산란과 결함 등을 논의했다. 영바이어스 \(T(E)\) 자체가 유한 바이어스 전류나 산란을 포함한 이동도는 아니다. [1, Results “Application 2: CNT FET”, Fig. 5, Discussion and Supplementary §S8]

## 5. 단순 블록 반복 및 적용 한계

[Hod 등의 D&C](hod-divide-and-conquer.md)는 주기 계산에서 얻은 동일한 가운데 \(H,S\) 블록을 여러 번 조립한다. DeePTB-SK는 긴 원자 구조를 입력받아 각 국소 환경의 SK 적분을 평가한다. 균일한 환경에서는 비슷한 블록이 반복될 수 있지만, 모델이 학습한 범위의 환경 변화에는 다른 원소가 나올 수 있다. 환경별 차이가 출력된다는 사실은 학습 범위 밖에서도 신뢰할 수 있다는 보장은 아니다. [1, Results “Theoretical framework and workflow” and applications; 2, Results; 5, §II.C]

실제로 적용할 때는 관심 에너지 창의 밴드·속도와 짧은 접촉의 \(T(E)\)를 기준 계산과 비교하고, 전극·계면·결함·변형의 원자 환경이 학습자료에 포함되는지 살핀다. 전위 정렬, cutoff, 전하 갱신, spin, 산란과 유한 전압 처리도 모델별로 별도로 정해야 한다. [1, Results “Theoretical framework and workflow” and “Application 2: CNT FET”; 4, §III]

## 6. 참고 자료

1. J. Zou et al., “Deep learning accelerated quantum transport simulations in nanoelectronics: from break junctions to field-effect transistors,” *npj Comput. Mater.* **11**, 375 (2025), [논문](https://doi.org/10.1038/s41524-025-01853-6); [소속 정정](https://doi.org/10.1038/s41524-026-01969-3).
2. Q. Gu et al., “Deep learning tight-binding approach for large-scale electronic simulations at finite temperatures with ab initio accuracy,” *Nat. Commun.* **15**, 6772 (2024), [원문](https://pmc.ncbi.nlm.nih.gov/articles/PMC11310461/).
3. J. C. Slater and G. F. Koster, “Simplified LCAO method for the periodic potential problem,” *Phys. Rev.* **94**, 1498 (1954), [원문](https://doi.org/10.1103/PhysRev.94.1498).
4. N. Papior et al., “Improvements on non-equilibrium and transport Green function techniques,” *Comput. Phys. Commun.* **212**, 8–24 (2017), [원문](https://arxiv.org/abs/1607.04464).
5. O. Hod, J. E. Peralta, G. E. Scuseria, “First-principles electronic transport calculations in finite elongated systems: A divide and conquer approach,” *J. Chem. Phys.* **125**, 114704 (2006), [원문](https://www.tau.ac.il/~odedhod/papers/paper8.pdf).
