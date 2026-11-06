# 품질 근거: born-effective-charge.md

- 대상 문서: `docs/computational-materials-science/dielectric-response/born-effective-charge.md`
- 판정 범위: 전체 문서, 신규 작성
- 검토 기준: 두 독립 과학 출처와 원문 귀속 결과를 구분한다.
- 문서 SHA-256: `89fe4f5952a36c27b1d8025815218bf29b55fcac1096d2e82ed1182a6b4a4a14`

## 문서 범위와 질문

- 목적: Born 유효전하의 응답 정의와 극성 격자·전자–포논 계산에서의 역할을 설명한다.
- 독자: 재료·DFT 기본 개념을 아는 연구자.
- 제외: 실험 재현, 특정 공정의 합성 가능성, 범용 ML 정확도 보증.

## 주장과 근거

1. **주장:** Born 유효전하는 원자 변위에 대한 분극 변화의 텐서 응답이며 형식 산화수와 동일하지 않다.
   - **범위:** 절연체에서 미소 변위 및 선형 응답
   - **판정:** `supported`
   - **출처:** gonze (Abstract; §III dynamical matrices; §IV electronic dielectric tensor; §V BEC; §VII sum rule; §VIII low-frequency response), baroni (§§II.3.2, II.4.2–4.3; §V.6 anharmonic effects)
2. **주장:** BEC와 고주파 유전 텐서는 polar long-range 전자–포논 항을 정하는 장파장 물리량이다.
   - **범위:** 3D polar crystal, 장파장 극한
   - **판정:** `supported`
   - **출처:** epw (Eqs. (3)–(13), (28)–(36); sections Phonons, e-ph matrix elements, long-range terms, self-energy), giustino (§§III.A–B, V.B; force constants, e-ph matrix elements, AHC self-energy and lifetimes)
3. **주장:** 조화 이온 유전 응답은 BEC뿐 아니라 포논 고유벡터와 주파수도 필요로 한다.
   - **범위:** 단위와 모드 정규화 규약을 고정한 bulk crystal
   - **판정:** `supported`
   - **출처:** gonze (Abstract; §III dynamical matrices; §IV electronic dielectric tensor; §V BEC; §VII sum rule; §VIII low-frequency response), baroni (§§II.3.2, II.4.2–4.3; §V.6 anharmonic effects)

## 가정과 한계

- 논문별 수치·후보는 해당 원문이 보고한 결과로만 기록했다. 독립 재현·합성·소자 검증으로 표현하지 않았다.
- 유전율 식은 본문에 적은 SI 단위, 구조, 선형·조화 근사와 모드 정규화에 한정한다.
- 원본 문헌의 그림을 복제하지 않았다. SVG는 개념 관계를 새로 그린 저작 도식이며, 아래 원문들은 물리 관계의 검증 근거다.

## 독립 검토

- 상태: pass; 전 문서와 적용된 그림 최종본 검토 완료.
- 독립 검토: dielectric_literature가 최종 문서의 과학 내용·인용·절 번호·수치와 원문을 대조했다.
- 독립 재현하지 않은 논문 고유 수치와 필터 결과는 본문 및 finding에서 1차 출처 보고값으로 한정했다.
