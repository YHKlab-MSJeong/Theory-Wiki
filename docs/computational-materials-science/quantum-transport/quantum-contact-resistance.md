---
description: Landauer 채널 수와 transmission으로 정해지는 양자 접촉저항의 범위를 설명한다.
---

# Quantum contact resistance

## 1. 저항 양자의 convention

전하 \(e>0\)를 쓰면 하나의 spin-resolved ballistic channel의 conductance quantum은 \(G_Q=e^2/h\), 저항 양자는 \(R_Q=h/e^2\)이다. spin degeneracy가 보존된 하나의 orbital mode는 두 channel을 가지므로 conductance는 \(2e^2/h\)가 된다. 따라서 \(h/e^2\), \(h/(2e^2)\)라는 숫자를 쓰기 전에 spin·valley·orbital degeneracy를 채널 수에 포함했는지 밝혀야 한다. [Beenakker, §I.C.2, 식 (1.33)](https://arxiv.org/pdf/cond-mat/9612179), [Feilhauer–Moško, §I](https://arxiv.org/pdf/1011.6193)

## 2. 이상적인 두 단자 한계

zero-temperature에서 Fermi energy로 평가한 phase-coherent two-terminal conductor의 선형 conductance는

\[
G=\frac{e^2}{h}\sum_n T_n,
\]

이며 \(T_n\)은 spin을 이미 분리해 센 channel \(n\)의 transmission이다. 따라서 \(N\)개의 spin-degenerate mode가 모두 \(T=1\)이면 \(R_{2\mathrm{t}}=h/(2e^2N)\)이다. 이 유한 값은 disorder가 없는 channel에도 reservoir와 mode matching이 있는 두 단자 측정에서 나타나는 contact contribution이다. [Beenakker, §I.C.2](https://arxiv.org/pdf/cond-mat/9612179), [Feilhauer–Moško, §I, 식 (11), (15)](https://arxiv.org/pdf/1011.6193)

## 3. 접촉 하나에 임의로 반씩 나눌 수 없는 이유

대칭 이상 모형에서는 \(h/(2e^2N)\)를 양쪽 접촉에 \(h/(4e^2N)\)씩 배분하는 bookkeeping을 쓸 수 있다. 하지만 비대칭 contact, 반사, mode mismatch가 있으면 각 contact에 고유하고 보편적인 half-quantum resistance를 할당할 수 없다. 실제 contact의 transmission은 contact material과 geometry에 의존하므로 이 bookkeeping을 계면의 고유 물성으로 읽으면 안 된다. [Mortensen et al., §I](https://arxiv.org/pdf/cond-mat/9907026), [Beenakker, §I.C](https://arxiv.org/pdf/cond-mat/9612179)

## 4. 네 단자 저항과의 구별

four-terminal measurement는 voltage probe의 위치와 coupling으로 정의된 electrochemical potential 차이를 쓴다. weak noninvasive probe의 이상화에서 ballistic channel의 내부 voltage drop은 two-terminal 값과 다를 수 있다. 그러므로 네 단자 추출값과 \(h/(2e^2N)\)을 직접 동일시하거나, \(R_Q\)를 모든 interface의 실제 contact resistance로 쓰면 안 된다. [Texier–Montambaux, §2](https://gilles.montambaux.com/files/publications/reprints/189_four_terminal_resistances.pdf), [Landauer, abstract](https://doi.org/10.1088/0953-8984/1/43/011)

## 5. 계산·보고 기준

양자 한계를 인용할 때에는 \(T_n\), degeneracy convention, terminal 수, 온도·energy averaging, two- 또는 four-terminal 정의를 함께 쓴다. 유한 온도에서는 \(-\partial f/\partial E\) 가중을, 유한 bias에서는 \(f_L-f_R\) 적분과 가능하면 bias-dependent transmission을 다룬다. 비탄성 산란은 별도 모형이 있을 때만 포함한다. [Landauer–Büttiker transport](landauer-buttiker.md)를 함께 참조한다.

## 6. 참고 문헌

1. C. W. J. Beenakker, *Random-matrix theory of quantum transport* (1997), §I.C.2, https://arxiv.org/pdf/cond-mat/9612179.
2. J. Feilhauer, M. Moško, *Quantum and Boltzmann transport in the quasi-one-dimensional wire with rough edges* (2010), §I, https://arxiv.org/pdf/1011.6193.
3. N. A. Mortensen et al., *Contact resistance of quantum tubes* (1999), §I, https://arxiv.org/pdf/cond-mat/9907026.
4. C. Texier, G. Montambaux, *Four-terminal resistances in mesoscopic networks of metallic wires: Weak localisation and correlations*, §2, https://gilles.montambaux.com/files/publications/reprints/189_four_terminal_resistances.pdf.
5. R. Landauer, *Conductance determined by transmission: probes and quantised constriction resistance*, abstract, https://doi.org/10.1088/0953-8984/1/43/011.
