# 품질 근거: electronic-structure-solvers.md

- 대상 문서: docs/computational-science/atomistic-simulation/electronic-structure-solvers.md
- 검토 범위: 신규 문서 전체
- 목적: OMM, PEXSI, ELSI, CheSS의 서로 다른 알고리즘·인터페이스 역할을 Order-N DFT 및 block-stitching 수송과 구분한다.
- 문서 SHA-256: 4e5b996ed7aa843e6f18f8083a515a52d3c82a81b53d99657706a619e5fbb4c6
- 검증 기록 SHA-256: registry에서 추적

## 주장과 근거

1. **SIESTA의 OMM, historical Order-N, PEXSI, ELSI와 CheSS는 동일한 solver를 가리키지 않는다.**
   - 범위: SIESTA 5.4의 electronic-structure solver 설명과 구현 주의.
   - 판정: supported.
   - 출처: SIESTA 5.4 reference manual, “Calculation of the electronic structure,” “SolverOMM,” “SolverON,” “SolverPEXSI,” “SolverELSI,” “SolverCheSS”; ELSI 2018 paper.
2. **ELSI는 host electronic-structure code와 solver library를 잇는 software interface이며, 선택된 backend가 numerical method를 결정한다.**
   - 범위: ELSI interface 및 solver-family 지원.
   - 판정: supported.
   - 출처: ELSI 2018 paper; ELSI 2020 paper.
3. **PEXSI는 pole expansion과 selected inversion으로 희소 matrix function/density matrix를 구하고, 이점은 입력 행렬 구조 및 parallel setting에 의존한다.**
   - 범위: PEXSI electronic-structure use; universal O(N) 또는 guaranteed speedup을 주장하지 않는다.
   - 판정: supported.
   - 출처: PEXSI official introduction; Lin et al. (2013).
4. **CheSS는 sparse matrix functions를 Chebyshev polynomial로 계산하는 library이며 SIESTA 5.4 integration은 experimental로 표시된다.**
   - 범위: density matrix and related matrix functions.
   - 판정: supported.
   - 출처: Mohr et al. (2017); SIESTA 5.4 reference manual, “SolverCheSS.”
5. **이 solver families는 이미 계산한 channel block 반복이나 RGF 수송 자체가 아니다.**
   - 범위: 전체 구조의 KS electronic-structure solution과 open-boundary device transport의 계산 목표 차이.
   - 판정: supported.
   - 출처: SIESTA 5.4 reference manual; ELSI 2020 paper; SIESTA TBtrans guide.

## 가정과 한계

- SIESTA implementation claims are explicitly versioned to 5.4.
- Scaling is not generalized from solver names alone; basis sparsity, matrix graph, problem size, k-points, memory and parallel resources remain relevant.
- No performance benchmark or electronic-structure calculation was run for this wiki update.

## 그림과 표현

- solver-and-transport-roles.svg is an original conceptual diagram; it distinguishes the self-consistent KS path from block-extension transport and labels ELSI as an interface.
- editable source: refs/quality/figure-source/solver-and-transport-roles.html
- SVG and HTML hashes are stored in registry.
- diagram-design self_check.py --offline passed and Inkscape PNG rendering was inspected.

## 독립 검토

- solver-source audit and independent basis/solver page review checked algorithm identities, version limits and block-stitching boundary.
- humanizer review comments were applied without changing the technical distinctions.
