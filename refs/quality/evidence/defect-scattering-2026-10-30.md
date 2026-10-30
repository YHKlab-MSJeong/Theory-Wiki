# Defect scattering 검증 기록

대상: `docs/device-physics/mobility/defect-scattering.md`  
대상 SHA-256: `0ffb3f41377d4e10a492dcc45e5ab8211859e63c66dda8fcbd0b17873134d826`

범위는 charged impurity와 vacancy의 disorder potential, screening, Born-model normalization의 주의다. Si(111)과 monolayer MoS\(_2\)의 parameter를 상호 이전하지 않는다.

| 주장 | 대조 근거 | 판정 |
| --- | --- | --- |
| charged·neutral defect에는 전하 상태, 위치, screening을 분리해야 함 | Hwang–Das Sarma 식 (1)–(3); Kaasbjerg–Low–Jauho §II.A–B | supported |
| normalized matrix element, defect density, final-state sum을 함께 정의해야 함 | Hwang–Das Sarma 식 (1)–(3); Kaasbjerg–Low–Jauho 식 (10)–(13) | supported |

독립 검토자 `wiki_rules`가 단위가 닫히지 않은 보편 전이율 식을 지적했다. 작성자는 그 식을 삭제하고 normalization 의존성을 명시했다. humanizer 점검은 과학 내용을 바꾸지 않았다. 그림·수치 예제는 없다.

1. E. H. Hwang, S. Das Sarma, *Transport properties of two-dimensional electron systems on silicon (111) surfaces* (2006), pp. 1–2, https://arxiv.org/pdf/cond-mat/0608645.
2. K. Kaasbjerg, T. Low, A.-P. Jauho, *Electron and hole transport in disordered monolayer MoS2: atomic vacancy-induced short-range and Coulomb disorder scattering* (2016), §II, https://arxiv.org/pdf/1612.00469.
