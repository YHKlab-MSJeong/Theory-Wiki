---
description: 열린 전극, 산란 상태, transmission과 전류를 연결하는 양자 수송 문서의 읽는 길을 안내한다.
---

# 전자 수송의 열린 경계와 계산 접근

열린 전자 수송 문제는 전극이 상태를 공급하고 소자 안에서 전파·산란된 전자가 다시 전극으로 나가는 과정을 다룬다. 비평형 Green 함수 (non-equilibrium Green's function, NEGF)는 열린 계의 상태와 점유를 계산한다. 양자 전달 경계 방법 (quantum transmitting boundary method, QTBM)은 지정한 전극 모드에서 출발하는 산란 상태를 구한다. Landauer 관계는 에너지별 transmission과 두 전극의 점유 차이로 전류를 계산한다. 여기서는 독립 전자의 두 단자 정상상태 탄성·결맞음 수송을 기본형으로 둔다. [1, §II; 2, §II; 3; 4, §1.1; 5, §2.4; 6, Appendix D, pp. 784–785]

<figure markdown="span">

  ![두 단자에서 reservoir의 점유와 electrode self-energy가 산란영역에 열린 경계를 제공하며, transmission으로부터 charge current를 계산한다. NEGF와 QTBM은 수송 상태·전달을 기술하고, Landauer 관계는 transmission과 reservoir 점유 차이를 전류로 변환한다.](images/open-transport-overview.svg)

  <figcaption markdown="1">
  이 위키가 작성한 두 단자 charge-transport 개념도. NEGF와 QTBM의 수송 기술, Landauer 전류 관계의 역할을 나눠 표시했다. 원 논문의 그림을 복제하지 않았다.
  </figcaption>
</figure>

## 1. 문서 간 관계

[NEGF 문서](negf.md)는 열린 전극이 상태와 점유에 미치는 영향을 Green 함수로 다룬다. [QTBM 문서](scattering-qtbm.md)는 입사 전극 모드에 해당하는 산란 상태와 경계 조건을 설명한다. [Landauer 수송 문서](landauer-transmission.md)는 전극 점유 차이와 에너지별 transmission을 전류로 연결한다. 세 방법이 한 계산에서 항상 순서대로 적용되는 것은 아니다. 각 방법은 열린 경계, 파동함수 산란, 전류 관계라는 서로 다른 관점을 설명한다. [1–5]

## 2. 참고 자료

1. N. Papior et al., “Improvements on non-equilibrium and transport Green function techniques: the next-generation TranSIESTA,” *Computer Physics Communications* **212**, 8–24 (2017), [§II](https://arxiv.org/abs/1607.04464).
2. M. Brandbyge et al., “Density-functional method for nonequilibrium electron transport,” *Physical Review B* **65**, 165401 (2002), [§II](https://arxiv.org/abs/cond-mat/0110650).
3. C. S. Lent and D. J. Kirkner, “The quantum transmitting boundary method,” *Journal of Applied Physics* **67**, 6353–6359 (1990), [DOI](https://doi.org/10.1063/1.345156).
4. L. Bruneau et al., “Landauer-Büttiker and Thouless conductance,” *Journal of Mathematical Physics* **55**, 075204 (2014), [§1.1](https://arxiv.org/abs/1408.0185).
5. S. Kohler, J. Lehmann, and P. Hänggi, “Driven quantum transport on the nanoscale,” *Physics Reports* **406**, 379–443 (2005), [§2.4](https://arxiv.org/abs/cond-mat/0409251).
6. W. R. Frensley, “Boundary conditions for open quantum systems driven far from equilibrium,” *Reviews of Modern Physics* **62**, 745–791 (1990), [Appendix D, pp. 784–785](https://personal.utdallas.edu/~frensley/technical/FrensleyRMP1990.pdf), [DOI](https://doi.org/10.1103/RevModPhys.62.745).
