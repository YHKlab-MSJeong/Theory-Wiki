# 품질 근거: nonorthogonal-kpm.md

- 대상 문서: `docs/computational-materials-science/quantum-transport/nonorthogonal-kpm.md`
- 검토 범위: 비직교 기저 KPM 연산, Chebyshev DOS, 전자수 조건의 Fermi 준위, HamGNN-NEGF 내 역할 및 적용 한계
- 출처 유형: 1997년 비직교 KPM 논문, 2006년 KPM 리뷰, 2026년 9월 29일 arXiv v1 preprint
- 독립 검토: `kpm_dfth_science_review`, 과학 주장·식·원문 위치 재검토, 2026-11-08
- 그림: `nonorthogonal-kpm-workflow.svg`는 연산자 적용, moment, 평활 DOS와 전자수 조건의 순서를 원문을 바탕으로 새로 그렸다. editable source는 `refs/quality/figure-source/nonorthogonal-kpm-workflow.html`이다.
- 문체: humanizer 검토 후 수식, 변수, 수렴 조건, 주장 범위를 다시 확인했다.

## 주장과 근거

1. **비직교 Kohn–Sham 문제는 일반화 고유값 문제로 표현되며, 비직교 KPM은 전체 고유값을 직접 구하지 않고 moments로 DOS를 근사한다.**
   - 범위: 양의 정부호 overlap을 갖는 비직교 기저의 스펙트럼 계산.
   - 판정: supported.
   - 근거: Röder et al. (1997), Eqs. (1)–(9); Weiße et al. (2006), §§2–4.
2. **Röder 등의 비직교 구현은 행렬 작용에서 overlap 선형계를 풀며, PCG로 이를 수행하고 (S^{-1})을 조밀 행렬로 명시 구성하지 않는다.**
   - 범위: 인용한 비직교 KPM 구현의 연산 경로.
   - 판정: reported-primary.
   - 근거: Röder et al. (1997), Eqs. (7)–(9), pp. 15383–15385.
3. **Chebyshev moment 수와 무작위 trace 벡터 수는 각각 스펙트럼 해상도와 확률적 trace 오차에 영향을 주고, kernel은 DOS의 delta 피크를 유한 폭으로 평활화한다.**
   - 범위: KPM DOS 근사의 수치 해상도와 stochastic trace.
   - 판정: supported.
   - 근거: Röder et al. (1997), Eqs. (2)–(9); Weiße et al. (2006), §§2–4.
4. **전자수 적분과 점유 함수에 대한 목표 조건을 풀어 Fermi 준위를 정하며, HamGNN-NEGF 논문은 이를 비직교 KPM 단계로 RGF transmission 계산과 구분한다.**
   - 범위: 해당 모델에서 주어진 Hamiltonian·overlap 및 점유 정의에 대한 (\mu_F); KPM 자체는 transmission solver가 아니다.
   - 판정: supported.
   - 근거: Röder et al. (1997), pp. 15384–15385; Liu et al. (2026), §II, Fig. 1.
5. **HamGNN preprint Results p. 5는 (2\times2\times5) Si 사례에서 KPM 수렴과 이후 NEGF 사용을 서술하고, Methods p. 12는 benchmark Fermi 준위를 직접 대각화로 얻었다고 서술한다.**
   - 범위: 두 구절이 어떻게 연결되는지 preprint가 설명하지 않으므로, 모든 transmission benchmark의 절차를 하나로 판정하지 않는다.
   - 판정: reported-primary.
   - 근거: Liu et al. (2026), Results p. 5, Supplementary Table 1; Methods p. 12.
6. **HamGNN 논문은 희소 행렬에 대해 KPM 비용을 (O(N_{\rm mom}N_{\rm rand}N))으로 제시하지만, 비직교 구현에서는 overlap 선형계 풀이 비용도 실제 계산 시간에 들어간다.**
   - 범위: 고정된 moment·random-vector·수렴 설정의 점근 비교이며 PCG 반복 수는 별도 영향을 준다.
   - 판정: supported.
   - 근거: Liu et al. (2026), §II; Röder et al. (1997), Eqs. (7)–(9).

## 미해결 범위

- HamGNN preprint는 KPM DOS 계산이 에너지 의존 전극 self-energy를 포함하는지 명확히 설명하지 않는다. 문서는 open-system DOS라고 단정하지 않는다.
- KPM의 해상도, 무작위 trace 오차, overlap solve 허용오차는 서로 다른 오차원이다. 문서에서는 이를 하나의 수렴량으로 합치지 않는다.
- meV 수준 Fermi 준위 오차는 논문이 제시한 구조와 설정에 관한 보고값이며 다른 물질·기저의 보증값이 아니다.
