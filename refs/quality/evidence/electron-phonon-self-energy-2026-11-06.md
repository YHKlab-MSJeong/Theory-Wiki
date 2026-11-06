# 품질 근거: electron-phonon-self-energy.md

- 대상 문서: `docs/computational-materials-science/electron-phonon-coupling/electron-phonon-self-energy.md`
- 판정 범위: 전체 문서, 신규 작성
- 검토 기준: 두 독립 과학 출처와 원문 귀속 결과를 구분한다.
- 문서 SHA-256: `cc6fbbaa662464a31b4e01d8b4155dc950b6ed89508f62ae3d683a4b8e0e85a4`

## 문서 범위와 질문

- 목적: Fan–Migdal과 Debye–Waller self-energy 및 준입자 근사의 에너지·수명 해석을 설명한다.
- 독자: 재료·DFT 기본 개념을 아는 연구자.
- 제외: 실험 재현, 특정 공정의 합성 가능성, 범용 ML 정확도 보증.

## 주장과 근거

1. **주장:** Fan–Migdal은 동적 1차 EPC 제곱 항이고 Debye–Waller는 정적 2차 퍼텐셜 항이다.
   - **범위:** 조화 AHC, band-diagonal 근사와 retarded convention
   - **판정:** `supported`
   - **출처:** epw (Eqs. (3)–(13), (28)–(36); sections Phonons, e-ph matrix elements, long-range terms, self-energy), giustino (§§III.A–B, V.B; force constants, e-ph matrix elements, AHC self-energy and lifetimes)
2. **주장:** 에너지 이동은 실수부와 연결되고 허수부는 준입자 반폭·수명과 연결되지만 peak가 잘 정의된 조건에서만 단순식을 쓸 수 있다.
   - **범위:** retarded electron self-energy; half-width convention 명시
   - **판정:** `supported`
   - **출처:** epw (Eqs. (3)–(13), (28)–(36); sections Phonons, e-ph matrix elements, long-range terms, self-energy), giustino (§§III.A–B, V.B; force constants, e-ph matrix elements, AHC self-energy and lifetimes)
3. **주장:** pole, on-shell, adiabatic AHC 계산은 서로 다른 에너지 평가 및 포논 근사를 사용한다.
   - **범위:** 근사 가정 및 broadening·k/q 수렴을 분리
   - **판정:** `supported`
   - **출처:** giustino (§§III.A–B, V.B; force constants, e-ph matrix elements, AHC self-energy and lifetimes), ponce23 (Review sections on Fan and Debye-Waller terms and calculation approximations)

## 가정과 한계

- 논문별 수치·후보는 해당 원문이 보고한 결과로만 기록했다. 독립 재현·합성·소자 검증으로 표현하지 않았다.
- 유전율 식은 본문에 적은 SI 단위, 구조, 선형·조화 근사와 모드 정규화에 한정한다.
- 원본 문헌의 그림을 복제하지 않았다. SVG는 개념 관계를 새로 그린 저작 도식이며, 아래 원문들은 물리 관계의 검증 근거다.

## 그림

- `docs/assets/eph-self-energy.svg` SHA-256 `c455b61dbb0de41df1faab0a9840151c33a50fcc0f2fd56f4b5f83a255d0f8a8`; editable source `refs/quality/figure-source/eph-self-energy.html`.
  - SVG accessible title/description and system-font offline self-check passed; source-claim boundary as described above.

## 독립 검토

- 상태: pass; 전 문서와 적용된 그림 최종본 검토 완료.
- 독립 검토: eph_sources가 최종 문서의 수식·규약·근사·인용을 대조하고, diagram_audit가 연결된 도식과 설명의 일치를 점검했다.
- 독립 재현하지 않은 논문 고유 수치와 필터 결과는 본문 및 finding에서 1차 출처 보고값으로 한정했다.
