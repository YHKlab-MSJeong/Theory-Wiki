# 품질 근거: localized-basis-sets.md

- 대상 문서: docs/computational-science/atomistic-simulation/localized-basis-sets.md
- 검토 범위: 신규 문서 전체
- 목적: semicore와 기저 유연성을 분리하고, 목표 수송 물리량을 기준으로 작은 원자궤도 기저를 비교하는 절차를 정리한다.
- 비포함: 사용자의 실제 MoS₂/Au 구조를 계산하거나 특정 SZP 기저를 검증하지 않는다.
- 문서 SHA-256: add66656416f75a1a024ceaf49cf7d52458e27497e1c85cb05c9bd2d1addd198
- 검증 기록 SHA-256: registry에서 추적

## 주장과 근거

1. **Semicore 전자 선택과 zeta/polarization basis 선택은 서로 다른 설정이다.**
   - 범위: PSML 전자 구성과 SIESTA 원자궤도 basis 정의.
   - 판정: supported.
   - 출처: SIESTA 5.4 reference manual, “Basis sets,” “Basis generation,” “Basis size”; PSML specification, valence and semicore metadata.
2. **작은 basis의 적합성은 DZP band 복제도만으로 정하지 않고, 목표 밴드·접촉 정렬·수송 관측량에서 확인한다.**
   - 범위: basis를 수송 계산에 사용할 때의 검증 설계.
   - 판정: supported.
   - 출처: Afzalian et al. (2021, §§II–III); Quhe et al. (2019, SI Fig. S1); Szabó et al. (2019, §§II–III).
3. **밴드 또는 중간표현의 적합이 장치 전류를 자동으로 보장하지 않는다.**
   - 범위: 계면·수송 비교와 축소모형의 판정 범위.
   - 판정: supported.
   - 출처: Quhe et al. (2019, SI Fig. S1); Ducry et al. (2019, pp. 70–72, Figs. 2, 4).

## 가정과 한계

- basis 비교에서 구조·pseudopotential·교환-상관 함수·k점·smearing 등 다른 입력 차이를 기록하도록 안내한다.
- 허용 오차는 관심 장치와 물리량에 따라 정하도록 했으며 보편 기준값을 제시하지 않는다.
- local PPS_ion_from_psml Mo 파일의 메타데이터나 실제 수송 결과를 공개 근거로 주장하지 않는다.

## 그림과 표현

- basis-validation-workflow.svg는 검증 단계를 요약한 자체 제작 도식이다. 문헌 그림을 복제하지 않았다.
- editable source: refs/quality/figure-source/basis-validation-workflow.html
- SVG 및 HTML source 해시는 registry에 기록한다.
- diagram-design self_check.py --offline 통과; Inkscape PNG 렌더링을 눈으로 확인했다.

## 독립 검토

- 별도 basis/solver 검토자가 문서와 cited sources를 대조했다.
- humanizer 검토 의견을 반영하고 기술 조건과 주장 강도를 다시 확인했다.
