# 신규 과학 문서 4종 원문 대조 기록 — 2026-11-10 (진행 중)

> 상태: **NOT REVIEWED / NOT APPROVED**. 이 파일은 근거 수집과 수정 내역을 남기는 작업 기록이다. 독립 과학 검토자 검토, 모든 주장별 독립 근거, 최종 문서 SHA 등록, 저장소 전체 테스트는 미완료다. `registry.json`의 `pass`로 이용하지 않는다.

## 검토 범위
- `docs/computational-science/machine-learning/e3nn.md`
- `docs/computational-science/machine-learning/lem-slem.md`
- `docs/computational-science/machine-learning/machine-learning-glossary.md`
- `docs/computational-science/atomistic-simulation/divide-and-conquer-h-plus-lambda-s.md`

## 직접 확인한 원문 구절 (짧은 원문 발췌)

1. e3nn 공식 소개, https://docs.e3nn.org/en/latest/ , What is e3nn?:
   - "equivariant neural networks for the group O(3)"
   - 적용 판단: `e3nn.o3`와 전체 E(3) 모델의 변환 성질을 분리해야 함.
2. e3nn Tensor Product API, https://docs.e3nn.org/en/stable/api/o3/o3_tp.html , 첫 문단:
   - "The tensor product is bilinear"
   - 적용 판단: 기약표현 결합 연산 설명. 원자료와 같은 구현 저장소의 문서이므로 독립 2차 증거로 중복 계산하지 않음.
3. DeePTB E3 공식 입력, https://github.com/deepmodeling/DeePTB/blob/main/docs/advanced/e3tb/advanced_input.md , Model options:
   - "Strictly Localized Equivariant Message-passing or `slem`"
   - "Localized Equivariant Message-passing or `lem`"
   - 적용 판단: 두 방식의 국소성 차이를 명시. 별도 ICLR 2025 SLEM 원논문 초록 https://proceedings.iclr.cc/paper_files/paper/2025/hash/7db2ffcbfd0bd361d47b7fa612bd2ba2-Abstract-Conference.html 과 대조.
4. DeePTB-NEGF 논문, https://doi.org/10.1038/s41524-025-01853-6 , Eq. (3)와 인접 문단:
   - "H′ = H + λ · S"
   - "λ is determined during training"
   - 적용 판단: 비직교 기저의 상수 에너지 offset. 위치 의존 퍼텐셜 갱신과 구별.
5. Wang (2014), https://doi.org/10.1093/nsr/nwu060 , LS3DF 설명과 Eq. (5) 인접 문단:
   - "positive and negative fragments"
   - 적용 판단: LS3DF는 통상적인 partition-of-unity 조합과 다른 부호 fragment 합; 본문에 보완.
6. Peherstorfer et al. (2018), https://doi.org/10.1137/16M1082469 , Abstract:
   - "varying evaluation costs and varying fidelities"
   - 적용 판단: high-/low-fidelity는 특정 정확도 목표·계산비용 비교의 맥락에 따름.
7. Yang & Lee (1995), https://doi.org/10.1063/1.470549 , Abstract:
   - "based on partition of density matrix"
   - 적용 판단: 분할 밀도행렬 D&C는 Hamiltonian block stitching과 구별해야 함.

## 실제 수정·교정
- 2026-11-10: 머신러닝 용어 문서의 multifidelity 설명에 Peherstorfer et al. 2018 및 2026 survey 참고문헌 추가.
- 2026-11-10: LEM/SLEM 논문 참고문헌의 저자 표기 구체화.
- 2026-11-10: LS3DF의 음·양 부호 fragment 조합을 독립된 수식으로 추가하여 단순 가중합과 구별.
- 2026-11-10: 네 문서의 MkDocs nav, topic index, computational science overview 경로를 추가 및 연결.

## 미완료 / 배포 차단
- 원문 전체의 정의, 가정, 수식, 인용 위치와 각 비자명 주장별 **독립 두 출처** 대조.
- 작성자와 구별되는 **독립 과학 검토자**의 실제 reviewer identity, 검토 범위, 최종 판정.
- 검증된 문서 SHA 및 검증 기록 SHA를 `refs/quality/registry.json`에 등록.
- `python -m unittest discover -s tests`, `python scripts/check_quality.py`, `mkdocs build --strict` 실제 실행.
- main 병합, 배포 워크플로 성공 확인.

**이 기록은 독립 검토가 아니며 배포 승인 기록으로 사용할 수 없다.**
