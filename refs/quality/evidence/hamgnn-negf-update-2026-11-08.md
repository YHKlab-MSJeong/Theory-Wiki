# 변경 검토: hamgnn-negf.md

- 대상 문서: `docs/computational-materials-science/quantum-transport/hamgnn-negf.md`
- 이전 문서 SHA-256 기준선: `460a52db1467f6a1ef3701e164004008fe82ef6447ba12016ccf75bf1f9187a1`
- 이전 전체 검증: `refs/quality/evidence/hamgnn-negf-2026-11-08.md` (SHA-256 `146168ce00f6fb9a04b57deeced9c1d9f3c48720ef61016e37102f963acc7e95`)
- 변경 범위: KPM 절차의 설명을 전용 문서에 맞춰 정돈하고 Results p. 5와 Methods p. 12의 Fermi 준위 기술 차이를 각 적용 범위를 분리해 더 구체적으로 기록했다. 전체 문서는 독립 reviewer가 다시 대조했다.
- 독립 검토: `kpm_dfth_science_review`, 2026-11-08.

## 변경된 주장

1. **Results p. 5는 (2\times2\times5) Si에서 KPM 수렴 후 그 (E_F)를 이후 NEGF에 사용한다고 하고, Methods p. 12는 benchmark systems의 (E_F)를 직접 대각화로 얻었다고 한다.**
   - 판정: reported-primary.
   - 출처: Liu et al. (2026), Results p. 5, Supplementary Table 1; Methods p. 12.
   - 해석: preprint는 두 진술의 대상 관계를 설명하지 않는다. 각 구절을 별도로 보존하고 모든 transmission benchmark에 하나의 절차가 쓰였다고 추론하지 않는다.

## 재확인한 범위

- HamGNN 학습 label과 정적 Hamiltonian 예측, 전극 self-energy·KPM·RGF workflow, 고정 단면에서의 길이 스케일링, finite-bias (H_0) 제한, overlap (S) 구성의 문서화 부족은 이전 기록의 근거를 유지했다.
- 개인 장치에 관한 문구는 일반 적용 경계로 바꾸었다.
