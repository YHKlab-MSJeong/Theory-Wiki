# 품질 근거: hamgnn-negf.md

- 대상 문서: docs/computational-materials-science/quantum-transport/hamgnn-negf.md
- 검토 범위: 신규 HamGNN-NEGF 독립 문서 전체
- 목적: training matrices, Hamiltonian prediction, electrode self-energy, nonorthogonal KPM, RGF, scaling assumptions and validation limits를 설명한다.
- 출처 유형: 2026-09-29 arXiv v1 preprint; peer-reviewed publication으로 표시하지 않는다.
- 문서 SHA-256: 460a52db1467f6a1ef3701e164004008fe82ef6447ba12016ccf75bf1f9187a1
- 검증 기록 SHA-256: registry에서 추적

## 주장과 근거

1. **HamGNN-NEGF workflow는 작은 구조의 ordinary ground-state DFT matrix data로 학습하며 DFT-NEGF transport output을 학습 label로 요구하지 않는다.**
   - 범위: 저자들이 report한 training construction. 일반 DFT Hamiltonian/overlap 자료와 electrode data는 필요하다.
   - 판정: reported-primary.
   - 원 출처: Liu et al. (2026), Abstract and Methods pp. 11–12.
2. **E(3)-equivariant GNN은 큰 장치 Hamiltonian을 예측하고 DFT electrode self-energy, nonorthogonal KPM Fermi search, RGF transmission calculation을 결합한다.**
   - 범위: 논문의 static DFTH-NEGF workflow; transport SCF loop는 생략된다.
   - 판정: reported-primary.
   - 원 출처: Liu et al. (2026), §II, Fig. 1, pp. 3–4.
3. **저자들은 fixed cross-section and calculation settings에서 total cost가 channel length에 linear scaling을 보인다고 보고한다.**
   - 범위: reported cost terms for HamGNN prediction, nonorthogonal KPM and RGF; layer size, energy/k-point samples and convergence settings are fixed.
   - 판정: reported-primary.
   - 원 출처: Liu et al. (2026), §II and Methods, pp. 3–4.
4. **논문은 Pt–Si–Pt and doped Pt–Si:P–Pt test structures에서 보고된 Hamiltonian/transmission errors와 320–480 atom speedup을 제시한다.**
   - 범위: specific model, structures, basis, sampling and test settings.
   - 판정: reported-primary.
   - 원 출처: Liu et al. (2026), Results pp. 5–7, 9.
5. **finite-bias results use zero-bias H0 approximation and are limited to weakly nonlinear regimes; some pristine-interface transmission errors increase with bias.**
   - 범위: paper's finite-bias benchmark, not a fully self-consistent finite-bias general method.
   - 판정: reported-primary.
   - 원 출처: Liu et al. (2026), Abstract; Results pp. 9–11; Methods p. 12.
6. **The large-device overlap S construction is not sufficiently specified in the main paper and is marked as an implementation question.**
   - 범위: do not claim HamGNN predicts both H and S unless an additional source establishes it.
   - 판정: reported-primary.
   - 원 출처: Liu et al. (2026), §§II–III and Methods.

## 가정과 한계

- Linear scaling is not generalized to changing cross section or varying principal-layer size.
- The preprint's results do not establish transfer to the user's MoS₂/Au structure.
- Finite-bias validation is restricted to the studied weakly nonlinear approximation.
- Narrow molecular resonances can be sensitive to small Hamiltonian/energy errors.

## 그림과 표현

- hamgnn-negf-workflow.svg is an original workflow diagram and identifies the unspecified large-device overlap construction.
- editable source: refs/quality/figure-source/hamgnn-negf-workflow.html
- SVG and HTML hashes are stored in registry.
- diagram-design self_check.py --offline passed; Inkscape PNG was visually inspected.

## 독립 검토

- An independent source auditor and a separate scientific reviewer compared workflow, matrix target, scaling conditions, numerical results, finite-bias scope and the overlap-matrix caveat to arXiv v1.
- Korean prose was reviewed with humanizer while preserving equations, numbers and claim limits.
