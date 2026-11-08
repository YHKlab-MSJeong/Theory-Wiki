# 품질 근거: basis-set-validation-cases.md

- 대상 문서: docs/computational-materials-science/quantum-transport/basis-set-validation-cases.md
- 검토 범위: 신규 문서 전체
- 목적: basis 사용 보고, 직접 transmission 비교, 다른 Hamiltonian 표현 비교, mode-space 축소 사례의 범위를 분리한다.
- 각 수치와 사례는 아래 원 논문이 보고한 결과로 제한한다.
- 문서 SHA-256: 48b8105ddbc21838f569d1e3fcb4801bc56cb43fd35c6d81c51d525f49ebd553
- 검증 기록 SHA-256: registry에서 추적

## 주장과 근거

1. **MoS₂/산화물 사례의 원소별 reference/transport basis와 CB edge·defect-state 결과.**
   - 범위: Ducry et al. 2026의 CP2K/PBEsol 소자모델.
   - 판정: reported-primary.
   - 원 출처: Ducry et al., npj 2D Materials and Applications 10, 49 (2026), Methods and Supplementary Information.
2. **ReS₂ SZP/DZP 전송 비교의 조건과 정성적 판정.**
   - 범위: zigzag ReS₂, Lg=4 nm, Vg=-1.3 V, Supporting Information Fig. S1.
   - 판정: reported-primary.
   - 원 출처: Quhe et al., J. Mater. Chem. C 7, 1108 (2019), SI p. 1, Fig. S1.
3. **WSe₂ band 계산과 Au|WSe₂ 수송에 사용한 서로 다른 basis 선택 및 검증 한계.**
   - 범위: Sassi et al. (2025), Methods.
   - 판정: reported-primary.
   - 원 출처: Sassi et al., ACS Applied Electronic Materials 7 (2025), Methods.
4. **Afzalian et al.의 QE+Wannier/OpenMX device comparison과 SZP/DZP basis-convergence 구분.**
   - 범위: WS₂ device ID–VG 사례 및 저자 목록.
   - 판정: reported-primary.
   - 원 출처: Afzalian et al., IEEE Transactions on Electron Devices (2021), Fig. 1 and §§II–III.
5. **VASP-to-Wannier metal/MoS₂ contact workflow와 보고된 정렬 및 k sampling 조건.**
   - 범위: Szabó et al. (2019), §§II–III.
   - 판정: reported-primary.
   - 원 출처: Szabó et al., Nano Letters 19, 3647 (2019).
6. **Mode-space 축소 사례의 Cu band error와 interface-dependent current error.**
   - 범위: Ducry et al. (2019), pp. 70–72, Figs. 2 and 4; basis cardinality 축소로 분류하지 않는다.
   - 판정: reported-primary.
   - 원 출처: Ducry et al., SISPAD (2019).

## 가정과 한계

- 사용 보고와 기저 수렴 검증을 문서에서 구분한다.
- 원문에 없는 quantitative convergence claim은 추가하지 않는다.
- 논문 결과를 사용자의 MoS₂/Au/SZP 구조에 대한 검증으로 일반화하지 않는다.
- 논문 figure를 복제하지 않고 수치·방법을 서술한다.

## 독립 검토

- basis/solver reviewer가 paper claims, numerical conditions, and source locations를 대조했다.
- 한국어 표현을 humanizer 기준으로 다듬고 문헌의 주장 강도와 적용 범위를 재확인했다.
