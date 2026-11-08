---
description: Born 유효전하를 원자 변위와 거시 분극 사이의 동적 선형 응답으로 정의한다.
---

# Born effective charge

Born 유효전하(Born effective charge, BEC)는 원자의 형식 산화수와 같은 정전기적 전하가 아니다. 결정에서 원자 하나를 조금 움직였을 때 거시 분극이 얼마나 변하는지를 나타내는 텐서이며, 전기장에 대한 원자 힘의 응답으로도 정의할 수 있다. [1, §V; 2, §II.3.2]

## 1. 정의와 단위

셀 부피를 \(\Omega\), 원자 \(\kappa\)의 변위를 \(u_{\kappa\beta}\), 분극 성분을 \(P_\alpha\)라 하면 SI 정의는

\[
Z^{*}_{\kappa,\alpha\beta}
=\Omega\frac{\partial P_\alpha}{\partial u_{\kappa\beta}}
=\frac{\partial F_{\kappa\beta}}{\partial E_\alpha}.
\]

여기서 \(Z^*\)의 차원은 전하이며, 결정 대칭이 허용하는 비대각 원소를 포함할 수 있다. 일부 계산 코드와 논문은 \(Z^*/e\)처럼 기본 전하 \(e\)로 나눈 무차원 값을 표기한다. 지표 순서와 부호는 문헌 규약에 맞춰 확인해야 한다. [1, §V; 2, §II.3.2]

## 2. 형식 전하와의 차이

원자가 움직이면 주변 결합 전자도 재배치되므로 분극 변화는 원자 핵의 전하만으로 정해지지 않는다. 따라서 BEC가 형식 전하보다 크거나 비등방적일 수 있다. 이런 동적 응답은 유전 텐서, 극성 포논, 장거리 전자–포논 결합을 계산하는 데 쓰인다. [1, §V; 2, §II.3.2]

## 3. 계산에서의 역할과 조건

DFPT는 원자 변위나 거시 전기장에 대한 전자 밀도와 파동함수의 1차 응답을 구하고, 이로부터 BEC를 얻는다. BEC는 고주파 유전 텐서 및 동역학 행렬과 함께 장파장 극성 격자 응답을 정한다. [1, §§III–V, VIII; 2, §§II.3.2, II.4.2]

절연체의 전체 Born 전하 텐서에 대한 합은 병진 불변성의 acoustic sum rule을 만족해야 한다. 수치 오차 때문에 남는 잔차는 출력과 보정 여부를 함께 기록해야 한다. 금속에서는 거시 분극의 정의와 장파장 전기장 응답이 절연체와 다르므로 같은 정의를 무비판적으로 적용할 수 없다. [1, §VII; 2, §§II.3.2, II.4.2]

## 4. 유전 응답 및 전자–포논 결합과 연결

BEC와 포논 고유벡터를 합쳐 모드 유효전하를 만들면 이온 유전율 기여를 얻는다. 극성 물질의 장거리 Fröhlich 전자–포논 퍼텐셜도 BEC와 \(\varepsilon^\infty\)에 의존하므로, 두 물리량은 [유전 응답](dielectric-response.md)과 [전자–포논 결합](../electron-phonon-coupling/electron-phonon-coupling.md)에서 함께 쓰인다. [1, §§IV–V, VIII; 2, §§II.3.2, II.4.2; 3, “Long-range contributions”]

## 5. 참고 문헌

1. X. Gonze and C. Lee, *Physical Review B* **55**, 10355 (1997), https://doi.org/10.1103/PhysRevB.55.10355.
2. S. Baroni et al., *Reviews of Modern Physics* **73**, 515 (2001), https://doi.org/10.1103/RevModPhys.73.515.
3. EPW project, “Theory: Long-range contributions,” https://docs.epw-code.org/Theory.html#long-range-contributions.
