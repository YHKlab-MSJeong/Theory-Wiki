# 품질 근거: dfpt-dielectric-response.md

- 대상 문서: `docs/computational-materials-science/dielectric-response/dfpt-dielectric-response.md`
- 판정 범위: 전체 문서, 신규 작성
- 검토 기준: 두 독립 과학 출처와 원문 귀속 결과를 구분한다.
- 문서 SHA-256: `7d49f075feabd5eecdbbe523d1a793f83f5f555f4cc26c46150f6b33d775d4ca`

## 문서 범위와 질문

- 목적: DFPT의 전자·원자 선형 응답에서 유전 텐서를 계산하고 검토하는 기준을 정리한다.
- 독자: 재료·DFT 기본 개념을 아는 연구자.
- 제외: 실험 재현, 특정 공정의 합성 가능성, 범용 ML 정확도 보증.

## 주장과 근거

1. **주장:** DFPT의 1차 파동함수·밀도 응답으로 BEC, 전자 유전 텐서와 동역학 행렬 등 2차 에너지 미분량을 얻는다.
   - **범위:** DFT 기반 선형 응답과 조화 결정 격자
   - **판정:** `supported`
   - **출처:** gonze (Abstract; §III dynamical matrices; §IV electronic dielectric tensor; §V BEC; §VII sum rule; §VIII low-frequency response), baroni (§§II.3.2, II.4.2–4.3; §V.6 anharmonic effects)
2. **주장:** 정적 유전율의 이온 항에는 BEC와 Γ점 포논 모드가 들어가고, 수치 규약·수렴 설정을 별도로 확인해야 한다.
   - **범위:** 조화 절연체, 계산별 단위·질량 정규화 명시
   - **판정:** `supported`
   - **출처:** gonze (Abstract; §III dynamical matrices; §IV electronic dielectric tensor; §V BEC; §VII sum rule; §VIII low-frequency response), baroni (§§II.3.2, II.4.2–4.3; §V.6 anharmonic effects)
3. **주장:** 선형 조화 응답의 수렴은 상 안정성, 박막 계면 성능 또는 비조화 효과 검증을 대신하지 않는다.
   - **범위:** 모델 범위와 재료·소자 주장 구분
   - **판정:** `supported`
   - **출처:** baroni (§§II.3.2, II.4.2–4.3; §V.6 anharmonic effects), stengel (Main text on electric displacement, dielectric response and structural regimes)

## 가정과 한계

- 논문별 수치·후보는 해당 원문이 보고한 결과로만 기록했다. 독립 재현·합성·소자 검증으로 표현하지 않았다.
- 유전율 식은 본문에 적은 SI 단위, 구조, 선형·조화 근사와 모드 정규화에 한정한다.
- 원본 문헌의 그림을 복제하지 않았다. SVG는 개념 관계를 새로 그린 저작 도식이며, 아래 원문들은 물리 관계의 검증 근거다.

## 독립 검토

- 상태: pass; 전 문서와 적용된 그림 최종본 검토 완료.
- 독립 검토: dielectric_literature가 최종 문서의 과학 내용·인용·절 번호·수치와 원문을 대조했다.
- 독립 재현하지 않은 논문 고유 수치와 필터 결과는 본문 및 finding에서 1차 출처 보고값으로 한정했다.
