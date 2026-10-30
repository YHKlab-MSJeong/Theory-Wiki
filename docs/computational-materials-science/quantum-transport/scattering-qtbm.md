---
description: QTBM 개방경계 해법과 비탄성 산란 모형의 결합 조건을 구분한다.
---

# Scattering QTBM method

## 1. 기본 QTBM의 역할

quantum transmitting boundary method (QTBM)은 open contact에서 주어진 incoming mode에 대한 stationary Schrödinger equation을 transmitting boundary condition과 함께 푸는 방법이다. discretized device에서는 contact self-energy 또는 동등한 boundary operator를 써서 반사·투과 파를 구하며, 이 기본 문제는 elastic coherent scattering state의 문제다. [Frensley, Appendix D, 식 (D1)–(D5)](https://personal.utdallas.edu/~frensley/technical/FrensleyRMP1990.pdf), [Shao et al., §I–II, 식 (2)](https://academicweb.nd.edu/~lent/pdf/nd/An_eigenvalue_method_for_open-boundary_quantum_transmission_problems.pdf)

## 2. NEGF와의 관계

같은 single-particle Hamiltonian과 ideal lead를 쓰는 탄성 정상상태에서는 QTBM의 outgoing boundary와 retarded lead self-energy가 동등한 open-boundary 문제를 표현한다. 그러나 QTBM wavefunction 하나는 reservoir occupation 또는 inelastic redistribution을 자동으로 주지 않는다. 다중 incoming mode의 점유와 current를 계산할 때에는 각 mode의 injection과 Fermi occupation을 명시해야 한다. [Gehring, §3.5.4, 식 (3.84)–(3.91)](https://www.iue.tuwien.ac.at/phd/gehring/node51.html), [Frensley, Appendix D](https://personal.utdallas.edu/~frensley/technical/FrensleyRMP1990.pdf)

## 3. 산란을 결합하려면

phonon, roughness, impurity scattering을 넣는 방법은 유일하지 않다. 예를 들어 QTBM solution을 Pauli master equation과 결합해 scattering transition과 population을 갱신하는 모형이 있다. 이는 QTBM 자체가 비탄성 산란을 포함한다는 뜻이 아니라 추가된 collision model과 closure가 수송을 결정한다. [Vyas et al., abstract](https://journals.aps.org/prapplied/abstract/10.1103/PhysRevApplied.13.014067), [Kosik, §7.2.6.1](https://www.iue.tuwien.ac.at/phd/kosik/node96.html)

## 4. 허수 퍼텐셜만으로 충분하지 않은 이유

\(-iW\) 같은 absorbing term은 out-scattering 또는 loss를 나타낼 수 있지만, 일반적으로 corresponding in-scattering을 만들지 않는다. Kosik과 Heinz의 예에서 보듯 이를 phonon scattering 전체로 등치하면 population을 결정할 수 없으므로, source/in-scattering term과 그 산란률·bath occupation을 같은 모형 안에서 정의해야 한다. [Kosik, §7.2.6.1, 식 (7.22)–(7.25)](https://www.iue.tuwien.ac.at/phd/kosik/node96.html), [Heinz, §4.5, PDF p. 111](https://iis-people.ee.ethz.ch/~schenk/theses/heinz.pdf)

## 5. 적용과 검증 기준

문서나 코드에서 scattering QTBM이라고 부를 때에는 elastic QTBM boundary, scattering Hamiltonian 또는 rate, population update, in/out-scattering 관계, self-consistency 대상, current conservation 검사를 명시한다. elastic QTBM transmission과 산란 결합 결과를 직접 비교할 때에는 contact mode·energy grid·injection convention을 고정한다. numerical current conservation은 산란 model의 현실성을 보증하지 않는다.

## 6. 참고 문헌

1. W. R. Frensley, *Boundary conditions for open quantum systems driven far from equilibrium*, Rev. Mod. Phys. (1990), Appendix D, https://personal.utdallas.edu/~frensley/technical/FrensleyRMP1990.pdf.
2. Z.-a. Shao et al., *An eigenvalue method for open-boundary quantum transmission problems* (1995), §I–II, https://academicweb.nd.edu/~lent/pdf/nd/An_eigenvalue_method_for_open-boundary_quantum_transmission_problems.pdf.
3. R. Kosik, *Numerical Challenges on the Road to NanoTCAD* (2004), §7.2.6.1, https://www.iue.tuwien.ac.at/phd/kosik/node96.html.
4. P. B. Vyas et al., *Master-Equation Study of Quantum Transport in Realistic Semiconductor Devices Including Electron-Phonon and Surface-Roughness Scattering* (2020), abstract, https://journals.aps.org/prapplied/abstract/10.1103/PhysRevApplied.13.014067.
5. A. Gehring, *Simulation of Tunneling in Semiconductor Devices* (2003), §3.5.4, https://www.iue.tuwien.ac.at/phd/gehring/.
6. F. O. Heinz, *Simulation Approaches for Nano-Scale Semiconductor Devices* (2004), §4.5, https://iis-people.ee.ethz.ch/~schenk/theses/heinz.pdf.
