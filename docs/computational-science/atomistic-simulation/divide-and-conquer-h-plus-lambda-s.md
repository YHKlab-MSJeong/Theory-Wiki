---
description: Hamiltonian stitching과 fragment 기반 D&C-DFT를 구분하고 비직교 기저의 H+λS 에너지 이동을 설명한다.
---

# Divide-and-conquer의 두 의미와 \(H+\lambda S\)

> 상태: 확인 중 — 출처별 주장 검토 및 독립 과학 검토가 완료되기 전에는 게시하지 않는다.

## 1. 서로 다른 두 가지 divide-and-conquer

**Hamiltonian stitching**에서는 작은 구조의 onsite·hopping 행렬 블록을 복제하거나 연결해 큰 장치의 \(H\) 및 비직교 기저라면 \(S\)를 구성한다. 이어 조립된 행렬로 고유값 문제 또는 NEGF 수송을 계산한다. [1, §§II.C–D] 이는 큰 장치 전체에 대해 Kohn–Sham 자기일관 DFT 계산을 수행했다는 뜻이 아니다.

**Fragment 기반 divide-and-conquer DFT (D&C-DFT)**에서는 공간적으로 분할된 부분계의 전자밀도 또는 밀도행렬을 근사적으로 결합해 전체 밀도를 얻고, 이를 이용해 전체 유효 퍼텐셜을 갱신한다. Yang의 초기 전자밀도 분할과 Yang–Lee의 밀도행렬 분할은 이 계열이다. [2, Abstract; 3, Abstract; 4, Abstract] 큰 계의 전자구조를 부분계별로 계산한다는 목표는 비슷하지만, 단순히 행렬을 이어 붙이는 작업과는 알고리즘 및 자기일관성이 다르다.

| 비교 항목 | Hamiltonian stitching | Fragment D&C-DFT |
|---|---|---|
| 결합 대상 | \(H,S\)의 국소 행렬 블록 | 부분계의 밀도·밀도행렬 및 전역 퍼텐셜 |
| 전자구조 계산 | 미리 얻은 블록을 조립하고 재사용 가능 | 부분계 전자구조를 반복적으로 갱신 |
| 장거리 정전기 | 블록 재사용만으로 자동 해결되지 않음 | 전체 밀도에서 장거리 Coulomb 퍼텐셜을 갱신하는 구현 가능 |
| 적용 사례 | Hod 등 (2006)의 긴 분자 수송 | Yang (1991), Yang–Lee (1995), LS3DF |

두 방식을 같은 D&C라는 단어만으로 동일시하지 않는다. 관련 문서: [Hod 등의 수송 분할](../../computational-materials-science/quantum-transport/hod-divide-and-conquer.md).

## 2. \(H+\lambda S\)의 의미

비직교 기저 \(\{\phi_\mu\}\)에서

\[
H_{\mu\nu}=\langle\phi_\mu|\hat H|\phi_\nu\rangle,\qquad
S_{\mu\nu}=\langle\phi_\mu|\phi_\nu\rangle
\]

이고 일반화 고유값 문제는 \(Hc=\varepsilon Sc\)이다. 물리적 연산자에 공간적으로 **일정한** 에너지 \( \lambda \)만큼 항등 연산자를 더하면

\[
\hat H'=\hat H+\lambda\hat I,\qquad
H'=H+\lambda S,\qquad
H'c=(\varepsilon+\lambda)Sc
\]

가 된다. \(\lambda\)는 에너지 단위를 갖고, 부호는 \(H'=H+\lambda S\)라는 정의에 따른다. 기저가 직교하면 \(S=I\)여서 통상적인 대각 이동 \(H+\lambda I\)가 된다. 이 결과는 비직교 기저의 정의에서 직접 얻어지는 선형대수 관계이며 특정 D&C 구현에 종속되지 않는다. [5, §Hamiltonian parameterization and Eq. (3); 6, §Matrix elements of Hamiltonian and overlap]

### (1) DeePTB-NEGF의 식 (3)

DeePTB-NEGF 논문은 주기 학습 구조와 개방 경계 장치 영역 사이의 에너지 기준 차이를 다루면서

\[
H'=H+\lambda S
\]

를 도입한다. 저자들은 \(\lambda\)를 학습 과정에서 DeePTB 예측 및 DFT 참조 Hamiltonian 블록을 비교해 정한다고 설명한다. 이는 **전역 전위 또는 기준 에너지의 일정한 offset을 맞추는 자유도**이지, 임의의 위치 의존 Hartree 퍼텐셜이나 장치 전하 재분포를 스스로 생성하는 절차가 아니다. [5, Eq. (3) and surrounding text]

### (2) 바이어스 및 전위 정렬과 구별

\(H\)에 일정한 \(\lambda S\)를 더하면서 에너지축과 전극 화학퍼텐셜도 동일한 기준으로 변환하면 관측 가능한 수송은 변하지 않아야 한다. 반면 **장치에만** \(+\lambda S\)를 더하고 전극의 기준을 고정하면 상대 band alignment와 transmission이 변할 수 있다. 이때는 단순 표기 변경이 아니라 물리적 정렬 가정이 달라진다. 위치 의존 퍼텐셜 \(V(\mathbf r)\)은 일반적으로

\[
\Delta H_{\mu\nu}=
\langle \phi_\mu|V(\mathbf r)|\phi_\nu\rangle
\]

이며, \(V(\mathbf r)=\lambda\)일 때에만 \(\lambda S_{\mu\nu}\)로 단순화된다. 따라서 \(H+\lambda S\) 하나로 Poisson 자기일관성이 구현된다고 말할 수 없다. 이 부분은 정의로부터의 직접 유도이며 구체적인 장치 사례에서는 별도 검증이 필요하다.

## 3. Fragment D&C-DFT와 global Poisson

전역 전자밀도를 부분계 \(\alpha\)의 밀도에서 조합하는 한 가지 형태는

\[
\rho(\mathbf r)=\sum_\alpha w_\alpha(\mathbf r)\rho_\alpha(\mathbf r),
\qquad \sum_\alpha w_\alpha(\mathbf r)=1
\]

이다. \(w_\alpha\)는 겹치는 조각의 중복 계산을 조정하는 분할 가중치다. 밀도행렬 기반 구현에서는 기저 블록에 대응하는 분할 규칙을 사용한다. 모든 D&C-DFT가 위의 동일한 가중 함수 또는 buffer 구현을 사용하는 것은 아니다. [2, Abstract; 3, Abstract; 7, D&C lecture]

국소 조각의 계산만 반복한다고 전역 Coulomb 상호작용이 사라지는 것은 아니다. LS3DF 등은 장거리 정전기를 다루기 위해 전체 시스템에 대해 Poisson 방정식을 풀면서 비용이 큰 양자역학 계산은 조각별로 나누어 처리한다. [4, discussion of global Poisson; 8, §III LS3DF algorithm] 이때의 **global Poisson**은 D&C-DFT의 특정 구현 전략을 설명하며, Hod식 조립이나 DeePTB의 \(\lambda S\)에 일반적으로 포함되는 단계는 아니다.

## 4. 어느 접근을 선택할 것인가

- 긴 주기 채널에서 **고정된 국소 행렬 블록**을 재사용하고 싶다면 stitching을 생각한다. 접촉·결함·strain에 따라 onsite와 hopping이 달라지면 해당 블록의 전이성을 확인해야 한다. [1, §§II–III]
- 전체 전하 분포에 따른 **DFT 전위와 전자밀도 갱신**을 원한다면 fragment density 기반 D&C와 전역 electrostatics의 결합 여부를 살펴본다. [3, Abstract; 4, global Poisson discussion]
- DeePTB 또는 다른 학습 Hamiltonian의 **에너지 영점 차이**가 핵심이면 \(H+\lambda S\)가 해당 offset을 나타낼 수 있다. 전극·소자 기준과 \(\lambda\) 추정 방법을 검증해야 한다. [5, Eq. (3)]

어느 경우에도 'D&C를 쓴다'는 표현만으로 Hamiltonian 조립, DFT-SCF, Poisson, NEGF가 자동 수행된다고 해석하지 않는다.

## 5. 참고 자료

1. O. Hod, J. E. Peralta, G. E. Scuseria, “First-principles electronic transport calculations in finite elongated systems: A divide and conquer approach,” *J. Chem. Phys.* **125**, 114704 (2006), [§§II.C–D](https://doi.org/10.1063/1.2349482).
2. W. Yang, “Direct calculation of electron density in density-functional theory,” *Phys. Rev. Lett.* **66**, 1438 (1991), [Abstract](https://doi.org/10.1103/PhysRevLett.66.1438).
3. W. Yang, T.-S. Lee, “A density-matrix divide-and-conquer approach for electronic structure calculations of large molecules,” *J. Chem. Phys.* **103**, 5674 (1995), [Abstract](https://doi.org/10.1063/1.470549).
4. L.-W. Wang, “Divide-and-conquer quantum mechanical material simulations with exascale supercomputers,” *Natl. Sci. Rev.* **1**, 604–617 (2014), [discussion of global Poisson](https://doi.org/10.1093/nsr/nwu060).
5. J. Zou et al., “Deep learning accelerated quantum transport simulations in nanoelectronics,” *npj Comput. Mater.* **11**, 375 (2025), [Hamiltonian parameterization, Eq. (3)](https://doi.org/10.1038/s41524-025-01853-6).
6. SIESTA developers, [Hamiltonian and overlap matrix documentation](https://docs.siesta-project.org/projects/siesta/en/5.4/reference/siesta.html).
7. DFT course notes, [“Divide-and-Conquer,” §6.2, Eqs. (6.9)–(6.10)](https://www.home.uni-osnabrueck.de/apostnik/Lectures/DFT-6.pdf).
8. LS3DF authors, [“Linearly Scaling 3D Fragment Method for Large-Scale Electronic Structure Calculations,” §III](https://escholarship.org/uc/item/5zb5d4p3).
