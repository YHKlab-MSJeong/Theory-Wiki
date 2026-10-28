# Landauer 수송과 transmission

!!! warning "검증 상태: 확인 중"
    핵심 식과 관례를 원문과 대조했다. 최종 본문 전체에 대한 독립적인 주장별 검토는 아직 끝나지 않았다.

## 1. 어떤 질문에 답하는가

두 전극 사이 소자의 에너지별 transmission으로부터 전류와 선형 응답 conductance를 어떻게 구하는가? 이 문서는 두 전극이 각각 평형 분포를 유지하고, 소자의 전자가 독립 입자로 기술되며 탄성·위상 결맞음 수송을 하는 정상상태를 기준으로 한다. 강한 상호작용과 비탄성 산란은 이 기본식의 적용 범위 밖에 둔다. [1, §1.1; 2, §2.4; 3, §II]

## 2. Transmission과 채널

에너지 \(E\)에서 왼쪽 전극으로부터 들어온 전자가 소자를 통과하여 오른쪽 전극으로 나갈 확률을 생각하자. 단일 채널에서는 transmission \(T(E)\)가 이 확률을 나타내며, 여러 채널이 있으면 각 transmission 고유값의 합으로 나타낼 수 있다. 따라서 다중 채널의 총 transmission은 1보다 클 수 있다. [4, §I.C.1–2; 6, §2.3, 식 (2.32)–(2.33)]

Transmission은 소자와 전극이 결합된 전체 수송 문제의 성질이다. 따라서 소자의 상태가 존재한다는 사실만으로 그 상태가 두 전극 사이 전류에 얼마나 기여할지 결정할 수는 없다. 이 문장에서의 해석은 두 전극을 잇는 전달을 다루는 [1, 식 (1.2)]과 전극 결합을 포함하는 [2, 식 (18)]에 근거한다.

## 3. 유한 바이어스 전류

두 전극의 온도가 같고 \(\mu_L-\mu_R=eV\)라고 정의한다. 여기서 \(e>0\)는 기본 전하, \(V\)는 이 화학 퍼텐셜 차이로 정의한 전압, \(h\)는 Planck 상수이다. 에너지 \(E\)와 화학 퍼텐셜은 같은 단위로 표현한다. 아래의 \(I\)는 \(\mu_L>\mu_R\)일 때 양수인 전류 관례를 쓴다. [1, 식 (1.6), Remark 2; 2, 식 (17)]

스핀별 transmission \(T_\sigma(E,V)\)를 각각 계산한 경우 전류는

\[
I(V)=\frac{e}{h}\sum_\sigma\int_{-\infty}^{\infty}
T_\sigma(E,V)\,[f_L(E)-f_R(E)]\,dE,
\qquad
f_\alpha(E)=\frac{1}{1+\exp[(E-\mu_\alpha)/(k_B\Theta)]}.
\]

\(\alpha=L,R\), \(k_B\)는 Boltzmann 상수, \(\Theta\)는 절대온도이다. \(f_L-f_R\)는 두 전극의 점유 차이를 나타내며, 이 차이와 transmission이 겹치는 에너지가 전류에 기여한다. [1, 식 (1.6); 2, 식 (17)]

두 스핀의 transmission이 같고 \(T\)가 한 스핀의 값이면 식 앞의 계수는 \(2e/h\)가 된다. 반대로 \(T\)에 이미 두 스핀이 합산되어 있다면 2를 다시 곱하지 않는다. [1, Remark 2; 4, §I.C.2]

유한 온도에서는 \(f_L-f_R\)의 가장자리가 퍼져 있다. 영도에서 \(\mu_L>\mu_R\)이면 그 차이는 \(\mu_R<E<\mu_L\)에서 1이고 그 밖에서는 0이므로, 적분 구간은 해당 에너지 구간으로 줄어든다. 이는 위 Fermi 함수의 영도 극한에서 얻는다. [1, 식 (1.6); 2, 식 (16)–(17)]

일반적으로 \(T_\sigma(E,V)\)는 바이어스에서의 소자 퍼텐셜에 의존할 수 있다. 따라서 0 V transmission을 고정한 적분은 별도의 근사이며, 유한 바이어스에서 구한 transmission을 사용한 결과와 구분한다. [7, §4; 8, §2.1, 식 (2.41)]

## 4. 선형 응답과 영도 극한

평형 화학 퍼텐셜을 \(\mu\), 평형 Fermi 함수를 \(f(E)\)라고 하자. \(V\to0\)에서 Fermi 함수를 전개하면

\[
f_L-f_R=eV\left(-\frac{\partial f}{\partial E}\right)+o(V).
\]

이에 전류식을 대입하고 \(T_\sigma(E,V)\)가 \(V=0\)에서 연속이라고 가정하면, 평형에서 \(f_L-f_R=0\)이므로 transmission의 1차 바이어스 변화는 선형 conductance에 기여하지 않는다. 결과는

\[
G=\left.\frac{dI}{dV}\right|_{V=0}
=\frac{e^2}{h}\sum_\sigma\int dE\,
T_\sigma(E,0)\left(-\frac{\partial f}{\partial E}\right).
\]

즉 유한 온도에서는 평형 화학 퍼텐셜 근처의 transmission이 열적 가중을 받아 conductance를 정한다. 영도이고 transmission이 \(E=\mu\)에서 연속이면 \(-\partial f/\partial E\)가 Dirac delta로 수렴하여

\[
G=\frac{e^2}{h}\sum_\sigma T_\sigma(\mu,0).
\]

위 유도는 Fermi 함수의 Taylor 전개와 영도 극한에 따른다. [1, 식 (1.6); 2, 식 (16)–(17)]

## 5. 계산 결과를 읽을 때

- 비교하는 transmission과 화학 퍼텐셜의 에너지 기준을 맞춘다. 스핀의 포함 여부와 전류 부호 관례도 함께 기록한다.
- 유한 바이어스에서는 해당 바이어스의 transmission과 점유 차이를 사용했는지 확인한다. 0 V 곡선을 사용했다면 그 근사를 명시한다.
- 주기적인 횡방향이 있는 계산에서는 \(k\)별 값과 Brillouin zone 평균값을 구분한다. TBtrans 문서는 두 출력을 별도로 정의한다. [5, NetCDF4 support]
- 에너지 간격과 적분 범위, 횡방향 \(k\)-점 및 전극 모델의 수렴은 별도로 확인한다. 식을 적용할 수 있다는 사실만으로 특정 계산 결과의 수치 수렴이나 실험 재현이 보장되지는 않는다.

## 6. 참고 자료

1. L. Bruneau, V. Jakšić, Y. Last, C.-A. Pillet, “Landauer-Büttiker and Thouless conductance” (2014), [§1.1, 식 (1.2), (1.6), Remark 2, 6](https://arxiv.org/html/1408.0185).
2. S. Kohler, J. Lehmann, P. Hänggi, “Driven quantum transport on the nanoscale” (2004), [§2.4, 식 (16)–(18), PDF pp. 14–15](https://arxiv.org/pdf/cond-mat/0409251). 원문은 반대쪽 전류 부호와 \(\mu_R-\mu_L=eV\)를 사용한다.
3. H. Ness, L. K. Dash, R. W. Godby, “Generalization and applicability of the Landauer formula for non-equilibrium current in the presence of interactions” (2010), [§II, 식 (4)](https://arxiv.org/pdf/1007.1104).
4. C. W. J. Beenakker, “Random-matrix theory of quantum transport” (1997), [§I.C.1–2, 식 (1.33)](https://arxiv.org/pdf/cond-mat/9612179).
5. [SIESTA documentation: TBTrans User Guide](https://docs.siesta-project.org/projects/siesta/en/stable/reference/tbtrans.html), NetCDF4 support.

6. D. Palmqvist, *Thermokinetic Uncertainty Relations and Dynamical Activities in Quantum Systems* (2026), [§2.3, 식 (2.32)–(2.33)](https://research.chalmers.se/publication/551724/file/551724_Fulltext.pdf).
7. V. Moldoveanu, R. Dragomir, [Theoretical methods for quantum transport](https://cifra-c2unesco.ro/wp-content/uploads/2022/10/QT-D1.pdf) (2022), §4, p. 10.
8. L. Groß, *Understanding molecular structure–function relationships in controlling nanoscale conductance* (2016), [§2.1, 식 (2.41)](https://ediss.sub.uni-hamburg.de/bitstream/ediss/6747/1/Dissertation.pdf).
