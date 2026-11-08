# 변경 검토: long-channel-transport.md

- 대상 문서: `docs/computational-materials-science/quantum-transport/long-channel-transport.md`
- 이전 문서 SHA-256 기준선: `e7da664b4f3807761be85246357d48d1860ab08496c65d194d65062303c825b7`
- 이전 교차 링크 검증: `refs/quality/evidence/long-channel-transport-crosslink-2026-11-08.md` (SHA-256 `ad31332ee4ecd3ea5517db479679bb0f3182d05de36343c0b73597a8fbdb4834`)
- 변경 범위: DFTH-NEGF와 비직교 KPM 전용 문서를 각각 정적 Hamiltonian 수송과 Fermi 준위 계산 단계로 연결했다. 과학적 정의나 수치는 추가하지 않았다.
- 독립 검토: `diagram_final_review`, 링크·역할 구분 확인, 2026-11-08.

## 판정

- DFTH-NEGF는 NEGF backend에서 고정 DFT Hamiltonian을 사용하고 열린계 수송 SCF Hamiltonian 되먹임을 생략하는 방법으로 소개한다.
- 비직교 KPM은 electron-number constraint에서 Fermi 준위를 찾는 단계로 소개한다.
- 두 문서 링크와 MkDocs 메뉴 경로가 실제 파일에 연결되는지 빌드로 다시 확인한다.
- 기존 블록 반복, Order-N DFT, 학습 Hamiltonian의 구분과 근거는 이전 기록에서 유지했다.
