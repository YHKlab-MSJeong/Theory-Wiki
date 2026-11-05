# Scattering QTBM 문서 검증 기록

대상: docs/computational-materials-science/quantum-transport/scattering-qtbm.md
대상 SHA-256: d331be396872b0417a5a8aaf47be3df95e53735a3e6ae30486cc97bba4b1a9fb
기준 문서 SHA-256: 57d16c75a0fe3fc3fdf1ed7d617f011b348aa60a91286aebddcf93b72498657b
이전 검증 기록: refs/quality/evidence/scattering-qtbm-2026-10-30.md
이전 기록 SHA-256: bb9688662e56eadc0ea3a6ab25a0b31cf8f1f3f774c8eda31d56272be50b20b3

## 검토 범위와 판정

문서를 QTBM 기본 소개부터 다시 구성했다. 입사·반사·투과 상태, 열린 경계와 주입 source, 비직교 기저에서의 overlap 항, flux transmission, reservoir 점유 가중 모드 전류, NEGF와의 관계, 별도 산란 closure 순서로 설명한다. Mode matching에 필요한 evanescent mode와 먼 lead에서 flux를 전달하는 propagating channel의 역할을 구분했다. QTBM은 각 에너지에서 산란 상태를 구하므로 그림의 reservoir-weighted mode current에 에너지 적분을 명시했다. Gehring 인용은 HTML 절과 식 번호가 맞지 않아 저장소 PDF로 고쳤다. QTBM 자체와 모델에 따라 추가되는 산란 방정식의 범위를 분리했다.

| 검토 주장 | 독립 대조 근거 | 판정 |
|---|---|---|
| QTBM은 지정한 입사 lead mode의 정상상태 산란 문제를 에너지 의존 열린 경계와 입사 source로 푼다. | Frensley Appendix D 식 (D1)–(D6); Gehring §3.5.4 식 (3.92)–(3.99); Shao et al. §II 식 (2) | supported |
| 비직교 기저의 열린 경계 연산자에는 central overlap과 lead-device overlap coupling이 들어가며, 주입 source의 상세 형태는 구현 convention에 의존한다. | Lake–Pandey §VI.C–D; Papior et al. §II 식 (1)–(4); Shao et al. §II 식 (2) | supported |
| Transmission은 출사 대 입사 flux 비이며, 단순 진폭 제곱은 unit-flux normalization에서만 바로 쓸 수 있다. | Gehring §3.5 식 (3.55)–(3.56); Shao et al. §II | supported |
| 두 terminal의 순전류는 각 에너지에서 좌·우 reservoir 입사 mode의 signed occupation-weighted 기여를 합한 뒤 에너지에 대해 적분하며, 탄성·결맞음 한계에서 \(f_L-f_R\) 꼴 Landauer 식으로 나타난다. | Bruneau et al. §1.1 식 (1.2), (1.6); Kohler et al. §2.4 식 (16)–(18) | supported |
| 산란 closure는 QTBM 경계조건과 별도다. Pauli master equation을 결합한 QTBM 연구는 한 구체적 사례다. | Vyas et al. 초록; Weinbub–Kosik §7.4 | supported |
| 허수 흡수항 \(-iW\)만으로 대응 in-scattering과 재주입이 정해지지 않는다. | Kosik §7.2.6.1, 식 (7.22)–(7.25); Heinz §4.5 | supported |
| Evanescent mode는 경계 mode matching에 필요할 수 있고, 독립적인 먼-lead flux 채널은 아니지만 꼬리가 central region을 가로지르면 2단자 전류에 영향을 줄 수 있다. | Khomyakov et al. §III.A–B, 식 (4)–(17); Sørensen et al. §II.A, §III.A | supported |

## 그림 재현 및 무결성

- HTML source: refs/quality/figure-source/qtbm-workflow.html
- HTML source SHA-256: 79cf23482c9d85de2d25ae7476004709878f287dbd2aa1043db8ba29fe6845d4
- SVG: docs/assets/qtbm-workflow.svg
- SVG SHA-256: 8333b6f4447a4fb2111bfcbddfbcbe7553bedadd65fbf10f5ed0b45c902bc117
- diagram-design self-check와 SVG export가 통과했다. Inkscape 미리보기에서 elastic QTBM과 optional scattering closure의 분리, 부호 있는 mode-current 합, 점선 경로, label 및 캔버스 잘림을 확인했다.
- 독립 검토: qtbm_citations_final (본문 인용과 식 번호, 2026-11-05), qtbm_delta_review (전류 부호 설명과 최종 도식 경로, 2026-11-05), qtbm_evanescent_review (evanescent mode의 matching·flux 역할 및 인용, 2026-11-05), wiki_transport_diagram_review (current의 에너지 적분, 2026-11-05). 최종 도식 수정 후 차단 사항 없음.

## 참고 자료

1. W. R. Frensley, “Boundary conditions for open quantum systems driven far from equilibrium,” Reviews of Modern Physics 62, 745–791 (1990), Appendix D, https://personal.utdallas.edu/~frensley/technical/FrensleyRMP1990.pdf.
2. A. Gehring, Simulation of Tunneling in Semiconductor Devices (2003), §3.5.4, https://repositum.tuwien.at/bitstream/20.500.12708/12170/2/Gehring%20Andreas%20-%202003%20-%20Simulation%20of%20tunneling%20in%20semiconductor%20devices.pdf.
3. Z.-a. Shao, W. Porod, C. S. Lent, and D. J. Kirkner, “An eigenvalue method for open-boundary quantum transmission problems,” Journal of Applied Physics 78, 2177–2186 (1995), §II, https://academicweb.nd.edu/~lent/pdf/nd/An_eigenvalue_method_for_open-boundary_quantum_transmission_problems.pdf.
4. R. K. Lake and R. R. Pandey, “Non-Equilibrium Green Functions in Electronic Device Modeling” (2006), §VI.C–D, https://arxiv.org/pdf/cond-mat/0607219.
5. P. B. Vyas, M. L. Van de Put, and M. V. Fischetti, “Master-Equation Study of Quantum Transport in Realistic Semiconductor Devices Including Electron-Phonon and Surface-Roughness Scattering,” Physical Review Applied 13, 014067 (2020), https://doi.org/10.1103/PhysRevApplied.13.014067.
6. R. Kosik, Numerical Challenges on the Road to NanoTCAD (2004), §7.2.6.1–2, https://www.iue.tuwien.ac.at/phd/kosik/node96.html.
7. F. O. Heinz, Simulation Approaches for Nano-Scale Semiconductor Devices (2004), §4.5, https://iis-people.ee.ethz.ch/~schenk/theses/heinz.pdf.
8. L. Bruneau, V. Jakšić, Y. Last, and C.-A. Pillet, “Landauer-Büttiker and Thouless conductance,” Journal of Mathematical Physics 55, 075204 (2014), §1.1, https://arxiv.org/html/1408.0185.
9. S. Kohler, J. Lehmann, and P. Hänggi, “Driven quantum transport on the nanoscale,” Physics Reports 406, 379–443 (2005), §2.4, https://arxiv.org/pdf/cond-mat/0409251.
10. N. Papior, N. Lorente, T. Frederiksen, A. García, and M. Brandbyge, “Improvements on non-equilibrium and transport Green function techniques: the next-generation transiesta,” Computer Physics Communications 212, 8–24 (2017), §II, https://arxiv.org/pdf/1607.04464.
11. J. Weinbub and R. Kosik, “Computational perspective on recent advances in quantum electronics: from electron quantum optics to nanoelectronic devices and systems,” Journal of Physics: Condensed Matter 34, 163001 (2022), §7.4, https://doi.org/10.1088/1361-648X/ac49c6.

13. P. A. Khomyakov, G. Brocks, V. Karpan, M. Zwierzycki, and P. J. Kelly, “Conductance calculations for quantum wires and interfaces: mode matching and Green functions,” *Physical Review B* **72**, 035450 (2005), §§III.A–B, https://arxiv.org/pdf/cond-mat/0501609.
14. H. H. B. Sørensen, P. C. Hansen, D. E. Petersen, S. Skelboe, and K. Stokbro, “Efficient wave function matching approach for quantum transport calculations,” (2009), §II.A, §III.A, https://arxiv.org/pdf/0804.4306.
