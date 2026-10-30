# Scattering QTBM 검증 기록

대상: `docs/computational-materials-science/quantum-transport/scattering-qtbm.md`  
대상 SHA-256: `57d16c75a0fe3fc3fdf1ed7d617f011b348aa60a91286aebddcf93b72498657b`

범위는 elastic QTBM open boundary, retarded-self-energy와의 등가적 open problem, 그리고 absorbing term에 대응하는 reinjection 필요성이다. Vyas의 Pauli-master-equation 결합은 단일 논문의 사례로만 기록한다.

| 주장 | 대조 근거 | 판정 |
| --- | --- | --- |
| QTBM은 incoming mode의 elastic open-boundary scattering-state 해법 | Frensley Appendix D 식 (D1)–(D5); Shao et al. §I–II 식 (2) | supported |
| QTBM outgoing boundary와 retarded lead self-energy의 관계 | Gehring §3.5.4 식 (3.84)–(3.91); Frensley Appendix D | supported |
| absorbing loss만으로는 conservation을 닫지 못하며 reinjection model이 필요 | Kosik §7.2.6.1 식 (7.22)–(7.25); Heinz §4.5 PDF p. 111 | supported |

독립 검토자 `wiki_tooling`가 QTBM 자체가 비탄성 산란을 포함한다고 읽히는 표현과 허수 퍼텐셜의 단일 근거를 지적했다. 작성자는 Pauli master equation을 한 사례로 낮추고 Kosik·Heinz의 독립 근거를 추가했다. Shao 원문은 접근 timeout이 있어 해당 식별자·주장 범위만 보수적으로 기록했다. humanizer 점검은 과학 의미를 바꾸지 않았다. 그림·수치 예제는 없다.

1. W. R. Frensley, *Boundary conditions for open quantum systems driven far from equilibrium*, Rev. Mod. Phys. (1990), Appendix D, https://personal.utdallas.edu/~frensley/technical/FrensleyRMP1990.pdf.
2. Z.-a. Shao et al., *An eigenvalue method for open-boundary quantum transmission problems* (1995), §I–II, https://academicweb.nd.edu/~lent/pdf/nd/An_eigenvalue_method_for_open-boundary_quantum_transmission_problems.pdf.
3. R. Kosik, *Numerical Challenges on the Road to NanoTCAD* (2004), §7.2.6.1, https://www.iue.tuwien.ac.at/phd/kosik/node96.html.
4. F. O. Heinz, *Simulation Approaches for Nano-Scale Semiconductor Devices* (2004), §4.5, https://iis-people.ee.ethz.ch/~schenk/theses/heinz.pdf.
