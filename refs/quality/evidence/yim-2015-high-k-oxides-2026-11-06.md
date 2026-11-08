# 품질 근거: yim-2015-high-k-oxides.md

- 대상 문서: `docs/computational-materials-science/dielectric-response/yim-2015-high-k-oxides.md`
- 판정 범위: 전체 문서, 신규 작성
- 검토 기준: 두 독립 과학 출처와 원문 귀속 결과를 구분한다.
- 문서 SHA-256: `e2ae8c3cb75d9e61289c3b3549a635b54a82327ad7339cf25b6b920c707d5bef`

## 문서 범위와 질문

- 목적: Yim 등 2015년 high-throughput 산화물 스크리닝의 질문과 결과 해석 범위를 기록한다.
- 독자: 재료·DFT 기본 개념을 아는 연구자.
- 제외: 실험 재현, 특정 공정의 합성 가능성, 범용 ML 정확도 보증.

## 주장과 근거

1. **주장:** Yim 등은 초록·서론에서 1,800개 초과 또는 약 1,800개 산화물 구조를, Results에서 1,762개 계산 구조를 보고하고 Fig. 4에 1,158개를 표시한다.
   - **범위:** 원문 내부 표현 차이를 그대로 기록하며 독립 재현 주장은 하지 않음
   - **판정:** `reported-primary`
   - **출처:** yim (Abstract; Introduction; Methods; Results and Fig. 4; primary-research)
   - **판정 메모:** 1차 연구 논문에 귀속한 보고값이며 독립 재현 결과가 아니다.
2. **주장:** 연구의 재료 설계 문제는 유전율뿐 아니라 누설 억제를 위한 큰 밴드갭과 함께 후보를 고르는 것이다.
   - **범위:** 게이트 유전체 설계 맥락
   - **판정:** `supported`
   - **출처:** yim (Abstract; Introduction; Methods; Results and Fig. 4; primary-research), robertson06 (Review sections on dielectric constant, band gap, offsets and interfaces)
3. **주장:** 계산상 후보 통과는 박막·계면·공정 신뢰성의 검증을 뜻하지 않는다.
   - **범위:** 벌크 screening 결과의 적용 한계
   - **판정:** `supported`
   - **출처:** yim (Abstract; Introduction; Methods; Results and Fig. 4; primary-research), robertson04 (Eq. (1), §§1–2; high-k gate dielectric constraints)

## 가정과 한계

- 논문별 수치·후보는 해당 원문이 보고한 결과로만 기록했다. 독립 재현·합성·소자 검증으로 표현하지 않았다.
- 유전율 식은 본문에 적은 SI 단위, 구조, 선형·조화 근사와 모드 정규화에 한정한다.
- 문서에는 Yim et al. Fig. 4를 재사용했다. 라이선스, 원본 PDF, crop 범위와 해시는 `paper-figure-reuse-2026-11-08.md`에 기록했다. 별도 SVG 개념도는 위키가 새로 그렸다.

## 독립 검토

- 상태: pass; 전 문서와 적용된 그림 최종본 검토 완료.
- 독립 검토: dielectric_literature가 최종 문서의 과학 내용·인용·절 번호·수치와 원문을 대조했다.
- 독립 재현하지 않은 논문 고유 수치와 필터 결과는 본문 및 finding에서 1차 출처 보고값으로 한정했다.
