# 품질 근거: ml-born-effective-charge.md

- 대상 문서: `docs/computational-materials-science/dielectric-response/ml-born-effective-charge.md`
- 판정 범위: 전체 문서, 신규 작성
- 검토 기준: 두 독립 과학 출처와 원문 귀속 결과를 구분한다.
- 문서 SHA-256: `20126b7d689cf6d9439e7882f0e6eb31ace7a3881810835aa90b676f1627c023`

## 문서 범위와 질문

- 목적: SevenNet-Polar의 Born 유효전하 예측 범위와 유전율 계산에서의 입력 역할을 구분한다.
- 독자: 재료·DFT 기본 개념을 아는 연구자.
- 제외: 실험 재현, 특정 공정의 합성 가능성, 범용 ML 정확도 보증.

## 주장과 근거

1. **주장:** SevenNet-Polar 논문은 BEC 전용 예측과 에너지·힘·응력·BEC 다중과제 모델을 제시하고, BEC RMSE 0.0043e 및 0.0029e를 보고한다.
   - **범위:** 논문이 정의한 ZrO2, Li3PO4 및 perovskite 자료 분할의 결과이며 독립 재현값이 아님
   - **판정:** `reported-primary`
   - **출처:** seven (v3 Abstract; §§2–4, 2026-07-21; primary-research)
   - **판정 메모:** 1차 연구 논문에 귀속한 보고값이며 독립 재현 결과가 아니다.
2. **주장:** BEC만으로 전체 유전 텐서를 얻을 수 없고, 포논 모드와 전자 응답이 추가로 필요하다.
   - **범위:** bulk polar crystal, 선형·조화 응답
   - **판정:** `supported`
   - **출처:** gonze (Abstract; §III dynamical matrices; §IV electronic dielectric tensor; §V BEC; §VII sum rule; §VIII low-frequency response), baroni (§§II.3.2, II.4.2–4.3; §V.6 anharmonic effects)
3. **주장:** 시험 분할 점수와 학습 분포가 달라지는 조건의 일반화는 다른 검증 질문이다.
   - **범위:** 원문 benchmark와 일반적인 distribution shift 평가 경계
   - **판정:** `supported`
   - **출처:** seven (v3 Abstract; §§2–4, 2026-07-21; primary-research), wilds (Abstract; distribution shifts and in-/out-of-distribution evaluation)

## 가정과 한계

- 논문별 수치·후보는 해당 원문이 보고한 결과로만 기록했다. 독립 재현·합성·소자 검증으로 표현하지 않았다.
- 유전율 식은 본문에 적은 SI 단위, 구조, 선형·조화 근사와 모드 정규화에 한정한다.
- 원본 문헌의 그림을 복제하지 않았다. SVG는 개념 관계를 새로 그린 저작 도식이며, 아래 원문들은 물리 관계의 검증 근거다.

## 독립 검토

- 상태: pass; 전 문서와 적용된 그림 최종본 검토 완료.
- 독립 검토: dielectric_literature가 최종 문서의 과학 내용·인용·절 번호·수치와 원문을 대조했다.
- 독립 재현하지 않은 논문 고유 수치와 필터 결과는 본문 및 finding에서 1차 출처 보고값으로 한정했다.
