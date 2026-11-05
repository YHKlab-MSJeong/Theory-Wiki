# defect-scattering 그림 추가 검증 기록

대상 문서: docs/device-physics/mobility/defect-scattering.md
대상 SHA-256: 0d58789a120899d4d0fd84effa7a1bd5a50d1e70460fde6823bf7efedbbf6293
기준 문서 SHA-256: 0ffb3f41377d4e10a492dcc45e5ab8211859e63c66dda8fcbd0b17873134d826
이전 검증 기록: refs/quality/evidence/defect-scattering-2026-10-30.md
이전 검증 기록 SHA-256: c0e0c876b39a78f7fc9f6e1d05c07a206818bd6524fefc8ec3115bb5fe662f96

## 범위와 주장

본문의 정의·수식·조건은 수정하지 않았다. 새 그림은 기존에 독립 검증된 문서 주장을 원본 도식으로 재구성했다. 그림에 별도 수치 사례나 새로운 계산 결과는 넣지 않았다.

| 그림에서 확인할 주장 | 직접 대조한 근거 | 판정 |
|---|---|---|
| single-defect matrix element Mₖ′ₖ=⟨k′|Vⱼ|k⟩ is normalized before the disorder average of |M|²; independent-defect Born rate then uses defect density and a final-state sum, while one periodic supercell is not random-ensemble mobility | Hwang–Das Sarma (1)–(3); Kaasbjerg–Low–Jauho §II.A–B, (10)–(13) | supported |

## 그림 재현 및 검토

- HTML source: refs/quality/figure-source/defect-scattering-model.html
- HTML source SHA-256: 864173175b9fc4af2eb4271c048fc4ab569f77275b319538d4649785310b9027
- SVG: docs/assets/defect-scattering-model.svg
- SVG SHA-256: 763eaa76a25de0c6b5751262ee60e86feb6ddaa8d81542d83ed4ba2b23df84d5
- diagram-design 접근성 self-check와 SVG export를 통과했다. 원문에서 검토된 가정·부호·정규화만 나타내도록 확인했다.
- 대체 텍스트는 humanizer 점검 뒤 수식, 한계, 전문용어를 보존했다.
- 독립 검토 첫 회차에서 unsquared matrix element와 transport rate 사이의 disorder average·defect density 연결이 그림에서 빠졌다고 지적했다. 두 번째 검토에서 M 정의 누락과 final-state sum 중복을 지적했다. 도식에 Mₖ′ₖ=⟨k′|Vⱼ|k⟩, 단일 결함 normalization, disorder 평균 |M|², 그리고 rate 상자의 defect density와 final-state sum을 분리했다. re-review에서 제안된 “density factor follows normalization” 표현도 반영했다. 최종 확인에서 matrix-element, average, density factor와 final-state sum의 구분 및 SVG 잘림 부재가 확인되어 통과했다.

## 이전 근거

refs/quality/evidence/defect-scattering-2026-10-30.md는 그림 전 문서 내용의 검증 기록으로 유지한다. 이 기록은 새 도식의 의미와 재현 파일만 추가로 확인한다.
