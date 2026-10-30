---
description: self-consistent Born approximation 반복의 수렴 판정과 물리 검사를 구분한다.
---

# SCBA convergence

## 1. SCBA가 푸는 고정점

self-consistent Born approximation (SCBA)은 scattering self-energy를 이전 Green function으로 계산하고 Dyson–Keldysh 식을 다시 푸는 고정점 문제다. \(g\)를 고립 central region의 Green function으로 정의하면, 개략적으로

\[
G_{n}^{r}(E)=\left[g^{-1}(E)-\Sigma_{\mathrm{contacts}}^{r}(E)-\Sigma_{\mathrm{scatt}}^{r}[G_{n-1}](E)\right]^{-1}
\]

처럼 쓸 수 있으며, lesser component도 같은 self-energy functional과 함께 갱신한다. phonon scattering을 포함한 NEGF 전개에서 이 반복과 electrostatic self-consistency를 구분한 예가 제시되어 있다. [Bescond et al., §II, 식 (1)–(2)](https://in4.iue.tuwien.ac.at/pdfs/sispad2013/21-3.pdf), [Mera–Pedersen–Nikolić, §V.1–2, 식 (21), (25)–(28)](https://arxiv.org/html/1512.06846)

## 2. 수치 수렴의 최소 조건

혼합된 iterate의 변화량이 작다는 것만으로 고정점 수렴을 선언하면 안 된다. mixing coefficient가 작으면 update가 작아져도 residual \(\lVert F[G]-G\rVert\)은 남을 수 있다. 따라서 (i) retarded와 lesser Green function 또는 self-energy의 residual, (ii) charge와 Poisson loop를 포함했으면 electrostatic residual, (iii) energy grid·integration window 변화에 대한 안정성을 서로 구분해 점검한다. 초기값과 energy range가 다른 self-consistent solution으로 이어질 수 있다는 사례가 보고되어 있다. [Lee–Sanvito, §III.B, 식 (41), (44); §V, Fig. 14–15](https://arxiv.org/pdf/0804.3389), [Bescond et al., §II](https://in4.iue.tuwien.ac.at/pdfs/sispad2013/21-3.pdf)

## 3. conservation과 analytic structure

정상상태 two-terminal 계산에서는 terminal current가 \(I_L=-I_R\)인지 확인해야 한다. Mera–Pedersen–Nikolić의 대칭 molecular model에서는 특정 coupling과 wide-band 조건에서 전류 일치가 iteration의 민감한 판별자가 아니었으므로, 전류 일치 하나만을 일반 convergence criterion으로 쓰면 부족하다. [Mera–Pedersen–Nikolić, §V.2, 식 (25)–(28)](https://arxiv.org/html/1512.06846), [Bescond et al., §II](https://in4.iue.tuwien.ac.at/pdfs/sispad2013/21-3.pdf) retarded self-energy의 causality, lesser/greater component의 관계와 Hilbert-transform 처리는 구현 convention 및 포함한 diagram에 맞게 별도 점검해야 하며, current conservation이 이를 대신하지 않는다. [Lee–Sanvito, §II.B, 식 (15)–(18)](https://arxiv.org/pdf/0804.3389), [Mera–Pedersen–Nikolić, §V.1](https://arxiv.org/html/1512.06846)

## 4. 수렴이 뜻하지 않는 것

SCBA 반복의 residual 통과는 선택한 Born diagram, phonon bath, screening, device Hamiltonian, contact model이 실제 물리를 충분히 설명한다는 증거가 아니다. 서로 다른 초기값·grid·mixing에서 같은 관측량을 얻는지는 numerical robustness 검사이지 실험적 검증이 아니다. [Lee–Sanvito, §V](https://arxiv.org/pdf/0804.3389), [Bescond et al., §II](https://in4.iue.tuwien.ac.at/pdfs/sispad2013/21-3.pdf)

## 5. 권장 기록

반복 횟수만 남기지 말고 residual norm과 norm의 정의, mixing, energy range·spacing, contact current mismatch, charge/Poisson residual, 초기값 및 중단 기준을 기록한다. 전류·전하·spectral function의 검사와 실험 또는 상위 수준 계산의 비교를 수치 수렴과 분리해 보고한다.

## 6. 참고 문헌

1. M. Bescond et al., *One-shot Current Conserving Approach of Phonon Scattering Treatment in Nano-transistors* (2013), §II, https://in4.iue.tuwien.ac.at/pdfs/sispad2013/21-3.pdf.
2. W. Lee, S. Sanvito, *Exploring the limits of the self consistent Born approximation for inelastic electronic transport* (2008), §II–V, https://arxiv.org/pdf/0804.3389.
3. H. Mera, T. G. Pedersen, B. K. Nikolić, *Hypergeometric resummation of self-consistent sunset diagrams for electron-boson quantum many-body systems out of equilibrium* (2016), §V, https://arxiv.org/html/1512.06846.
