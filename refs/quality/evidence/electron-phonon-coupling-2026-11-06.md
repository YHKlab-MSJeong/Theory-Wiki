# 품질 근거: electron-phonon-coupling.md

- 대상 문서: `docs/computational-materials-science/electron-phonon-coupling/electron-phonon-coupling.md`
- 판정 범위: 전체 문서, 신규 작성
- 검토 기준: 두 독립 과학 출처와 원문 귀속 결과를 구분한다.
- 문서 SHA-256: `5daa502470a743c1119b639c99d73cef8a94251c3ec2953bdf62d5f920a1994c`

## 문서 범위와 질문

- 목적: 힘상수·동역학 행렬·포논 모드와 전자–포논 결합 행렬원소의 관계를 연결한다.
- 독자: 재료·DFT 기본 개념을 아는 연구자.
- 제외: 실험 재현, 특정 공정의 합성 가능성, 범용 ML 정확도 보증.

## 주장과 근거

1. **주장:** 힘상수는 에너지 Hessian이며 Fourier 변환과 원자 질량 가중으로 동역학 행렬을 만들고, 그 고유값은 포논 주파수 제곱이다.
   - **범위:** 조화 결정; 문서에 고정한 Fourier 부호·고유벡터 규약
   - **판정:** `supported`
   - **출처:** giustino (§§III.A–B, V.B; force constants, e-ph matrix elements, AHC self-energy and lifetimes), baroni (§§II.3.2, II.4.2–4.3; §V.6 anharmonic effects)
2. **주장:** EPC 행렬원소는 포논 모드의 1차 퍼텐셜 변화가 전자 상태 전이에 결합하는 진폭이다.
   - **범위:** 주기 결정의 harmonic DFPT; prefactor와 normalization convention 명시
   - **판정:** `supported`
   - **출처:** giustino (§§III.A–B, V.B; force constants, e-ph matrix elements, AHC self-energy and lifetimes), epw (Eqs. (3)–(13), (28)–(36); sections Phonons, e-ph matrix elements, long-range terms, self-energy)
3. **주장:** 극성 long-range Fröhlich contribution은 BEC와 epsilon-infinity에 의존하고 단거리 보간과 별도 처리된다.
   - **범위:** polar 3D crystal, long-wavelength treatment
   - **판정:** `supported`
   - **출처:** epw (Eqs. (3)–(13), (28)–(36); sections Phonons, e-ph matrix elements, long-range terms, self-energy), giustino (§§III.A–B, V.B; force constants, e-ph matrix elements, AHC self-energy and lifetimes)

## 가정과 한계

- 논문별 수치·후보는 해당 원문이 보고한 결과로만 기록했다. 독립 재현·합성·소자 검증으로 표현하지 않았다.
- 유전율 식은 본문에 적은 SI 단위, 구조, 선형·조화 근사와 모드 정규화에 한정한다.
- 원본 문헌의 그림을 복제하지 않았다. SVG는 개념 관계를 새로 그린 저작 도식이며, 아래 원문들은 물리 관계의 검증 근거다.

## 그림

- `docs/assets/eph-workflow.svg` SHA-256 `0baaecd332809a54ccb53c8116016ceab3ec38b4b945abd164e04151568eb766`; editable source `refs/quality/figure-source/eph-workflow.html`.
  - SVG accessible title/description and system-font offline self-check passed; source-claim boundary as described above.

## 독립 검토

- 상태: pass; 전 문서와 적용된 그림 최종본 검토 완료.
- 독립 검토: eph_sources가 최종 문서의 수식·규약·근사·인용을 대조하고, diagram_audit가 연결된 도식과 설명의 일치를 점검했다.
- 독립 재현하지 않은 논문 고유 수치와 필터 결과는 본문 및 finding에서 1차 출처 보고값으로 한정했다.
