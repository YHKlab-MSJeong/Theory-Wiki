# 그림 없는 문서 보완: 변경 범위 검토

- 일자: 2026-11-08. 대상은 아래 7개 문서의 도식, 캡션 및 추가된 ONETEP 원문 그림이다. 기존 본문 전체를 새로 검토했다는 뜻은 아니다.
- 독립 검토: `inventory`는 네 도식과 Lee 원그림, ONETEP 원그림을 대조했고 `paper_figs`는 나머지 유전 응답 도식 세 개를 대조했다. 본 작업자가 원문 및 시각 자료를 통합 확인했다.
- 4개 수송·국소성 그림 검토에서 SK를 학습 표적처럼 표시한 표현과 층간 단방향 연결을 수정했다. Order-N 도식에는 고정 절단·연결 수 및 다른 비용 조건을 명시했다. Lee Fig. 5에는 안정·준안정 색상과 HfO₂ 비교점을 추가했다.
- SevenNet의 BEC 전용 모델과 다중과제 출력을 구분했다. 유전율에는 별도의 포논 및 전자 응답이 필요하다. 수치는 자체 도식에서 재현하지 않았다.
- 연구 원문 대조: Gonze–Lee 1997 §§V, VIII 및 Baroni et al. 2001 §§II.3.2, II.4.2; SevenNet-Polar v3 Abstract and §§2.1–2.3; Yim 2015 Methods; Lee 2018 Fig. 5 and Methods; TBtrans 5.4 Principal layer interactions; Wimmer and Richter 2009 §1; Zou 2025 §§II–III (기존 근거 승계, 해당 웹페이지 직접 접근은 차단); Soler 2002 §§VI, XIII; Kohn 1996; Benzi et al. 2013 §§4, 8.
- ONETEP Fig. 7: Prentice et al. 2020 §IV.B.1.b, PDF file p. 10, printed p. 174111-9. Four polymer chains, hybrid XC, Iridis5 32 nodes; fit excludes two smallest systems. The article applies CC BY 4.0 except where otherwise credited; Fig. 7 has no separate credit. 300 dpi PDF crop preserves axes, data and legend. Original PDF https://mostwiedzy.pl/pl/publication/download/1/the-onetep-linear-scaling-density-functional-theory-program_47452.pdf SHA-256 6463d9363979d40b222b933a065cb9c763f07170d021d8333ef8aa98fa87ff09; PNG SHA-256 824baf69a7658e10b23544401fcfd1e712d4834f78356fa75a1cc6a813985f42.
- Capture: `pdftoppm -f 10 -l 10 -r 300 -x 180 -y 1790 -W 1020 -H 720 -png -singlefile INPUT.pdf OUTPUT`. Lee Fig. 5 provenance and capture are in `paper-figure-reuse-2026-11-08.md`.
- ONETEP Fig. 3은 원 학위논문의 라이선스 표기가 충돌해 사용하지 않았다. DeePTB Fig. 1/2는 CC BY-NC-ND 4.0에서 crop 허가를 확인하지 못해 원문 링크와 자체 도식만 사용했다.
- Humanizer: 새 캡션과 설명만 부분 검토했으며 과학적 검증과 분리했다.

## 이전 문서 해시와 해당 변경
- `computational-materials-science/dielectric-response/born-effective-charge.md` baseline `1e79b2587c3b860138c08af83afc258667eb9621b1f82722b71026c9310a097c`; assets: born-effective-charge-response.svg; BEC는 절연체의 미소 원자 변위와 분극 선형 응답으로 정의한다.
- `computational-materials-science/dielectric-response/dfpt-dielectric-response.md` baseline `7d49f075feabd5eecdbbe523d1a793f83f5f555f4cc26c46150f6b33d775d4ca`; assets: dfpt-dielectric-workflow.svg; 조화 절연체의 정적 유전 응답은 전자 및 Born 전하와 포논에 의한 이온 응답을 포함한다.
- `computational-materials-science/dielectric-response/high-k-screening.md` baseline `241ece2089e0d3693a7f0c1c6469e61845ab79241ee700ff96e49493a7af63de`; assets: high-k-selection.svg, lee-2018-fig5.png; 유전체 선별에서 밴드갭과 유전율 외에 계면과 안정성을 검토한다.
- `computational-materials-science/dielectric-response/ml-born-effective-charge.md` baseline `0b75c5bc6e825d7853f961787401965846d751606a43c532e59c833fffdf0337`; assets: sevennet-polar-outputs.svg; BEC만으로 전체 유전율이 정해지지 않으며 포논과 전자 응답이 추가로 필요하다.
- `computational-materials-science/quantum-transport/hamiltonian-block-stitching.md` baseline `d50ca8e43e1ace7dc040a7f1265a2207148735bdd2f549033eafa77d3cb7ef5f`; assets: block-stitching.svg; 비직교 층 블록 모형은 H, S 및 층간 결합을 사용한다.
- `computational-materials-science/quantum-transport/ml-hamiltonian-transport.md` baseline `4efc76ac3ace20d2204c2094df938cae54516a9689bd9106c58cc1f4ba2af102`; assets: ml-hamiltonian-overview.svg; 학습된 국소 환경 모형으로 큰 구조의 Hamiltonian을 구성해 수송을 계산할 수 있다.
- `computational-science/atomistic-simulation/order-n-dft.md` baseline `5279b2506bee0c4563b0a7d7b3e58ea95f29042c898ae551eda5a0553a9aadf6`; assets: order-n-locality.svg, onetep-2020-fig7.png; 밀도행렬의 국소성 및 절단은 선형 스케일링 전자구조 방법의 기반이다.
