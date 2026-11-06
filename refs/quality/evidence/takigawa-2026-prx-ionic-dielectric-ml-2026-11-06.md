# 품질 근거: takigawa-2026-prx-ionic-dielectric-ml.md

- 대상 문서: `docs/computational-materials-science/dielectric-response/cases/takigawa-2026-prx-ionic-dielectric-ml.md`
- 판정 범위: 전체 문서, 신규 작성
- 검토 기준: 두 독립 과학 출처와 원문 귀속 결과를 구분한다.
- 문서 SHA-256: `5567a088436276e59b7637a74a01f88f35c87a7bdaec2e73eb9f2c4eae80cbe5`

## 문서 범위와 질문

- 목적: Takigawa 등 2026년 PRX의 factorized ML과 이온 유전 텐서 산출 경로를 설명한다.
- 독자: 재료·DFT 기본 개념을 아는 연구자.
- 제외: 실험 재현, 특정 공정의 합성 가능성, 범용 ML 정확도 보증.

## 주장과 근거

1. **주장:** 2026 PRX 논문은 BEC와 포논 물성을 factorize해 이온 유전 텐서를 계산하고 전자 유전 기여를 별도로 예측하는 joint model을 제시한다.
   - **범위:** 모델 구성에 대한 원문 보고이며 독립 재현 주장은 하지 않음
   - **판정:** `reported-primary`
   - **출처:** prx (Abstract; §I notation; §II.A Eq. (2) Fig. 3; §II.B Eq. (3) Fig. 4 and Table III; primary-research)
   - **판정 메모:** 1차 연구 논문에 귀속한 보고값이며 독립 재현 결과가 아니다.
2. **주장:** 논문은 direct model과 joint model을 839개 Γ점 안정 산화물에서 5-fold CV로 비교하고 log10 고유값 오차 R²/RMSE를 보고한다.
   - **범위:** 논문 정의 데이터 분할의 결과이며 독립 재현값으로 취급하지 않음
   - **판정:** `reported-primary`
   - **출처:** prx (Abstract; §I notation; §II.A Eq. (2) Fig. 3; §II.B Eq. (3) Fig. 4 and Table III; primary-research)
   - **판정 메모:** 1차 연구 논문에 귀속한 보고값이며 독립 재현 결과가 아니다.
3. **주장:** 논문은 후보 풀 8,717개에서 Γ점 안정성 확인 후 4,654개, ML 유전율·r2SCAN 밴드갭 선별 142개, PBEsol-DFPT 확인 121개를 거쳐 DFPT 유전율과 DDH 밴드갭의 최종 FOM 기준으로 31개 후보를 남겼다고 보고한다.
   - **범위:** 논문이 정의한 순차 screening 수치·기준이며 독립 재현 주장은 하지 않음
   - **판정:** `reported-primary`
   - **출처:** prx (Abstract; §I notation; §II.A Eq. (2) Fig. 3; §II.B Eq. (3) Fig. 4 and Table III; primary-research)
   - **판정 메모:** 1차 연구 논문에 귀속한 보고값이며 독립 재현 결과가 아니다.
4. **주장:** 논문이 제시한 후보 탐색은 계산 기반 screening이며 실험 합성·박막 검증과 구분된다.
   - **범위:** 논문이 보고한 screening 결과와 후보물성 산출 경계
   - **판정:** `supported`
   - **출처:** prx (Abstract; §I notation; §II.A Eq. (2) Fig. 3; §II.B Eq. (3) Fig. 4 and Table III; primary-research), robertson06 (Review sections on dielectric constant, band gap, offsets and interfaces)

## 가정과 한계

- 논문별 수치·후보는 해당 원문이 보고한 결과로만 기록했다. 독립 재현·합성·소자 검증으로 표현하지 않았다.
- 유전율 식은 본문에 적은 SI 단위, 구조, 선형·조화 근사와 모드 정규화에 한정한다.
- 원본 문헌의 그림을 복제하지 않았다. SVG는 개념 관계를 새로 그린 저작 도식이며, 아래 원문들은 물리 관계의 검증 근거다.

## 독립 검토

- 상태: pass; 전 문서와 적용된 그림 최종본 검토 완료.
- 독립 검토: dielectric_literature가 최종 문서의 과학 내용·인용·절 번호·수치와 원문을 대조했다.
- 독립 재현하지 않은 논문 고유 수치와 필터 결과는 본문 및 finding에서 1차 출처 보고값으로 한정했다.
