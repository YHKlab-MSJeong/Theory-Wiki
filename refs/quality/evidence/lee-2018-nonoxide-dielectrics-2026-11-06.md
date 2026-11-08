# 품질 근거: lee-2018-nonoxide-dielectrics.md

- 대상 문서: `docs/computational-materials-science/dielectric-response/lee-2018-nonoxide-dielectrics.md`
- 판정 범위: 전체 문서, 신규 작성
- 검토 기준: 두 독립 과학 출처와 원문 귀속 결과를 구분한다.
- 문서 SHA-256: `aca83a58f3600eda9745771d2fd8062d927749776b7552c58753efa205456818`

## 문서 범위와 질문

- 목적: Lee 등 2018년 비산화물 유전체 스크리닝의 계산 대상과 후보 주장 범위를 정리한다.
- 독자: 재료·DFT 기본 개념을 아는 연구자.
- 제외: 실험 재현, 특정 공정의 합성 가능성, 범용 ML 정확도 보증.

## 주장과 근거

1. **주장:** Lee 등은 869개 이원 화합물, 절연체 449개, 삼원 불화물 415개를 조사했다고 보고한다.
   - **범위:** 원문 보고 수치이며 독립 재현 주장은 하지 않음
   - **판정:** `reported-primary`
   - **출처:** lee (Abstract; Methods; Results; primary-research)
   - **판정 메모:** 1차 연구 논문에 귀속한 보고값이며 독립 재현 결과가 아니다.
2. **주장:** Lee 등은 BaBeF4에 대해 밴드갭 9.7 eV와 유전율 17을 보고한다.
   - **범위:** 특정 구조와 원문 계산 설정의 문헌 보고값이며 독립 재현이 아님
   - **판정:** `reported-primary`
   - **출처:** lee (Abstract; Methods; Results; primary-research)
   - **판정 메모:** 1차 연구 논문에 귀속한 보고값이며 독립 재현 결과가 아니다.
3. **주장:** DFPT 계산은 Born 유효전하·포논 응답을 포함해 격자 유전 기여를 평가한다.
   - **범위:** 조화 절연체, 원문에 기술된 VASP/DFPT pipeline
   - **판정:** `supported`
   - **출처:** lee (Abstract; Methods; Results; primary-research), gonze (Abstract; §III dynamical matrices; §IV electronic dielectric tensor; §V BEC; §VII sum rule; §VIII low-frequency response)
4. **주장:** bulk screening에서 후보로 제안된 사실은 실험적 소자 성능을 보증하지 않는다.
   - **범위:** 재료 평가 단계의 경계
   - **판정:** `supported`
   - **출처:** lee (Abstract; Methods; Results; primary-research), robertson04 (Eq. (1), §§1–2; high-k gate dielectric constraints)

## 가정과 한계

- 논문별 수치·후보는 해당 원문이 보고한 결과로만 기록했다. 독립 재현·합성·소자 검증으로 표현하지 않았다.
- 유전율 식은 본문에 적은 SI 단위, 구조, 선형·조화 근사와 모드 정규화에 한정한다.
- 문서에는 Lee et al. Fig. 4와 Fig. 5를 재사용했다. 각 도판의 라이선스, 원본 PDF, crop 범위와 해시는 `paper-figure-reuse-2026-11-08.md`에 기록했다. 별도 SVG 개념도는 위키가 새로 그렸다.

## 독립 검토

- 상태: pass; 전 문서와 적용된 그림 최종본 검토 완료.
- 독립 검토: dielectric_literature가 최종 문서의 과학 내용·인용·절 번호·수치와 원문을 대조했다.
- 독립 재현하지 않은 논문 고유 수치와 필터 결과는 본문 및 finding에서 1차 출처 보고값으로 한정했다.
