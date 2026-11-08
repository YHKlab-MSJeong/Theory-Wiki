# 품질 근거: hamiltonian-block-stitching.md

- 대상 문서: `docs/computational-materials-science/quantum-transport/hamiltonian-block-stitching.md`
- 문서 SHA-256: 07c2977fc040edea4410c329dbf823e76b6cbcdad357eec3265787c86cd28daf
- 판정 범위: 신규 문서 전체
- 목적: 비직교 기저의 행렬 구성, principal layer 조립, 열린 경계 NEGF/RGF와 블록 반복 근사를 설명한다.
- 독자와 제외 범위: 국소 궤도·DFT·NEGF 기초가 있는 독자. 특정 코드의 파일 변환 스크립트는 제외한다.

## 주장과 근거

1. **주장:** 비직교 국소 궤도 기저에서는 일반화 고유값 문제의 \(H\)와 \(S\), 층간 결합 overlap을 함께 보존해야 한다.
   - **범위:** SIESTA/TBtrans 계열의 국소 원자궤도 행렬 표현
   - **판정:** `supported`
   - **출처:** Soler et al. (2002, §§III–VI), SIESTA 5.4 reference (“Calculation of electronic structure,” “NEGF equations”)
2. **주장:** 열린 경계 수송은 전극 self-energy로 반무한 전극을 나타내며, principal layer 결합 범위 조건을 확인해야 한다.
   - **범위:** 두 전극과 유한 scattering region을 잇는 coherent NEGF 예시
   - **판정:** `supported`
   - **출처:** SIESTA TBtrans guide (“TBT.Elec.<>.HS,” “Principal layer interactions”), Papior et al. (2017, NEGF/transport formalism)
3. **주장:** central scattering region의 RGF 재귀 비용은 고정된 층 행렬 차원에서 층 수에 선형으로 증가하며 단면·층 크기를 함께 늘리는 경우의 선형성을 뜻하지 않는다.
   - **범위:** 한 에너지·횡방향 \(k\)-점의 central-region 재귀 계산. 전극 surface Green 함수, 에너지 적분, 자기일관 반복 비용은 포함하지 않음.
   - **판정:** `supported`
   - **출처:** Wimmer and Richter (2009, §1, Eqs. (9)–(12), pp. 4–5); Papior et al. (2017, §III.C.1, Eqs. (17)–(18))
4. **주장:** 반복 Hamiltonian 블록은 게이트로 바뀌는 전위·전하나 결함에 따른 전자구조 변화를 새로 생성하지 않는다.
   - **범위:** 고정 행렬 블록을 반복해 만든 장치 모델
   - **판정:** `supported`
   - **출처:** SIESTA 5.4 reference (“TranSIESTA,” “NEGF equations”), Zou et al. (2025, §§III.2–III.3)
5. **주장:** Order-N DFT는 큰 구조에 대한 전자구조 계산을 선형 스케일링으로 수행하려는 방법이며, 작은 셀의 고정 행렬 블록을 길이 방향으로 복제하는 것과 계산 절차가 다르다.
   - **범위:** Order-N 방법과 고정 (H/S) 블록 확장의 개념 구분
   - **판정:** `supported`
   - **출처:** Soler et al. (2002, §XIV “Order-\(N\) functional”); SIESTA 5.4 reference (“Calculation of electronic structure”)

## 가정과 한계

- 실제 모델에는 \(H\), \(S\), 원자·기저 순서, 에너지 영점, spin, 전극 정렬과 층간 결합 범위가 일치해야 한다.
- 수식의 transmission은 탄성 단일입자 NEGF 맥락이며, 산란 self-energy는 별도 확장이다.
- 고정 cross-section에서 길이 선형은 수치 알고리즘의 비용 스케일링이다. 행렬 블록이 물리적으로 확장 구조를 대표한다는 검증을 대신하지 않는다.
- 본문은 역방향 층간 블록의 켤레전치와 retarded Green kernel \(zS-H\)를 명시했다. 고정 \(H\) 계산의 접촉 self-energy 효과와 접촉 유도 전위·전하의 자기일관 되먹임을 구분했다.

## 독립 검토

- 상태: pass.
- 독립 검토자: `hamiltonian_scope`.
- 검토 내용: 일반화 고유값 수식, (H/S) 결합, principal-layer 조건, RGF 비용과 그 적용 조건.
