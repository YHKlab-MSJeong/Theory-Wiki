# NEGF 계산 흐름도 검증 기록

대상: docs/computational-materials-science/quantum-transport/negf.md
대상 SHA-256: df333a7f89af78645d793f77d93891d0f716bd50241b6ae67ab1ffe9b4ff2598
기준 문서 SHA-256: 295dc1507854ad621b2b31277e8c80d96eb878be8c866e2fda15945b3daa66a0
이전 검증 기록: refs/quality/evidence/negf-2026-10-28.md
이전 기록 SHA-256: 28668709c323386ca6ef65d77ffeb8a7add4b61e74b63e40b8e0e3ab1c1e0861

## 변경 범위와 판정

정상상태 2단자 NEGF의 기존 과학 서술은 유지하고, 도식의 입력과 관측량 경로를 다시 분리했다. lead의 Hamiltonian·overlap·결합은 retarded self-energy와 broadening으로, reservoir 점유는 lesser self-energy로 표시했다. current 출력에는 전체 lead-current 식을 쓴다는 설명을 넣었다. 그림은 새로 그린 개념도다.

| 검토 주장 | 원문 위치 | 판정 |
|---|---|---|
| lead 구조와 결합이 \(\\Sigma^r\) 및 \(\\Gamma\)를 정하고, reservoir 점유는 \(\\Sigma^< = if\\Gamma\)에 들어간다. | Papior et al. §II 식 (1)–(4); SIESTA 5.4 NEGF equations; Lee–Sanvito §II 식 (2)–(9) | supported |
| \(G^<\)로부터 전하밀도를 계산하지만 terminal current는 전체 lead-current 식의 Green 함수와 self-energy를 사용한다. | Jauho–Wingreen–Meir 식 (18)–(19); Papior et al. §IV.A | supported |
| Poisson/Hamiltonian 갱신은 NEGF 단독의 필수 내부 단계가 아니라 결합 계산의 선택적인 바깥 반복이다. | Papior et al. §III.B; Brandbyge et al. §V | supported |

## 그림 재현 및 무결성

- HTML source: refs/quality/figure-source/negf-workflow.html
- HTML source SHA-256: e8ccbc3fc02b36480cc1a996f8c7740d937be8df628cefd6a5a48266e2dcc132
- SVG: docs/assets/negf-workflow.svg
- SVG SHA-256: 7b09623a14e4e32579c94fa40e584eb22d7421e313bd5d872189d494d2267f7a
- diagram-design 접근성·문서 무결성 self-check와 SVG export가 통과했다. Inkscape 미리보기에서 두 입력 경로, Gamma 연결, terminal-current label 및 캔버스 잘림을 확인했다.
- 독립 최종 검토: diagram_final_review와 wiki_transport_diagram_review (NEGF 입력 분리, density·full lead-current trace 구분, 2026-11-05). 차단 사항 없음.

## 참고 자료

1. N. Papior et al., “Improvements on non-equilibrium and transport Green function techniques: the next-generation transiesta,” Computer Physics Communications 212, 8–24 (2017), §II, §III.B, §IV.A, https://arxiv.org/pdf/1607.04464.
2. SIESTA developers, NEGF equations, SIESTA 5.4 Reference Manual, https://docs.siesta-project.org/projects/siesta/en/5.4/reference/siesta.html#negf-equations.
3. W. Lee and S. Sanvito, “Exploring the limits of the self consistent Born approximation for inelastic electronic transport” (2008), §II, 식 (2)–(9), https://arxiv.org/pdf/0804.3389.
4. A.-P. Jauho, N. S. Wingreen, and Y. Meir, “Time-dependent transport in interacting and noninteracting resonant-tunneling systems,” Physical Review B 50, 5528–5544 (1994), 식 (18)–(19), https://arxiv.org/pdf/cond-mat/9404027.
5. M. Brandbyge et al., “Density-functional method for nonequilibrium electron transport,” Physical Review B 65, 165401 (2002), §V, https://arxiv.org/pdf/cond-mat/0110650.
