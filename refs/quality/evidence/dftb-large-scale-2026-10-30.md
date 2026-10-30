# DFTB large-scale atomistic simulation 검증 기록

대상: `docs/computational-science/atomistic-simulation/dftb-large-scale.md`  
대상 SHA-256: `3561f23ebf9c3bebd45c9487b44a5ea7c5ea4f67eb53b432f43fa6db57f90fe2`

범위는 유한 비주기 SCC-DFTB2의 개략 에너지식, SCC charge, large-scale 계산의 scaling 주의와 parameter validation이다. 주기계의 전체 에너지식, 특정 parameter set의 정량 정확도, 특정 DFTB implementation의 성능 수치는 주장하지 않는다.

| 주장 | 대조 근거 | 판정 |
| --- | --- | --- |
| SCC-DFTB2의 2차 charge expansion, \(\gamma\), repulsive potential, Mulliken SCC | Yang et al. §II pp. 10862–10864; Hourahine et al. §II | supported |
| solver·Coulomb 처리에 따라 scaling이 달라져 일반 linear scaling을 보장할 수 없음 | Hourahine et al. §II; Aradi et al. abstract | supported |
| parameter transferability는 target observable로 별도 확인해야 함 | Zobelli et al. §II–IV Table I–II; Yang et al. §II | supported |

독립 검토자 `landauer_review`가 pair-repulsive 식의 비주기계 한정과 periodic image·k-point 경계를 지적했다. 작성자는 이를 본문에 명시했다. reviewer 환경에서는 Hourahine DOI 원문에 직접 접근하지 못했으므로, 해당 출처의 서지·범위는 작성자 조사 결과로 기록하고 reviewer가 직접 확인한 Yang 식과 구분한다. humanizer 점검은 과학적 조건과 수식을 보존했다. 그림·수치 예제는 없다.

1. Y. Yang et al., *Extension of the Self-Consistent-Charge Density-Functional Tight-Binding Method* (2007), §II, pp. 10862–10864, https://theory.rutgers.edu/resources/pdfs/Yang_JPhysChemA_2007_v111_p10861.pdf.
2. B. Hourahine et al., *DFTB+, a software package for efficient approximate density functional theory based atomistic simulations*, J. Chem. Phys. **152**, 124101 (2020), §II, https://doi.org/10.1063/1.5143190.
3. B. Aradi et al., *DFTB+: A sparse matrix-based implementation of the DFTB method* (2007), abstract, https://pureportal.strath.ac.uk/en/publications/dftb-a-sparse-matrix-based-implementation-of-the-dftb-method/.
4. A. Zobelli et al. (2012), §II–IV, https://arxiv.org/pdf/1207.3194.
