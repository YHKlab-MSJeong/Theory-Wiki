# 품질 근거: electronic-structure-solvers 그림 업데이트

- 대상: `docs/computational-science/atomistic-simulation/electronic-structure-solvers.md`
- 변경 범위: Hourahine et al. (2020) Fig. 5(c,d) 원그림 추가 및 해당 계산 조건 설명.
- 기준 버전 SHA-256: `4e5b996ed7aa843e6f18f8083a515a52d3c82a81b53d99657706a619e5fbb4c6`.
- 이전 전체 내용 검토: `electronic-structure-solvers-2026-11-08.md`.
- 독립 figure 검토: `paper_figure_audit`, 2026-11-08; 도판 범위와 캡션 확인.

## 추가 주장

- Fig. 5(c,d)는 C64000 CNT 및 Si6750 supercell의 non-self-consistent-charge, spin-non-polarized, Γ-point 계산에서 density-matrix construction 시간을 비교한다. 패널 (c)는 MKL·ELPA2·PEXSI, 패널 (d)는 MKL·ELPA2·NTPoly를 비교한다.
- 판정: reported-primary. 서로 다른 두 구조에 대한 서로 다른 solver 조합의 보고이므로 보편적인 성능 순위나 모든 solver에 대한 직접 비교로 일반화하지 않는다.
- 원문 위치: Hourahine et al. (2020), §III.A.1, Fig. 5(c,d), PDF p. 14. CC BY 4.0. crop와 PNG SHA는 `paper-figure-reuse-2026-11-08.md`에 기록했다.

기존 algorithm/solver 설명과 전체 과학 검토 범위는 이전 evidence를 유지한다.
