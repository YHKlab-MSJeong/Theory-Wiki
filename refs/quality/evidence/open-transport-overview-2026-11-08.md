# 품질 근거: 열린 경계 수송 overview

- 대상: `docs/computational-materials-science/quantum-transport/overview.md`
- 검토 범위: 두 단자 정상상태 탄성·결맞음 수송에서 NEGF, QTBM, Landauer 관계의 역할.
- 독립 검토: `new_article_fact_review`, 2026-11-08. 최종 도식도 두 단자 coherent·elastic charge-transport 설명과 대조했다.
- 도식: 원 논문 그림이 아닌 자체 개념도이며, 좌우 reservoir와 \(\Sigma_L,\Sigma_R\) 및 charge current를 표시한다. 도식과 편집 가능한 원본 해시는 `overview-diagrams-2026-10-31.md`의 2026-11-08 추가 기록을 참조한다.

## 주장과 근거

1. **NEGF는 열린 전극의 경계 self-energy와 상태·점유 계산을 다룬다.**
   - 범위: 독립전자 정상상태 수송의 두 단자 예시.
   - 판정: supported.
   - 출처: Papior et al. (2017), §II; Brandbyge et al. (2002), §§II–III.
2. **QTBM은 지정된 입사 전극 모드에서 출발하는 열린 경계 산란 상태를 푼다.**
   - 범위: stationary single-particle boundary formulation.
   - 판정: supported.
   - 출처: Frensley (1990), Appendix D; Gehring (2003), §3.5.4.
3. **두 단자 탄성·결맞음 Landauer 관계는 에너지별 transmission에 reservoir 점유 차이를 가중해 전류를 계산한다.**
   - 범위: 본문에서 명시한 독립전자 수송 조건.
   - 판정: supported.
   - 출처: Bruneau et al. (2014), §1.1, Eqs. (1.2), (1.6); Kohler et al. (2004/2005), §2.4, Eqs. (16)–(18).
4. **NEGF, QTBM, Landauer는 서로 다른 기술 관점이며 항상 한 계산에서 순차 실행되는 세 solver는 아니다.**
   - 범위: 이 문서의 독립전자 두 단자 개요.
   - 판정: supported.
   - 출처: Papior et al. (2017), §II; Brandbyge et al. (2002), §II; Frensley (1990), Appendix D.

## 한계

해밀토니안, 바이어스, 점유와 전류 부호 convention에 따라 세부 구현은 달라진다. 이 overview는 산란 self-energy나 상호작용 수송을 정의하지 않는다. 그림은 관계를 요약하며 독립 검증의 대체물이 아니다.
