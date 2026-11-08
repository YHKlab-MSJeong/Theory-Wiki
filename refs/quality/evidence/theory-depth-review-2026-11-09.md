# 이론 위키 전체 보강: 변경 범위 검토

- 일자: 2026-11-09. 아래 baseline 이후 변경된 이론 문서 26개를 검토했다. 과거 본문 전체를 새로 검증했다고 뜻하지 않는다.
- 이동도 4편 작성 mobility_theory, 독립 검토 atomistic_theory. QTBM·NEGF·Landauer·접촉저항·mode-space 6편 작성 transport_theory, 독립 검토 mobility_theory. 전자구조 5편 작성 atomistic_theory, 독립 검토 mobility_theory와 transport_theory. 나머지 RGF·장채널 작성 transport_theory, 독립 검토 atomistic_theory. 통합 담당자가 작성한 유전 응답·전자–포논·SCBA는 transport_theory가 독립 검토했다.
- 유전 텐서 선형 관계는 자발분극 기준을 보존하도록 δP=ε₀χδE로 썼다. EPC 흡수 k+q 및 방출 k−q의 행렬원소·유한 셀 정규화와 Pauli 차단, SCBA의 Keldysh 식 예외 및 에너지 window를 별도 대조했다. self-energy 상수 폭 예에서 ħ/(2×10 meV)=32.91 fs.
- 이동도 예제: 채널 G=0.801 mS, Rch=1248 Ω, 비보정 이동도 약 417 cm²/Vs. 2D 상관함수 Fourier 변환의 qΛ=2 값 exp=3^(−3/2), Gaussian=e^(−1); Matthiessen 두 구간의 0.8과 1.25를 검산했다. Yeh §IV.A, Kong §II, Lin §§I, IV 및 결함 논문 식 위치 수정; 원격 결함의 e^(−qd)는 Jang Eq.(3)을 확인했다.
- QTBM 문서의 오른쪽 outgoing mode를 χ_R⁻로 정정했다(각 lead에서 소자 입사=+로 정의한 문서 규약). transmission 속도비, NEGF의 ΓL,ΓR>0, Landauer 열폭 4 arcosh√2 kBT, probe 전류 조건 및 contact resistance를 검토했다. 비직교 mode-space Schur 소거는 4×4 fixture에서 전체 역행렬 대비 3.5e−16 오차로 확인했다.
- 비직교 RGF 재귀는 복소 Hermitian H, 양의 정부호 S, 4층×3궤도의 독립 fixture에서 전체 역행렬과 최대 4.23e−16 차이로 검산했다. 고정된 단면과 에너지·k점 등 계산 범위를 분리했다.
- SCC-DFTB는 전자 점유 과잉 Δq=q−q0 부호와 Hamiltonian correction, 0.05 eV 예제를 확인했다. 비직교 Tr(PS), 단일 스핀 0 K의 PSP=P, PEXSI pole expansion과 CheSS 재귀, 조건수 19와 선택 역행렬 2/3 예제를 검토했다. 숫자 예는 문서에 명시된 자체 산술이며 실재 물질 계산이 아니다.
- 개념이 등장하는 문맥에 기존 이론 문서와 1차 논문 링크를 추가했다. Humanizer는 변경된 한국어 문단에만 적용했고 수치·조건·출처와 사실 검증을 별도로 유지했다. 신규 그림 추가나 기존 이미지 변경은 없다.

## 직전 검증 문서 SHA-256
- `computational-materials-science/dielectric-response/dielectric-response.md`: `9313f64da4a46fa9c82845f9d46d0aa4c846dfbe60cd052335a83331788c4ecd`
- `computational-materials-science/electron-phonon-coupling/electron-phonon-coupling.md`: `c3c803f7986e267c860babd9a43af148b768412685bfd12a28b74e5ca3795a39`
- `computational-materials-science/electron-phonon-coupling/electron-phonon-self-energy.md`: `31e130953c3b3a5aa68d7e88ba7d250510a0b78bd6388fb20d54d0e09b325c1f`
- `computational-materials-science/quantum-transport/basis-set-validation-cases.md`: `42540248b7fb32cd3679fb5a777a104bd68884dfb9b66a3c813f57f393722868`
- `computational-materials-science/quantum-transport/dfth-negf.md`: `108f3046c3b68f2223fa5bcfed9ce0d3961f09eb27b0c3f37c3a8881e3713292`
- `computational-materials-science/quantum-transport/hamiltonian-block-stitching.md`: `087e6d430d2b482cbd5ca69d0f0fbd5a85c6949b6cc8e7bb810f42d2afe21e85`
- `computational-materials-science/quantum-transport/landauer-buttiker.md`: `a1b2bfc18daed44eb7bf438212d3a7cda75289b5e5b4b385df1f5bdb0a17f470`
- `computational-materials-science/quantum-transport/landauer-transmission.md`: `52c21d662b062aebec4531947a92c2a805243134a16220d7944950ad376b7939`
- `computational-materials-science/quantum-transport/long-channel-transport.md`: `3806c05e657624888d1d9c30277ee507a1f334456208d52f70b78ba609ea0278`
- `computational-materials-science/quantum-transport/ml-hamiltonian-transport.md`: `5f125fb0920da0b01cd3588da67c6684edce15ccf6f2d4263ce01d29d83eabdf`
- `computational-materials-science/quantum-transport/mode-space-transport.md`: `e443166a0ee7b79b3017aee9d5120870cd4292bd7b8b32598f03b73cd4ceaa7c`
- `computational-materials-science/quantum-transport/negf.md`: `9ff3f58690c41ce0cc17973551d0ae7c35936575b52276d874d50eefeddce80c`
- `computational-materials-science/quantum-transport/nonorthogonal-kpm.md`: `76f7914b06cf674bac2f7b68c002ca502da436c7613c54e418f26db13639dd45`
- `computational-materials-science/quantum-transport/overview.md`: `734599feb33072669f4e11978a2bb4515aa26fe04832a62bc11cd6c9ba9229ba`
- `computational-materials-science/quantum-transport/quantum-contact-resistance.md`: `87da14f16e5c72b9fb9eb201896d3f9f2c42d24ca939b03dbeb5a86d81cfbcef`
- `computational-materials-science/quantum-transport/scattering-qtbm.md`: `e431b2cb288b1920fe9b3aaf6795878cfb499b6f72f1c2c75944311e7d58d4c7`
- `computational-materials-science/quantum-transport/scba-convergence.md`: `1f2ce7e805a1a1580be30b5016620e8c0fe8a44c78ee8718cf07657843fa2f90`
- `computational-science/atomistic-simulation/dftb-large-scale.md`: `39e828ead74ee02b23603624f0a7487ffb4ee3c18a5b83c3d41c8540289d884d`
- `computational-science/atomistic-simulation/electronic-structure-solvers.md`: `1414e9ca4b89dc4b1e4ff8d724da07011f9c6bae24d86a9bb8ab61741bcc97b5`
- `computational-science/atomistic-simulation/localized-basis-sets.md`: `40cf679931d2535499a1828baee81f7cf26fe401c196d7b15eae89f1cd3980b6`
- `computational-science/atomistic-simulation/order-n-dft.md`: `215b6f3c6d9c95b9ad576d4bda0c7d6e99483d73bd3b82effd69120757309cc8`
- `computational-science/atomistic-simulation/siesta-54-omm.md`: `e805d88fba11fdac8c4ca110034af45f58fb7f451aeb8486dd030356e0e84961`
- `device-physics/mobility/defect-scattering.md`: `0ebd574342ae85cc3bc225ac13859249bd03a1cce8c7f79abe80691307c9f503`
- `device-physics/mobility/inversion-layer-mobility.md`: `4ccb37a0187bb06bebceaed87adae6bf036f30eb51c5ab56f6164284142c4017`
- `device-physics/mobility/matthiessens-rule.md`: `2dc8373fd60b72c77612db06aa2706649e63c76092819799b06ca7a1a028f444`
- `device-physics/mobility/surface-roughness-scattering.md`: `f57bb3dfbc49334b53e0ee1167089522d2b85ff220b09d9e4f94dc3ffd6cc83a`
