# 품질 근거: dielectric-response.md

- 대상 문서: `docs/computational-materials-science/dielectric-response/dielectric-response.md`
- 판정 범위: 전체 문서, 신규 작성
- 검토 기준: 두 독립 과학 출처와 원문 귀속 결과를 구분한다.
- 문서 SHA-256: `837e3d50ec1d7f1d0f1ffc892c950dd9f0c148391e477c1e9f6b65ac7daacfb4`

## 문서 범위와 질문

- 목적: 유전 응답을 전자·이온 성분으로 나누고 조화 포논 모드와 Born 유효전하를 연결한다.
- 독자: 재료·DFT 기본 개념을 아는 연구자.
- 제외: 실험 재현, 특정 공정의 합성 가능성, 범용 ML 정확도 보증.

## 주장과 근거

1. **주장:** Takigawa 등은 진공 기준을 포함하는 고주파 유전율을 1 + 전자 유전 기여로 표기한다.
   - **범위:** 특정 논문에 사용된 표기 convention의 기록이며 표기법 전체를 단정하지 않음
   - **판정:** `reported-primary`
   - **출처:** prx (Abstract; §I notation; §II.A Eq. (2) Fig. 3; §II.B Eq. (3) Fig. 4 and Table III; primary-research)
   - **판정 메모:** 1차 연구 논문에 귀속한 보고값이며 독립 재현 결과가 아니다.
2. **주장:** 정적 유전 응답은 고정 이온 전자 항과 격자 이온 항으로 분해되며, 이온 응답은 DFPT의 BEC와 포논 정보를 사용한다.
   - **범위:** 절연체의 선형·조화 응답; SI에서 상대 유전율 텐서
   - **판정:** `supported`
   - **출처:** gonze (Abstract; §III dynamical matrices; §IV electronic dielectric tensor; §V BEC; §VII sum rule; §VIII low-frequency response), baroni (§§II.3.2, II.4.2–4.3; §V.6 anharmonic effects)
3. **주장:** 질량 정규화 포논 모드의 이온 유전 응답은 모드 유효전하와 주파수에 의존하며, 저주파 모드는 역제곱 가중을 받는다.
   - **범위:** 정적 Γ점 조화 응답; 영주파수 병진 모드는 제외
   - **판정:** `supported`
   - **출처:** gonze (Abstract; §III dynamical matrices; §IV electronic dielectric tensor; §V BEC; §VII sum rule; §VIII low-frequency response), baroni (§§II.3.2, II.4.2–4.3; §V.6 anharmonic effects)
4. **주장:** High-k 게이트 재료의 유전율은 두께·밴드갭·밴드 정렬·계면 조건과 함께 판단해야 한다.
   - **범위:** 벌크 계산값에서 소자 적합성으로 과도 일반화 금지
   - **판정:** `supported`
   - **출처:** robertson04 (Eq. (1), §§1–2; high-k gate dielectric constraints), robertson06 (Review sections on dielectric constant, band gap, offsets and interfaces)

## 가정과 한계

- 논문별 수치·후보는 해당 원문이 보고한 결과로만 기록했다. 독립 재현·합성·소자 검증으로 표현하지 않았다.
- 유전율 식은 본문에 적은 SI 단위, 구조, 선형·조화 근사와 모드 정규화에 한정한다.
- 원본 문헌의 그림을 복제하지 않았다. SVG는 개념 관계를 새로 그린 저작 도식이며, 아래 원문들은 물리 관계의 검증 근거다.

## 그림

- `docs/assets/dielectric-response-map.svg` SHA-256 `9a12f5c3a11c87a75213a52448d51fd446d04e224cf944c91f81e3b41a1c1dd9`; editable source `refs/quality/figure-source/dielectric-response-map.html`.
  - SVG accessible title/description and system-font offline self-check passed; source-claim boundary as described above.

## 독립 검토

- 상태: pass; 전 문서와 적용된 그림 최종본 검토 완료.
- 독립 검토: dielectric_literature가 최종 문서의 과학 내용·인용·절 번호·수치와 원문을 대조했다. diagram_audit가 연결된 SVG와 HTML 원본의 식·접근성 설명을 별도로 대조했다.
- 독립 재현하지 않은 논문 고유 수치와 필터 결과는 본문 및 finding에서 1차 출처 보고값으로 한정했다.
