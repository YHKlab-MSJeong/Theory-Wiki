---
description: OMM, PEXSI, ELSI와 CheSS의 전자구조 계산 역할을 Order-N 및 장채널 Hamiltonian 확장과 구분한다.
---

# 전자구조 대규모 solver의 역할

이 이름들은 대규모 전자구조 계산에서 서로 다른 역할을 한다. OMM, PEXSI와 CheSS는 Kohn–Sham 전자구조의 점유 부분공간 또는 밀도행렬을 구하는 서로 다른 알고리즘 계열이다. ELSI는 solver 자체가 아니라 여러 solver를 전자구조 코드에 연결하는 인터페이스다. 실제 계산의 지원 범위와 성능은 코드 버전, 컴파일 옵션, 기저 희소성, 원자계 크기와 계산 조건에 따라 달라진다. [1, Calculation of the electronic structure; 2, §§I–II]

![전자구조 solver와 Hamiltonian 블록 확장·수송 계산은 서로 다른 경로다. ELSI는 solver 인터페이스를 제공한다.](../../assets/solver-and-transport-roles.svg)

## 1. 네 이름은 같은 종류가 아니다

| 이름 | 역할과 기본 아이디어 | 계산 범위와 주의점 |
|---|---|---|
| **OMM** (Orbital Minimization Method) | 보조 궤도함수로 점유 부분공간을 나타내고 에너지 functional을 최소화한다. 모든 고유값·고유벡터를 먼저 구하지 않고 밀도행렬을 구성할 수 있다. | 국소화 제약을 두는지에 따라 스케일링과 근사가 달라진다. SIESTA 5.4의 SolverOMM은 전 점유 부분공간을 최적화하는 세제곱 스케일링 solver로 설명된다. 이를 과거 SIESTA Order-N 구현과 동일시하지 않는다. [1, SolverOMM; 5, §§I–III] |
| **PEXSI** (Pole EXpansion and Selected Inversion) | Fermi–Dirac matrix function을 소수의 유리함수 항으로 근사하고, 희소 행렬의 selected inversion으로 밀도행렬에 필요한 원소를 얻는다. | 전 고유상태를 모두 계산하지 않는 대안이다. 희소 행렬의 구조, 시스템 차원, pole 수와 병렬 자원에 따라 효율이 달라진다. 모든 계에서 O(N)이라고 부르거나 항상 대각화보다 빠르다고 보장하지 않는다. [1, SolverPEXSI; 3; 6] |
| **CheSS** (Chebyshev Sparse Solvers) | Chebyshev 다항식으로 희소 matrix function을 계산하는 라이브러리다. 밀도행렬, 행렬 거듭제곱, 선택 구간의 고유값 등을 대상으로 한다. | 희소성, 스펙트럼 폭과 원하는 오차가 다항식 계산량에 영향을 준다. SIESTA 5.4 설명은 CheSS 연동을 실험적 기능으로 표시한다. [1, SolverCheSS; 4] |
| **ELSI** (ELectronic Structure Infrastructure) | 전자구조 코드와 solver 라이브러리 사이의 공통 인터페이스·소프트웨어 기반이다. 코드가 지원되는 여러 solver 중 하나를 같은 API 계열로 선택하도록 연결한다. | 독립적인 수치 알고리즘 이름이 아니다. 사용 가능한 backend는 ELSI와 solver의 버전 및 빌드 옵션에 따라 달라진다. 정확도와 스케일링은 선택된 backend가 결정한다. [1, SolverELSI; 2; 5] |

이 표의 “대규모”나 “선형 스케일링”은 입력 크기가 커질수록 항상 유리하다는 약속이 아니다. 예를 들어 SIESTA 문서는 대부분의 중간 크기 계산이 대각화 또는 OMM을 사용하며 Order-N이나 PEXSI의 이점이 없을 수 있다고 설명한다. 비교할 때는 실제 기저 크기, 희소 연결, k점, 메모리, 병렬 자원과 수렴 결과를 본다. [1, Calculation of the electronic structure; 3, Introduction]

## 2. Order-N은 알고리즘 목표이지 단일 solver 이름이 아니다

선형 스케일링 DFT는 계 크기에 대한 연산량 증가를 O(N)에 가깝게 만드는 목표다. 국소화된 궤도나 희소 밀도행렬 등을 활용하는 여러 알고리즘이 이 목표를 가질 수 있지만, OMM·PEXSI·CheSS라는 이름을 붙였다고 모든 구현과 조건에서 O(N)이 되는 것은 아니다. 특히 SIESTA 5.4의 SolverOMM은 세제곱 스케일링으로 안내된다. 같은 코드의 과거 Order-N 구현과는 별도 경로다. [1, SolverOMM; SolverON; SolverPEXSI; SolverCheSS; 2, §II]

CheSS의 Chebyshev 전개 역시 Hamiltonian 블록을 채널 방향으로 늘리는 작업과 다르다. 여기서 다항식은 희소 행렬의 함수, 예를 들면 밀도행렬을 계산하기 위한 수치 기법이다. [4, Abstract and §§II–III]

## 3. 작은 Hamiltonian 블록 복제와의 차이

[Hamiltonian 블록 확장과 RGF](../../computational-materials-science/quantum-transport/hamiltonian-block-stitching.md)는 이미 계산한 실공간 H와 비직교 기저의 경우 S 블록을 principal layer 방향으로 조립해 긴 산란영역을 만드는 수송 모델이다. OMM, PEXSI, ELSI 또는 CheSS가 이 블록을 대신 복제하거나 RGF 수송을 자동으로 수행하지 않는다. [1, NEGF equations; 7, Principal layer interactions]

두 방법의 입력과 계산 목표를 분리한다.

- **전체 큰 구조의 전자상태·밀도·에너지·힘을 자기일관적으로 구한다:** 해당 코드에서 지원되는 전자구조 solver를 고른다.
- **짧은 계산에서 얻은 대표 블록으로 긴 균일 채널을 구성해 T(E)를 계산한다:** Hamiltonian 블록 구성과 NEGF/RGF를 검토한다.
- **두 접근을 연결한다:** solver로 블록을 구했더라도 복제한 영역의 환경이 같다는 가정과 장치 전위·전하의 변화를 별도로 검증한다.

## 4. 선택할 때 확인할 항목

1. 현재 코드 빌드가 해당 solver와 필요한 행렬 형식을 지원하는가?
2. 계산에서 전체 고유상태가 필요한가, 점유 밀도행렬만 필요한가?
3. 기저의 희소성·시스템 크기·k점·온도·갭 조건이 알고리즘에 맞는가?
4. 실제 병렬 자원과 메모리에서 대각화 대비 이득이 있는가?
5. 선택 solver의 밀도행렬, 전자수, 총에너지와 힘이 목표 정확도로 수렴하는가?

solver 이름 또는 예상 O(N)만으로 정확도나 실행시간을 판단하지 않는다. 작은 사례에서 동일 물리 설정의 결과와 계산량을 비교하고, 실제 크기와 관측량에서 재확인한다.

## 5. 참고 자료

1. SIESTA developers, [SIESTA 5.4 reference manual](https://docs.siesta-project.org/projects/siesta/en/5.4/reference/siesta.html), “Calculation of the electronic structure,” “SolverOMM,” “SolverON,” “SolverPEXSI,” “SolverELSI,” and “SolverCheSS.”
2. V. W. Yu et al., “ELSI—An Open Infrastructure for Electronic Structure Solvers,” *Computer Physics Communications* **256**, 107459 (2020), [arXiv:1912.13403](https://arxiv.org/abs/1912.13403).
3. PEXSI developers, [PEXSI introduction](https://pexsi.readthedocs.io/en/stable/introduction.html), overview and pole expansion.
4. S. Mohr et al., “Efficient Computation of Sparse Matrix Functions for Large-Scale Electronic Structure Calculations: The CheSS Library,” [arXiv:1704.00512](https://arxiv.org/abs/1704.00512).
5. V. W. Yu et al., “ELSI: A Unified Software Interface for Kohn–Sham Electronic Structure Solvers,” *Computer Physics Communications* **222**, 267–285 (2018), [arXiv:1705.11191](https://arxiv.org/abs/1705.11191).
6. L. Lin et al., “Accelerating Atomic Orbital-based Electronic Structure Calculation via Pole Expansion and Selected Inversion,” [arXiv:1202.2159](https://arxiv.org/abs/1202.2159).
7. SIESTA developers, [TBtrans User Guide](https://docs.siesta-project.org/projects/siesta/en/5.4/reference/tbtrans.html), “Principal layer interactions,” “Green function,” and “Calculation time.”
