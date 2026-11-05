# landauer-buttiker 그림 추가 검증 기록

대상 문서: docs/computational-materials-science/quantum-transport/landauer-buttiker.md
대상 SHA-256: bcee4c43ba5977745ad7371b98c88fd7e5ccd2ecf1ed358ad0daa7ace1985091
기준 문서 SHA-256: 968c206595e71fec96a186d0a0c96924c6a9f5e3a766ec39d798e1e385216f42
이전 검증 기록: refs/quality/evidence/landauer-buttiker-2026-10-29.md
이전 검증 기록 SHA-256: 623d0a0a5a2dc7b2d6d032a5073f16beb0058c9d8eebde9084c923cb955f90e3

## 범위와 주장

본문의 정의·수식·조건은 수정하지 않았다. 새 그림은 기존에 독립 검증된 문서 주장을 원본 도식으로 재구성했다. 그림에 별도 수치 사례나 새로운 계산 결과는 넣지 않았다.

| 그림에서 확인할 주장 | 직접 대조한 근거 | 판정 |
|---|---|---|
| multi-terminal current is a signed sum over directed transmissions and reservoir occupations; voltage, voltage–temperature, and dephasing probes impose different zero-current conditions | Papior et al. §IV.A, (24)–(31); Förster et al. §II; Sánchez–Serra (2)–(10); Shastry–Stafford §II | supported |

## 그림 재현 및 검토

- HTML source: refs/quality/figure-source/landauer-buttiker-probes.html
- HTML source SHA-256: 52b839e877b6040b9f65751b932903b3fa6324628c12ed84bafc1bed6261bb36
- SVG: docs/assets/landauer-buttiker-probes.svg
- SVG SHA-256: d63cb66382aaf1221faf9c78cc14efaf06caa14a18999aafd34682ddd15528cb
- diagram-design 접근성 self-check와 SVG export를 통과했다. 원문에서 검토된 가정·부호·정규화만 나타내도록 확인했다.
- 대체 텍스트는 humanizer 점검 뒤 수식, 한계, 전문용어를 보존했다.
- 독립 최종 검토자: wiki_transport_diagram_review (그림의 의미·문서 주장·원문 위치, 2026-11-05).

## 이전 근거

refs/quality/evidence/landauer-buttiker-2026-10-29.md는 그림 전 문서 내용의 검증 기록으로 유지한다. 이 기록은 새 도식의 의미와 재현 파일만 추가로 확인한다.
