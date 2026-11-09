# Hod D&C와 DeePTB-NEGF: 출처 및 독립 검토

- 목적과 독자: 긴 채널 수송과 국소 궤도·NEGF 기초를 공부하는 독자가 Hod의 고정 블록 반복 및 DeePTB-SK의 환경 의존 행렬 구성을 비교한다. 코드별 재현과 신규 DFT 계산은 범위 밖이다.
- 신규 문서: `hod-divide-and-conquer.md`, `deeptb-negf.md`; 전체 주장·식·예제·인용 검토. 기존 문서 세 개에는 의미를 바꾸지 않는 관련 문서 링크만 추가했다.
- 기준 해시: `hamiltonian-block-stitching.md` 88c02049080cb0a982a30d31ce0cead4dcd75cb1e67727eb5fee6bee8a378e98; `ml-hamiltonian-transport.md` 332c0e32bca79a342542a250d0c20660638c1c70b170a33f80f491837e3120eb; `long-channel-transport.md` e15e94b94d59c352bf68c608a49828b9e3ca2ba85641ffe3624710dc938c9d71. 이전 근거는 registry의 prior_evidence 참조.

## 주요 주장과 출처

- Hod 등의 원문에 귀속한 계산 절차 및 결과: `reported-primary`. [Hod et al. 2006](https://www.tau.ac.il/~odedhod/papers/paper8.pdf) §§II.A–D, III, Eqs. (3), (6)–(8), (16)–(24), Figs. 1–6. 가운데 PBC, 고립 L+m+R, 접촉 결합용 PBC를 구분했다. 18 단위의 초기 설명과 30 단위 비교를 구분했다. 상관계수는 보고된 에너지 구간 및 에너지 이동 조건을 포함한다.
- 열린계 전송식 및 비직교 kernel: `supported`. Hod §§II.A–C와 독립적으로 [Papior et al. 2017](https://arxiv.org/abs/1607.04464) §III. 양 끝 결합 가정에서 끝 블록을 이용한 투과식은 Hod Eq. (16).
- SK 행렬 및 각도 예제: `supported`. [Gu et al. 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11310461/) Results “Theoretical framework of DeePTB”, Eqs. (1)–(2), 독립 출처 [Slater and Koster 1954](https://doi.org/10.1103/PhysRev.94.1498) Table I. 자체 대입: l=1,m=0은 xx=Vσ, yy=Vπ, xy=0; l=m=1/√2은 xy=(Vσ−Vπ)/2.
- 환경 의존 SK·onsite·학습·CNT 수송의 구체 모형, 수치와 접촉 조건: `reported-primary`. [Zou et al. 2025](https://doi.org/10.1038/s41524-025-01853-6), Results “Theoretical framework and workflow”, “Open Boundary Conditions Treatment”, “NEGF formalism”, “NEGF-Poisson Self-Consistency”, “Application 2: Carbon nanotube field-effect transistor”, Methods “Datasets” and “Training Settings”, Eqs. (1), (3)–(8), Fig. 5, Supplementary §S4; [arXiv v3](https://arxiv.org/html/2411.08800v3). Gu 2024의 자체 모델 구성은 해당 원문 Eqs. (3)–(8). λ는 학습 중 결정되는 자유도. 9 nm 직경 비교에서 gate work function 보정과 도핑 접촉을 명시. 180 nm zero-bias와 41 nm FET 구분.
- 반복 행렬·Order-N DFT·환경별 예측의 차이: `supported`. Hod §II.C, [Soler et al. 2002](https://doi.org/10.1088/0953-8984/14/11/302) §14, Zou 2025 Results.

## 독립 검토 및 교정

- `hod` 검토자는 Hod 원문 §§II.A–D, III, Figs. 1–6 및 Papior/Soler 근거와 전체 문서를 대조했다. 고립 분자의 끝 onsite가 접촉 유도 전하와 전위의 완전 자기일관 재조정을 포함하지 않는다는 설명을 보완한 뒤 재검토 PASS.
- `deeptb` 검토자는 Gu 및 Zou 원문과 SK 식, 모형 구분, 학습과 장치 수치·출처 위치를 검토했다. 출처 절 이름, λ의 학습 단계, 다궤도 onsite의 단위행렬, 도핑 접촉 및 gate 일함수 보정을 수정한 뒤 전체 재검토 PASS.
- `wiki_audit` 검토자는 DeePTB SK 예제와 접촉·전송 범위를 독립 교차 검토하고 같은 교정을 권고했다. 자체 예제는 논문 계산값이 아니다.
- 문체는 humanizer 지침으로 다듬고 수치·조건·출처를 유지했다. 과학 검토는 문체 수정과 별개다. 새로운 계산 또는 독립 물리 재현은 수행하지 않았다.
