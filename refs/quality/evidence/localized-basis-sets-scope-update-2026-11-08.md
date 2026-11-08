# 변경 검토: localized-basis-sets.md

- 대상 문서: `docs/computational-science/atomistic-simulation/localized-basis-sets.md`
- 이전 문서 SHA-256 기준선: `add66656416f75a1a024ceaf49cf7d52458e27497e1c85cb05c9bd2d1addd198`
- 이전 전체 검증: `refs/quality/evidence/localized-basis-sets-2026-11-08.md` (SHA-256 `6ad8194204d4331db8672ccc3e31eee44027ff74feafc1cb2922a7f4b369fc90`)
- 변경 범위: 개인의 특정 MoS2 계산에 대한 basis 권고와 적용 절을 제거하고, semicore·basis 설정 및 목표 물리량별 검증 절차를 일반 참고 내용으로 남겼다. MoS2가 포함된 문헌 제목은 연구 사례 인용으로만 남아 있다.
- 독립 검토: `kpm_dfth_science_review`, 2026-11-08.

## 유지된 주장

1. **Pseudopotential의 valence/semicore 선택은 basis의 radial zeta와 polarization 자유도와 구별된다.**
   - 판정: supported.
   - 출처: SIESTA 5.4 manual, “Basis sets,” “Basis generation,” “Basis size”; PSML specification, valence configuration and semicore metadata.
2. **수송 basis 선택은 큰 basis 재현만으로 판정하지 않고 목표 밴드·접촉 정렬·전송/전류의 관측량을 확인한다.**
   - 판정: supported.
   - 출처: Afzalian et al. (2021), §§II–III; Quhe et al. (2019), Supporting Information Fig. S1; Szabó et al. (2019), §§II–III.
3. **개별 밴드 또는 축소 표현의 일치만으로 접촉 transmission이 같다고 결론내릴 수 없다.**
   - 판정: supported.
   - 출처: Quhe et al. (2019), Supporting Information Fig. S1; Ducry et al. (2019), Figs. 2 and 4.

## 편집 경계

문서의 MoS2 문헌 인용은 연구 사례의 출처를 가리킨다. 사용자의 MoS2/Au 구조 또는 특정 ion의 정확도를 검증했다는 뜻으로 남기지 않았다.
