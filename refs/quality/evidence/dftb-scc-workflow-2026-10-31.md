# DFTB SCC workflow 그림 검증 기록

대상: `docs/computational-science/atomistic-simulation/dftb-large-scale.md`  
대상 SHA-256: `ec2bb020a8dd61278ed2cfbcb5ac9dd21b4def57ee72e011df318711fbb1aa42`  
기준 버전 SHA-256: `3561f23ebf9c3bebd45c9487b44a5ea7c5ea4f67eb53b432f43fa6db57f90fe2`  
그림: `docs/assets/scc-workflow.svg`  
그림 SHA-256: `a5b52b942dfe7f32085ef43aeb11ed487005026f0e45d137cb7a380c87eda58d`

이 변경은 기존 SCC-DFTB2 설명의 의미를 바꾸지 않고, 현재 \(\Delta q\) → SCC 보정 Hamiltonian → density matrix → 새 Mulliken \(\Delta q\) → residual 검사 → mixing 반복이라는 fixed-point 흐름을 원본 SVG로 시각화했다. 그림에는 수치 결과나 외부 논문 그림이 없다.

Koskinen–Mäkinen §II 식 (37)–(43), §IX 식 (91)–(92)와 Hourahine et al. §II.A.2–3 식 (7)–(12)을 대조했다. 접근성 검사와 SVG 구조 검사를 통과했다. SCC 수렴이 parameter validity·DFT/실험 정확도·전역 최소를 보장하지 않는다는 본문 한계를 보존했다.

1. P. Koskinen, V. Mäkinen, *Density-Functional Tight-Binding for Beginners* (2009), https://arxiv.org/pdf/0910.5861.
2. B. Hourahine et al., *DFTB+* (2020), https://strathprints.strath.ac.uk/71868/1/Hourahine_etal_JCP_2020_DFTB_plus_a_software_package_for_efficient_approximate.pdf.
