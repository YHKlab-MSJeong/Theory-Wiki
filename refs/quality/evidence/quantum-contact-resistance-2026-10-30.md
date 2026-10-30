# Quantum contact resistance 검증 기록

대상: `docs/computational-materials-science/quantum-transport/quantum-contact-resistance.md`  
대상 SHA-256: `40b925378cb79b2689b5fb2c338b1b7dc92ea230c8ac559d472898db53cda290`

범위는 zero-temperature, linear-response, coherent two-terminal conductance quantum과 four-terminal 정의의 구별이다.

| 주장 | 대조 근거 | 판정 |
| --- | --- | --- |
| spin-resolved \(e^2/h\)와 spin-degenerate mode의 \(2e^2/h\) | Beenakker §I.C.2 식 (1.33); Feilhauer–Moško §I 식 (11), (15) | supported |
| two-와 four-terminal resistance 및 probe 정의를 구별해야 함 | Texier–Montambaux §2; Landauer abstract | supported |

독립 검토자 `wiki_tooling`가 온도·bias 조건과 reference title을 교정했다. 유한 bias가 비탄성 산란을 자동 포함한다고 읽히는 표현은 삭제했다. humanizer 점검은 기호·조건을 보존했다. 그림·수치 예제는 없다.

1. C. W. J. Beenakker, *Random-matrix theory of quantum transport* (1997), §I.C.2, https://arxiv.org/pdf/cond-mat/9612179.
2. J. Feilhauer, M. Moško, *Quantum and Boltzmann transport in the quasi-one-dimensional wire with rough edges* (2010), §I, https://arxiv.org/pdf/1011.6193.
3. C. Texier, G. Montambaux, *Four-terminal resistances in mesoscopic networks of metallic wires: Weak localisation and correlations*, §2, https://gilles.montambaux.com/files/publications/reprints/189_four_terminal_resistances.pdf.
4. R. Landauer, *Conductance determined by transmission: probes and quantised constriction resistance*, abstract, https://doi.org/10.1088/0953-8984/1/43/011.
