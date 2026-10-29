# Landauer–Büttiker 문서 검증 기록

대상: docs/computational-materials-science/quantum-transport/landauer-buttiker.md  
검토일: 2026-10-29  
대상 SHA-256: 968c206595e71fec96a186d0a0c96924c6a9f5e3a766ec39d798e1e385216f42

이 기록은 정상상태, 탄성·위상결맞음, 비상호작용 평형 reservoir라는 문서의 기준 모형에서 다중 전극 Landauer–Büttiker 식, 에너지·열 전류, \(B=0\) 선형 열전 응답, probe 경계조건을 원문과 대조한 결과다. 상호작용·비탄성 수송의 미시적 해, 특정 계산의 수렴, 특정 전극·DFT 모형의 물리적 타당성은 포함하지 않는다.

## 주장별 대조

| 검토 항목 | 대조한 근거와 판단 |
| --- | --- |
| 전송 방향과 NEGF trace | Papior et al. [1] §IV.A 식 (24)–(27)과 Meair–Jacquod [2] 식 (1a)를 대조했다. 문서는 \(T_{\alpha\beta}\)를 \(\alpha\to\beta\)로 정의하고 그에 맞게 \(J_\alpha^N\)의 유입·유출 항을 썼다. |
| 다중 전극 전하·에너지·열 전류 | Meair–Jacquod [2] 식 (1a)–(1b), Sánchez–Serra [4] 식 (2)–(7)을 대조했다. \(J^Q_\alpha=J^E_\alpha-\mu_\alpha J^N_\alpha\), 전하·에너지 보존과 유한 바이어스에서의 열 전류 합의 의미를 구별했다. |
| 선형 전기·열전 응답 | Meair–Jacquod [2] 식 (2)–(3) 및 Sánchez–Serra [4] 식 (2)–(7)을 대조했다. 문서는 \(\Theta>0\), 평형 transmission, \(B=0\)의 방향 대칭을 명시하고 \(\mathcal G\), \(\mathcal L\), \(\mathcal K\)와 \(J^Q\)의 1차식을 제시했다. |
| 보존, time reversal과 gauge | Christen–Büttiker [3] 식 (1)–(4)과 Papior et al. [1] 식 (25)–(27)을 대조했다. 행·열 합의 물리적 역할, 자기장 역전의 조건, gauge covariance와 실제 유한 바이어스 전위 재배열을 분리했다. |
| voltage·dephasing·thermoelectric probe | Förster et al. [5] §II, Sánchez–Serra [4] isothermal·adiabatic case, Shastry–Stafford [6] §II를 대조했다. \(J_p^N=0\), energy-resolved \(J_p^N(E)=0\), \(J_p^N=J_p^Q=0\)의 조건을 구분했다. |

## 독립 검토와 수정

작성자와 분리된 AI 검토자 landauer_verify가 최종 파일을 원문과 대조했다. 검토 과정에서 선형 전류식의 누락된 덧셈 부호, 평형 전류 상쇄에 필요한 unitary 조건, spin-mixing과 time reversal의 적용 범위, 행·열 합의 역할, gauge invariance와 self-consistent 전위의 관계, probe 인용, 열 전류의 선형 응답 누락을 지적했다. 작성자는 이를 반영했으며, 검토자는 수정본에서 미해결 중대 오류를 발견하지 못했다고 판단했다.

그림과 수치 예제는 이 문서에 없다. 이후 추가할 경우에는 입력·단위·계산 과정, 원본 그림의 권리·설명·대체 텍스트를 이 기록과 같은 기준으로 검토한다.

## 참고 원문

1. N. Papior et al., *Computer Physics Communications* **212**, 8–24 (2017), https://arxiv.org/pdf/1607.04464.
2. J. Meair, P. Jacquod, *Journal of Physics: Condensed Matter* **25**, 082201 (2013), https://arxiv.org/pdf/1211.5583.
3. T. Christen, M. Büttiker, *Europhysics Letters* **35**, 523–528 (1996), https://arxiv.org/pdf/cond-mat/9604029.
4. D. Sánchez, L. Serra, *Physical Review B* **84**, 201307(R) (2011), https://arxiv.org/pdf/1107.3576.
5. H. Förster et al., *Physical Review B* **75**, 035340 (2007), https://arxiv.org/pdf/cond-mat/0609544.
6. A. Shastry, C. A. Stafford, *Physical Review B* **94**, 155433 (2016), https://arxiv.org/pdf/1603.00096.
