# Surface-roughness scattering 검증 기록

대상: `docs/device-physics/mobility/surface-roughness-scattering.md`  
대상 SHA-256: `35380d50d6c935f2aaf907e8636ba427ffe25be2f5be017679273e16d4ba0675`

범위는 통계적 roughness model, correlation-length convention 및 Born/golden-rule의 ensemble-averaged matrix element다. 특정 계면의 \(\Delta_{\mathrm{rms}}\), \(\Lambda\), mobility를 예측하지 않는다.

| 주장 | 대조 근거 | 판정 |
| --- | --- | --- |
| exponential correlation의 \(\sqrt2\) 길이 convention과 spectrum | Badami Ch. 2 §2.2.2 식 (2.24)–(2.26); Sano §II.A 식 (3)–(5) | supported |
| \(S(q)\)는 ensemble-averaged \(|M|^2\)에 나타나며 통계 파라미터만으로 rate를 확정하지 못함 | Badami Ch. 2 §2.1 식 (2.1)–(2.2); Sano §II.C 식 (11) | supported |

독립 검토자 `wiki_rules`가 \(S(q)\)를 개별 matrix element에 직접 더한 표현과 직접 근거 없는 correlated-interface 절을 지적했다. 작성자는 전자를 ensemble average로 고치고 후자를 삭제했다. humanizer 점검은 식·조건·출처를 보존했다. 그림·수치 예제는 없다.

1. O. Badami, PhD thesis (2017), Ch. 2, https://air.uniud.it/retrieve/e27ce0c5-bae9-055e-e053-6605fe0a7873/Badami_PhDThesisUploaded.pdf.
2. N. Sano, *Microscopic Modeling of Surface Roughness Scattering in Inversion Layers of MOSFETs Based on Ando’s Linear Model* (2026 preprint), §II–III, https://arxiv.org/html/2604.22155.
