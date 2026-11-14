# 머신러닝 용어 확장과 규칙 재확인

## 범위와 독자

- 과학계산 논문을 읽는 학습자를 위해 기존 17항목 사전을 45행의 용어 찾아보기로 확장했다. 학습/최적화, 평가/전이, 표현/대칭, 증강의 신규 문서 전체가 과학 검토 범위다.
- 기존 fidelity/CNN은 제목·약어·기호 설명·캡션 규약 및 bibliography 순서의 의미보존 변경이다. 사전은 변경 주장과 영향 범위 검토이며 기존의 유효한 출처 근거를 승계한다.
- 사용자 요청의 수식·예제·필요한 그림·관련 이론 및 원 논문 링크를 포함한다. 신규 학습이나 DFT 계산은 수행하지 않았다.

## RGLee 규칙 원문과 적용

- 원본의 pinned c2ac6381caece612ec28eeb4ddddd1b75226cc2f와 확인 당시 main fe8a6bc07dbb7d63afc5b55684b056dc8d31bd52의 AGENTS, format, research-workflow, quality README를 직접 읽었다. 네 파일 내용은 동일했다.
- 감사 기록은 `refs/quality/evidence/ml-rules-audit-2026-11-15.md`에 보존한다. 영문 대표 제목, 첫 약어 정의, core equation 기호, 캡션 달러 수식, 최초 인용 순서·번호를 범위 내 ML 페이지들에 반영했다.
- 원본의 생성 그림 금지 및 experiment 작업 경로에는 사용자가 허용한 검증된 자체 도식·수학 플롯과 /tmp 격리 사본 규칙을 적용한다. 논문 보고의 reported-primary 예외 및 local registry/checker도 local AGENTS의 명시 운영 기준이다.
- 이 결과의 과학 재검토 범위는 신규 네 문서와 사전 추가 정의이며, 기존 모든 위키의 과학 내용 전체를 새로 재검토한 것으로 확대하지 않는다.

## 기존 문서 기준과 근거 연결

- `glossary.md` 기준 SHA-256 `c4700f39cac03a1235705eed2d74244a6fd7af632c1def0d954e914e823adcb6`. 이전 evidence `refs/quality/evidence/ml-glossary-2026-11-15.md` (`a54c48965691a3d48fe5228e4c8257491889d14a6a89738f7b89e6d3c46bc2ef`).
- `fidelity.md` 기준 SHA-256 `3bb7bc5c687faeba5090e7b6f4269a6f4035babd2e1960a325ab84c7e0d5fa55`. 이전 evidence `refs/quality/evidence/ml-glossary-2026-11-15.md` (`a54c48965691a3d48fe5228e4c8257491889d14a6a89738f7b89e6d3c46bc2ef`).
- `cnn-kernel-receptive-field.md` 기준 SHA-256 `39688c61695dd033a8f7deb105c4536ed418d8c6e831f583cd2dc7fd15d220d2`. 이전 evidence `refs/quality/evidence/ml-glossary-2026-11-15.md` (`a54c48965691a3d48fe5228e4c8257491889d14a6a89738f7b89e6d3c46bc2ef`).

## 원문 대조와 독립성

- 본문의 각 인용 위치와 registry의 sources/findings가 claim group의 직접 출처와 범위를 기록한다. 같은 Deep Learning 책의 여러 chapter와 D2L의 여러 chapter는 각각 한 provenance로 센다. TFN과 이를 따르는 NequIP는 같은 계열로 표시하고 그 둘만을 독립 두 출처로 사용하지 않는다.
- Training 전체는 ml_training_writer가 작성하고 ml_representation_writer가 독립 검토했다. Adam의 raw second moment, epsilon 위치, fixed-theta uniform gradient 가정, SGD-L2 등가, AdamW 원문 lambda와 본문 lambda의 재매개변수화까지 원문과 확인했다.
- Representation 전체는 ml_representation_writer가 작성하고 ml_training_writer가 독립 검토했다. Completeness 정의는 Bartok에 명시 귀속했다. Attention과 parity/active tensor rotation, cutoff와 initial features/global paths/readout 범위를 대조했다.
- Evaluation과 augmentation 전체 및 사전 대응 부분은 root가 작성하고 ml_rules_audit가 원문·식·수치·그림을 독립 검토했다. Transfer toy 추가 범위까지 최종 PASS다.
- 사전의 training/representation 행은 각 독립 교차 리뷰어가, evaluation/augmentation 행은 ml_rules_audit가 확인했다. 기존 fidelity/CNN의 의미보존 변경과 nav/형식도 별도 확인했다.
- Bibliography를 최초 등장 순서로 정리한 후, 이전→현재 각 항목의 저자/제목/URL/설명 보존과 번호 대응을 독립 확인했다. 직접 숫자 인용 링크 43개를 bibliography URL과 대조했다. 반열린 구간 문장 안의 Adam 인용 한 곳에서 남은 번호를 10으로 교정한 뒤 재검사했다.

## 자체 계산과 도식

- Training 예제 J(w)=1/2(2w−6)^2, Jprime=4(w−3). w0=1에서 eta=.1/.5/.6의 첫 w는1.8/5/5.8, J는2.88/8/15.68. e_t=(1−4eta)e_(t−1)에서0<eta<.5. Fraction으로 정확 검산했다.
- N103,B32의 단일 과정은 [32,32,32,7]이며10epoch×4step=40. CPU의 설치된 PyTorch2.0.1+cu117 BatchSampler/SequentialSampler에서도 drop_lastFalse=[32,32,32,7], True=[32,32,32]를 직접 확인했다. 참고한 공식2.15 문서 버전과 실제 실행 버전을 구분한다.
- g1=0,theta0=2,lambda=.1,eta=.01에서 Adam+L2의 mhat=.2,vhat=.04, AdamW 감소량−.002. 원문의 lambda_paper/alpha를 본문 lambda로 정의했다.
- MAE toy [0,0,3] eV는 MAE1, MSE3, RMSEsqrt3. Transfer toy의 오류 [.1,−.1,.2]/[.05,−.05,.1]/[.2,−.2,.2] eV의 MAE는 .1333/.0667/.2. 어떤 실험 결과도 아니다.
- Polynomial f1=x, f2=x+.5x(x²−1)는 x=−1,0,1에서 동일. x=.5에서.5/.3125, x=2에서2/5. 기준 참값을 가정하지 않고 미관측점에서 가능한 함수값 차이를 그렸다.
- Augmentation Q=[[0,−1,0],[1,0,0],[0,0,1]]로 F=[1,2,0]을 돌리면[−2,1,0]. scalar field rhoPrime(r)=rho(Q^T(r−t))는 Cohen의 inverse action에 g(r)=Qr+t를 대입한 자체 유도다. detQ=1의 변수변환으로 적분이 보존된다. 격자에서는 보간·경계 조건이 추가된다.
- Attention toy scores[1,0]의 가중치는 .7310586/.2689414, value가 diag(2,4)면 output[1.4621172,1.0757657]. 임의 embedding과 descriptor(2,0)/(2,−1), rank2 rotation [[4,−3,0],[−2,1,0],[0,0,5]]도 NumPy로 검산했다.
- 1Angstrom 간격 네 노드, cutoff1.1Angstrom의 sum+self 업데이트 h0=[1,2,4,8], h1=[3,7,14,12], h2=[10,24,33,26]. 노드0의 의존집합은1step{0,1},2step{0,1,2}. 고정 local graph/atom-only 초기 특징 조건을 본문에 명시했다.
- 자체 SVG 세 개는 논문 원그림이나 재료 계산 결과를 복제하지 않았다. 재현 원본은 refs/quality/figure-source/ml-evaluation-augmentation.py와 ml-symmetry-message-passing.py이며, Python/NumPy/Matplotlib 또는 표준 라이브러리로 생성한다. Inkscape PNG를 root와 별도의 과학 리뷰어가 직접 보아 수치·범위·레이블·겹침을 확인했다. 폰트는 도식 Roboto, 수학/분할 예시 DejaVu Sans다.

## 최종 검토 버전

- `glossary.md` SHA-256 `6876e18cc4c393cf464d0d90b6d73ff581bf2bbd0ef9ce52819fbb6e3c15a429`.
- `fidelity.md` SHA-256 `f22db8d6fae462528b77e03112617630143e9effae5364acb13520f894dcb11b`.
- `cnn-kernel-receptive-field.md` SHA-256 `1ddaf3e873a5279e2285bb68205ac9b418dc2eba32a1b8a6c1e00ed8bebec443`.
- `training-and-optimization.md` SHA-256 `fd8c22e7b575f17bcf5318413982a0b7e6d896ef655e52c2d2fd44e4586b2b33`.
- `evaluation-and-transferability.md` SHA-256 `96e432ddad071b0bfcbe81165f652031b469f6fb8ee906703f03f1000a00080b`.
- `representation-and-symmetry.md` SHA-256 `bfadc491651d2f658e2eac55b3dc2534dcf16aec59f148b559f7d4759fe8e896`.
- `data-augmentation.md` SHA-256 `a530c470475770ec6a55351deae06119aedbe7991eb16897ca3de394d8bf8c45`.

- 최종 독립 과학 검토는 PASS이며 unresolved scientific finding은 없다. 무결성 검사와 strict build는 별도 실행한다. 검증 기록은 사이트 메뉴와 문서 본문에 추가하지 않는다.

- Matplotlib SVG의 trailing whitespace와 비결정적 날짜/ID를 정리했다. Inkscape 렌더의 픽셀 동일성과 연속 두 번 생성한 SVG 해시 동일성을 확인했으며 과학 내용과 그림 좌표는 보존했다.
