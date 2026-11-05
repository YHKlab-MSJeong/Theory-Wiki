# quantum-contact-resistance 그림 추가 검증 기록

대상 문서: docs/computational-materials-science/quantum-transport/quantum-contact-resistance.md
대상 SHA-256: 729c90c905e0c9d58daa3ed08c1a8f8a848a25e017325436b70f75e23c4e2fee
기준 문서 SHA-256: 40b925378cb79b2689b5fb2c338b1b7dc92ea230c8ac559d472898db53cda290
이전 검증 기록: refs/quality/evidence/quantum-contact-resistance-2026-10-30.md
이전 검증 기록 SHA-256: 3ccb4d119ca235cf3f16eea3babd756710e9554cf08212dba40afab537d4ab99

## 범위와 주장

본문의 정의·수식·조건은 수정하지 않았다. 새 그림은 기존에 독립 검증된 문서 주장을 원본 도식으로 재구성했다. 그림에 별도 수치 사례나 새로운 계산 결과는 넣지 않았다.

| 그림에서 확인할 주장 | 직접 대조한 근거 | 판정 |
|---|---|---|
| For N fully transmitting spin-degenerate modes, the ideal two-terminal conductance and resistance are G=(2e²/h)N and R₂t=h/(2e²N). | Beenakker §I.C.2, (1.33); Feilhauer–Moško §I, (11), (15) | supported |
| Equal halves of R₂t are a symmetry-based bookkeeping inference for the symmetric ideal model, not a universal resistance assigned to each physical contact. | Symmetric split is an explicitly bounded inference from the total two-terminal value; Mortensen et al. §I and Beenakker §I.C support the nonuniversal contact assignment. | supported, inference stated |

## 그림 재현 및 검토

- HTML source: refs/quality/figure-source/quantum-contact-resistance.html
- HTML source SHA-256: e8df172f0f0b7e7ab1712d8db6f2e5ed15782077f6280164633372e834469a93
- SVG: docs/assets/quantum-contact-resistance.svg
- SVG SHA-256: d2813113e291e55dbe6d3390c30c0ca149bbd3246ce9d3b3b6e9ac0ad2d92773
- diagram-design 접근성 self-check와 SVG export를 통과했다. 원문에서 검토된 가정·부호·정규화만 나타내도록 확인했다.
- 대체 텍스트는 humanizer 점검 뒤 수식, 한계, 전문용어를 보존했다.
- 독립 최종 검토자: wiki_transport_diagram_review (그림의 의미·문서 주장·원문 위치, 2026-11-05). 검토자는 대칭 contact 반분배를 직접 인용된 보편 사실과 구분해 명시하라고 권고했고, 이를 symmetry-based bookkeeping inference로 기록했다.

## 이전 근거

refs/quality/evidence/quantum-contact-resistance-2026-10-30.md는 그림 전 문서 내용의 검증 기록으로 유지한다. 이 기록은 새 도식의 의미와 재현 파일만 추가로 확인한다.
