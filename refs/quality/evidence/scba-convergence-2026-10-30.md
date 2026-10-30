# SCBA convergence 검증 기록

대상: `docs/computational-materials-science/quantum-transport/scba-convergence.md`  
대상 SHA-256: `6a194a73c50ecd4b9abf8548b28d7f6d5e43c6af4f33db5d5d32f8e82b889021`

범위는 고립 central-region \(g\)를 사용한 SCBA fixed-point iteration, residual·current conservation의 분리, 특정 모형에서의 초기값·energy-window 민감도다.

| 주장 | 대조 근거 | 판정 |
| --- | --- | --- |
| scattering self-energy와 Green function의 self-consistent iteration | Bescond et al. §II 식 (1)–(2); Mera–Pedersen–Nikolić §V.1–2 식 (21), (25)–(28) | supported |
| iterate change, fixed-point residual, current conservation을 구별해야 함 | Lee–Sanvito §III.B·§V; Mera–Pedersen–Nikolić §V.2 | supported |
| numerical fixed point는 물리 모형 검증과 다름 | Lee–Sanvito §V; Bescond et al. §II | supported |

독립 검토자 `wiki_tooling`가 contact self-energy 이중계산 가능성을 지적했다. 작성자는 \(g\)를 고립 central region으로 정의하고 Mera 논문의 대칭-model 관찰을 일반 명제로 쓰지 않도록 범위를 고쳤다. humanizer 점검은 식·조건을 보존했다. 그림·수치 예제는 없다.

1. M. Bescond et al., *One-shot Current Conserving Approach of Phonon Scattering Treatment in Nano-transistors* (2013), §II, https://in4.iue.tuwien.ac.at/pdfs/sispad2013/21-3.pdf.
2. W. Lee, S. Sanvito, *Exploring the limits of the self consistent Born approximation for inelastic electronic transport* (2008), §II–V, https://arxiv.org/pdf/0804.3389.
3. H. Mera, T. G. Pedersen, B. K. Nikolić, *Hypergeometric resummation of self-consistent sunset diagrams for electron-boson quantum many-body systems out of equilibrium* (2016), §V, https://arxiv.org/html/1512.06846.
