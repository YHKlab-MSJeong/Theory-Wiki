# 품질 근거: mode-space-transport.md

- 대상: `docs/computational-materials-science/quantum-transport/mode-space-transport.md`
- 검토 범위: 모드 기저 투영, overlap과 접촉 self-energy, 점유·밀도·전류, coupled/uncoupled-mode, 산란 근사, RGF 비용과 적용 범위.
- 독립 검토: `new_article_fact_review` 및 하위 `mode_space_factcheck`; 2026-11-08 최종 파일을 검토했다. full-BZ 적용 범위, bound-state broadening 표기, Lemus 근사 범위와 Papior 절·식 인용을 확인했다.
- 그림 검토: `paper_figure_audit`; 2026-11-08 Carrillo-Nuñez Fig. 2 crop, 출처, 허가, 본문 설명을 확인.
- 자체 도식 source: `refs/quality/figure-source/mode-space-workflow.html`.
- 논문 그림 재사용 기록: `refs/quality/evidence/paper-figure-reuse-2026-11-08.md`.

## 주장과 근거

1. **비직교 기저의 mode-space 투영은 Hamiltonian과 overlap을 함께 변환하며 접촉 결합과 self-energy도 같은 기저 규약을 따라야 한다.**
   - 범위: 완전 변환의 동등성과 모드 절단 뒤의 근사 차이를 구분한다.
   - 판정: supported.
   - 출처: Luisier et al. (2006), §II.B, Eqs. (9), (11)–(18); Ducry et al. (2019), pp. 69–70; Papior et al. (2017), §II.
2. **전극에 결합된 상태의 coherent lesser Green 함수는 reservoir 주입항으로 계산할 수 있지만, 전극과 분리된 bound-state 점유는 이 항만으로 정해지지 않을 수 있다.**
   - 범위: 두 단자 steady-state 식과 본문 convention.
   - 판정: supported.
   - 출처: Papior et al. (2017), §II.B, Eqs. (10)–(15); Brandbyge et al. (2002), §III.
3. **Uncoupled-mode 처리는 모드 간 결합을 추가로 제거하는 근사이고, mode-space의 basis truncation과 구분해야 한다.**
   - 범위: 결합된 mode-space 수송 및 Lemus et al.의 form-factor 근사.
   - 판정: supported.
   - 출처: Luisier et al. (2006), §II.B; Lemus et al. (2020), §§2.3–2.6, 3.2–3.5.
4. **RGF의 층 방향 선형 비용은 블록 폭을 고정했을 때의 한 에너지·횡방향 k점 계산에 해당한다.**
   - 범위: block-tridiagonal 산란영역, 층당 행렬 차원 고정.
   - 판정: supported.
   - 출처: Papior et al. (2017), §III.C.1, Eqs. (17)–(18); Wimmer and Richter (2009), Eqs. (9)–(12).
5. **Carrillo-Nuñez 등은 3 nm \(\langle111\rangle\) Si nanowire에 대해 논문이 표시한 에너지 창에서 full-band와 mode-space 밴드를 비교한다.**
   - 범위: 논문에 실린 구조·표본화·계산 조건의 보고 사실이며, 전류 정확도나 다른 구조로 일반화하지 않는다.
   - 판정: reported-primary.
   - 출처: Carrillo-Nuñez et al. (2020), Fig. 2, p. 5.

## 그림과 문체

- `mode-space-workflow.svg`는 위키가 새로 그린 개념도이며 paper figure가 아니다.
- Carrillo-Nuñez Fig. 2는 원래 축·범례·곡선을 보존한 crop이다. CC BY 4.0, 원문 위치와 crop 사실은 캡션 및 별도 재사용 기록에 적었다.
- Humanizer 문체 검토는 과학적 주장을 확대하지 않으며, 34편 전수 점검은 `humanizer-audit-2026-11-08.md`에 기록했다.
