# 논문 원그림 수록·재사용 점검

- 점검일: 2026-11-08
- 범위: 현재 위키에 포함된 논문 원그림, 이번에 추가한 세 도판, 권리 또는 파일 확보 문제로 링크만 유지한 후보.
- 독립 재사용 검토: `paper_figure_rights_audit`; 본 작업자가 최종 이미지 crop과 본문 위치를 시각 확인했다.
- 추가 도판 재검토: `paper_figure_audit`, 2026-11-08; 세 crop·캡션·본문 연결·재사용 조건 확인.
- 검증 기록은 사이트 문서와 메뉴에 넣지 않는다.

## 새로 수록한 도판

| 문서 | 원문 그림 | 라이선스와 출처 | 캡처 방식 | PNG SHA-256 |
|---|---|---|---|---|
| `docs/computational-materials-science/dielectric-response/lee-2018-nonoxide-dielectrics.md` | Lee et al. (2018), Fig. 4, PDF p. 4 | CC BY 4.0; [Nature 원문](https://www.nature.com/articles/s41598-018-33095-6.pdf), PDF SHA-256: `6a2d1be3a3b042ff5a831a94193345801cc32703f845629e4fa977d27b000309`. | [`capture-dielectric-paper-figures.sh`](../figure-source/capture-dielectric-paper-figures.sh)의 300 dpi 렌더와 `1620x600+620+1460` crop. 축·범례·데이터를 보존했다. | `c7c32ec272121e0c611f55819625ff699a9a018f27d97efd692898eaa1d622f8` |
| `docs/computational-materials-science/dielectric-response/yim-2015-high-k-oxides.md` | Yim et al. (2015), Fig. 4, PDF p. 3 | CC BY 4.0; [Nature 원문](https://www.nature.com/articles/am201557.pdf), PDF SHA-256: `41e976d563c98ab5167783d28fe04500e0a7cac88332a9a0d0a754014595b138`. | [`capture-dielectric-paper-figures.sh`](../figure-source/capture-dielectric-paper-figures.sh)의 300 dpi 렌더와 `1140x700+1270+275` crop. 축·범례·데이터를 보존했다. | `eb0ac490834ccc98186c9a5b70518d1a7b8e5509bc19d014b0fc3a3ce69d0005` |
| `docs/computational-materials-science/dielectric-response/takigawa-2026-prx-ionic-dielectric-ml.md` | Takigawa et al. (2026), Fig. 2, PDF p. 3 | [APS 원문 PDF](https://journals.aps.org/prx/pdf/10.1103/28wr-w896), PDF SHA-256: `d4e85051b506c119bb4c8f9d636d6595aa9f5696f9b6e1addde33e1075973534`. APS는 논문에 CC BY 4.0을 적용하며 일부 도판은 제3자 예외일 수 있다고 안내한다. Fig. 2 캡션의 별도 권리자 표기는 확인되지 않았다. | 300 dpi PDF 페이지 렌더에서 논문 캡션과 여백을 덜어 내고 도판 영역을 crop했다. 그림 데이터·요소는 수정하지 않았다. | `b28f57f42d5fe03015e583aebfd11995576ddfeb9ab75d9a4ba47439c79472a5` |
| `docs/computational-materials-science/dielectric-response/lee-2018-nonoxide-dielectrics.md` | Lee et al. (2018), Fig. 5, PDF p. 5 | CC BY 4.0; 공식 Nature PDF, 제3자 권리 표기 없음. PDF: <https://www.nature.com/articles/s41598-018-33095-6.pdf>. 원본 PDF SHA-256: `6a2d1be3a3b042ff5a831a94193345801cc32703f845629e4fa977d27b000309`. | 300 dpi 렌더 후 그림 영역만 crop. 밴드갭·유전율 축, 후보 표시, 색상 범례를 보존하고 논문 캡션·페이지 여백을 제거했다. PNG 크기 950×620 px. | `3ff44e655eae1a9966820c34e21b8db8f37493cd76ba23104d50b53c248dbfd1` |
| `docs/computational-science/atomistic-simulation/siesta-54-omm.md` | Lebedeva et al. (2023), Fig. 2, PDF p. 6 | CC BY 4.0; DOI `10.1098/rsos.230063`; Figure 2 별도 권리자 표기 없음. PDF 사본: <https://www.nanogune.eu/en/publications/download/4935>. 원본 PDF SHA-256: `1942586b7ed224cc096cbe77b49ea986beda696e79e06ed29eb1e3639fce62d0`. | 300 dpi 렌더 후 도판과 바깥 여백만 crop. 흐름도 요소를 수정하지 않았다. PNG 크기 1460×1050 px. 문서에서 2023 modular libOMM 구현과 SIESTA 5.4 native OMM을 구분했다. | `b5a12b4e2a79c7ffbb101e4b639e3e29c4f35cfac5783bb1c7b6445d65ae872c` |
| `docs/computational-materials-science/quantum-transport/basis-set-validation-cases.md` | Afzalian et al. (2021), Fig. 1, arXiv v1 PDF p. 2 | arXiv에 CC BY 4.0 표시; [arXiv record](https://arxiv.org/abs/2106.07248), [v1 PDF](https://arxiv.org/pdf/2106.07248). 그림 캡션에 제3자 권리자 표기 없음. 원본 PDF SHA-256: `8608ff6d687e390d3a66e0b8fffd1a46f8f5b88cdc297731df04c3244f69277f`. | 300 dpi 렌더 후 네 패널과 패널 제목을 보존하고 논문 캡션·페이지 여백을 crop했다. PNG 크기 2040×1000 px. 본문은 이 결과를 Hamiltonian 표현 비교로 설명하고 SZP/DZP 수렴 검증과 구별한다. | `6b397b51838334b39a1d74c4badb55d828332b8b1d8c9b574eba81f65971100d` |
| `docs/computational-materials-science/quantum-transport/mode-space-transport.md` | Carrillo-Nuñez et al. (2020), Fig. 2, PDF p. 5 | Glasgow 공식 저장소 레코드와 PDF에 CC BY 4.0 표시; [repository record](https://eprints.gla.ac.uk/221595/), [PDF](https://eprints.gla.ac.uk/221595/13/221595.pdf). figure별 별도 권리자 표기 없음. 원본 PDF SHA-256: `723c77336f6ec9f8ec21144f7794d4324146b929f788cc66d921669a0d3e068f`. | 300 dpi 렌더 후 full-band 비교 그림을 crop했다. 축, 범례, 곡선을 보존했다. 본문은 3 nm \(\langle111\rangle\) Si nanowire와 논문이 표시한 에너지 창의 밴드 비교로 범위를 제한한다. PNG SHA-256은 `50319c7751a8aea3eb6e8d656a788cdb0c169f8847e59984929e01ac9b35b305`. | `50319c7751a8aea3eb6e8d656a788cdb0c169f8847e59984929e01ac9b35b` |
| `docs/computational-science/atomistic-simulation/electronic-structure-solvers.md` | Hourahine et al. (2020), Fig. 5(c,d), PDF p. 14 | Warwick 공식 저장소와 논문 PDF에 CC BY 4.0 표시; [repository record](https://wrap.warwick.ac.uk/id/eprint/137347/), [PDF](https://wrap.warwick.ac.uk/id/eprint/137347/1/WRAP-DFTB-software-package-efficient-density-atomistic-simulations-Hourahine-2020.pdf). figure별 별도 권리자 표기 없음. 원본 PDF SHA-256: `70b13aa7578c952f0d76f3aa825dcef841c804abb59188f901032b99f2fdcbb2`. | 300 dpi 렌더 후 패널 (c,d)의 축·눈금·계열·범례를 보존하고 (a,b), 원 캡션 및 페이지 여백을 잘라냈다. 본문은 비자기일관 전하, spin-non-polarized, \(\Gamma\)-점 계산 조건을 명시한다. PNG SHA-256: `c3b499a0a9615e85decac3a8b1d4721027bc4cc84483475f14eccea7a7d62ab3`. | `c3b499a0a9615e85decac3a8b1d4721027bc4cc84483475f14eccea7a7d62ab3` |
| `docs/computational-materials-science/quantum-transport/basis-set-validation-cases.md` | Afzalian et al. (2021), Fig. 2, arXiv v1 PDF p. 3 | arXiv에 CC BY 4.0 표시; [arXiv record](https://arxiv.org/abs/2106.07248), [v1 PDF](https://arxiv.org/pdf/2106.07248v1). figure별 별도 권리자 표기 없음. 원본 PDF SHA-256: `8608ff6d687e390d3a66e0b8fffd1a46f8f5b88cdc297731df04c3244f69277f`. | 300 dpi 렌더 후 구조와 밴드 비교의 두 패널, 축, 범례와 주석을 보존하고 페이지 여백·논문 캡션을 잘라냈다. 구조와 밴드 곡선은 수정하지 않았다. 본문은 plane-wave/Wannier 표현 비교를 SZP/DZP 수렴과 구분한다. PNG SHA-256: `578dac7c2ef68fae399deef8f05c3a67750a7421aa5b270ba261fff094046975`. | `578dac7c2ef68fae399deef8f05c3a67750a7421aa5b270ba261fff094046975` |

캡처 명령과 crop 좌표는 [`capture-additional-paper-figures.sh`](../figure-source/capture-additional-paper-figures.sh)에 기록했다. 원본 PDF는 재배포용 위키 저장소에 넣지 않았다. 출처·원문 그림 번호·라이선스·crop 사실은 각 그림 캡션에 표시했다.

표는 로컬에 저장한 논문 원그림 9개 전체를 나열한다. 원본 PDF 해시와 crop 정보는 확인 가능한 작업 자료에서 기록했으며, 과거에 수록된 도판의 crop 좌표처럼 남아 있지 않은 정보는 임의로 만들어 채우지 않았다.

## 원문 링크만 유지한 도판

- Takigawa et al. (2026) 논문은 CC BY 4.0이지만 APS는 일부 그림에 제3자 저작권 예외가 있을 수 있다고 안내한다. Fig. 4 캡션에는 별도 권리자 표기가 없다. 출판사 도판 요청은 HTTP 403 challenge를 반환해 원본 파일을 확보하지 못했으므로, high-κ screening 문서에서 [공식 도판 링크](https://journals.aps.org/prx/article/10.1103/28wr-w896/deliverable/ded1aa42-0182-40ff-9cde-d6c2f81a6e41)만 유지한다.
- HamGNN-NEGF Fig. 1은 CC BY-NC-ND 4.0 조건으로 표시되어 있어 crop/수정본을 로컬 수록하지 않고 원문 PDF를 연결한다: <https://arxiv.org/abs/2609.37058>.
- Quhe et al. (2019) Supporting Information Fig. S1은 재사용 허가를 확인하지 못해 원문 PDF 링크만 둔다: <https://www.rsc.org/suppdata/c8/tc/c8tc05863f/c8tc05863f1.pdf>.
- Ducry et al. (2019) SISPAD Fig. 2–4는 접근 가능한 PDF에서 설명을 확인했지만 재사용 라이선스를 확인하지 못해 원문 링크만 둔다: <https://in4.iue.tuwien.ac.at/pdfs/sispad2019/SISPAD_4.1.pdf>.

## 독립 점검과 한계

- 원문 figure 번호, 논문 페이지, 캡션 설명과 각 도판이 연결된 위키 문단을 대조했다.
- 9개 PNG 각각에서 원본 페이지의 도표·곡선·라벨이 보존됐는지 확인했다. 변수를 다시 그리거나 색상·데이터를 수정하지 않았다.
- 라이선스 검토는 확인된 출처와 figure credit line에 한정한다. 이 기록은 법률 자문이나 출판사 파일 재배포 승인을 대신하지 않는다.
