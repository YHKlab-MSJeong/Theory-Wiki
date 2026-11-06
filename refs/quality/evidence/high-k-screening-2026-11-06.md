# 품질 근거: high-k-screening.md

- 대상 문서: `docs/computational-materials-science/dielectric-response/high-k-screening.md`
- 판정 범위: 전체 문서, 신규 작성
- 검토 기준: 두 독립 과학 출처와 원문 귀속 결과를 구분한다.
- 문서 SHA-256: `547e0fc138ff7d6a2439174ed9f5dd14a1a2af39688a23b81bfd909015557afd`

## 문서 범위와 질문

- 목적: High-k 후보를 밴드갭과 계면·결함·안정성 조건을 포함해 해석한다.
- 독자: 재료·DFT 기본 개념을 아는 연구자.
- 제외: 실험 재현, 특정 공정의 합성 가능성, 범용 ML 정확도 보증.

## 주장과 근거

1. **주장:** 평행판 근사에서 같은 정전용량은 높은 유전율의 더 두꺼운 절연막으로 구현할 수 있다.
   - **범위:** 이상화된 gate stack capacitance 관계
   - **판정:** `supported`
   - **출처:** robertson04 (Eq. (1), §§1–2; high-k gate dielectric constraints), robertson06 (Review sections on dielectric constant, band gap, offsets and interfaces)
2. **주장:** 큰 유전율과 넓은 밴드갭, 밴드 오프셋 및 계면 안정성을 함께 고려해야 한다.
   - **범위:** 실제 게이트 스택 후보 선별
   - **판정:** `supported`
   - **출처:** robertson04 (Eq. (1), §§1–2; high-k gate dielectric constraints), robertson06 (Review sections on dielectric constant, band gap, offsets and interfaces)
3. **주장:** 제일원리 screening은 후보군을 좁히는 계산 단계이며 실험 박막·소자 검증과 같지 않다.
   - **범위:** 2015 산화물·2018 비산화물 탐색의 보고 범위
   - **판정:** `supported`
   - **출처:** yim (Abstract; Introduction; Methods; Results and Fig. 4; primary-research), lee (Abstract; Methods; Results; primary-research)

## 가정과 한계

- 논문별 수치·후보는 해당 원문이 보고한 결과로만 기록했다. 독립 재현·합성·소자 검증으로 표현하지 않았다.
- 유전율 식은 본문에 적은 SI 단위, 구조, 선형·조화 근사와 모드 정규화에 한정한다.
- 원본 문헌의 그림을 복제하지 않았다. SVG는 개념 관계를 새로 그린 저작 도식이며, 아래 원문들은 물리 관계의 검증 근거다.

## 독립 검토

- 상태: pass; 전 문서와 적용된 그림 최종본 검토 완료.
- 독립 검토: dielectric_literature가 최종 문서의 과학 내용·인용·절 번호·수치와 원문을 대조했다.
- 독립 재현하지 않은 논문 고유 수치와 필터 결과는 본문 및 finding에서 1차 출처 보고값으로 한정했다.
