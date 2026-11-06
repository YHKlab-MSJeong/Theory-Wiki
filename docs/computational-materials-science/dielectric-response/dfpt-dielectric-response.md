---
description: DFPT에서 전자 응답, Born 유효전하, 힘상수와 포논을 결합해 유전 텐서를 계산하는 흐름을 설명한다.
---

# DFPT dielectric response

밀도범함수 섭동이론(density-functional perturbation theory, DFPT)은 평형 상태 주변에서 원자 변위와 전기장에 대한 전자계의 선형 응답을 계산한다. 이 응답으로 전자 유전 텐서, Born 유효전하, 동역학 행렬과 포논을 일관된 제일원리 틀 안에서 얻는다. [1, §§III–V; 2, §§II.3.2, II.4.2–4.3]

## 1. 계산되는 유전 응답

조화 절연체의 정적 유전 텐서는 고정 이온 전자 응답 \(\varepsilon^\infty\)와 격자 이온 응답의 합으로 쓸 수 있다.

\[
\varepsilon^0_{\alpha\beta}
=\varepsilon^\infty_{\alpha\beta}
+\varepsilon^{\mathrm{ion}}_{\alpha\beta}.
\]

\(\varepsilon^\infty\)는 원자 좌표를 고정한 전기장 섭동에서 계산한다. \(\varepsilon^{\mathrm{ion}}\)은 BEC와 Γ점 포논 모드에서 계산한다. 영 주파수 병진 모드는 분모에 넣지 않고, 전하 중성·병진 대칭 조건을 확인한다. 단위 셀 크기, 원자 질량, 모드 정규화, SI와 Gaussian 단위 선택은 결과 식에 영향을 주므로 계산별 규약을 명시해야 한다. [1, §§IV, VII–VIII; 2, §§II.3.2, II.4.2–4.3]

## 2. 수치 절차와 검토

실제 절차는 구조와 전자 바닥상태를 먼저 수렴한 뒤, 전기장 응답과 원자 변위 응답을 구하고, 힘상수와 포논 고유모드를 계산해 각 유전 기여를 조합하는 순서다. DFPT 응답은 격자, k점, 기저, pseudopotential과 수렴 설정에 의존하므로 단일 계산의 출력만으로 물리적 수렴을 단정할 수 없다. [1, §§III–V, VII–VIII; 2, §§II.3.2, II.4.2–4.3]

검토할 때는 다음 양을 서로 나눠 확인한다.

- 전자 \(\varepsilon^\infty\), 이온 \(\varepsilon^{\mathrm{ion}}\), 전체 정적 텐서가 각각 저장되어 있는가.
- BEC 합의 acoustic sum rule 잔차, 모드 주파수와 허수 모드 여부가 기록되었는가.
- k점, cutoff, 구조, 대칭, 전기장 및 원자 변위 응답의 수렴이 확인되었는가.
- 유전율을 보고할 때 방향별 텐서와 평균의 정의, 단위계, 이온 완화와 주파수 조건을 명시했는가.

## 3. 적용 범위

이 선형 응답은 선택한 구조와 전자구조 근사 주변의 미소 섭동에 대한 것이다. 구조적 상전이, 강한 비조화성, 분극의 이력 현상, 결함·계면이나 실제 박막의 효과는 별도 모델링 또는 계산이 필요하다. 계산이 수렴했다는 사실은 선택한 구조가 열역학적으로 안정하거나 소자에 적합하다는 판정을 대신하지 않는다. [1, §§III–VIII; 2, §§II.4.2–4.3, V.6; 3, §§2–3]

## 4. 참고 문헌

1. X. Gonze and C. Lee, *Physical Review B* **55**, 10355 (1997), https://doi.org/10.1103/PhysRevB.55.10355.
2. S. Baroni et al., *Reviews of Modern Physics* **73**, 515 (2001), https://doi.org/10.1103/RevModPhys.73.515.
3. M. Stengel, N. A. Spaldin, and D. Vanderbilt, “Electric displacement as the fundamental variable in electronic-structure calculations,” *Nature Physics* **5**, 304–308 (2009), https://doi.org/10.1038/nphys1185.
