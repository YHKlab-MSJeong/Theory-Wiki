# 머신러닝 용어 사전 초기 문서 검토

## 범위와 구성

- 목적은 논문에서 만난 ML 용어를 영문·한글로 찾아 정의·사용 맥락·수식·예제·관련 개념으로 이동할 수 있게 하는 것이다.
- 독자는 DFT·수송과 과학 ML 논문을 읽는 학습자다. 초기 범위는 fidelity/모델링 7개 항목, CNN 연산/RF 10개 항목이다. 신경망 학습 전체의 튜토리얼은 범위 밖이다.
- `computational-science/machine-learning/glossary.md`, `fidelity.md`, `cnn-kernel-receptive-field.md`의 신규 내용 전체를 검토했다. 기존 과학 문서 본문의 주장은 수정하지 않았다. 홈, domain index와 navigation에 진입 링크를 추가했다.
- 관련 용어는 묶음 문서에 서술하고 사전에서 해당 anchor로 이동한다. 문체에는 기존 humanizer 지침을 적용했다.

## 원문과 주장

- `supported`로 판단한 multi-fidelity 개념은 Perdikaris et al. 2017, Introduction와 §2(a), DOI 10.1098/rspa.2016.0751 및 Peherstorfer et al. 2018, §§1–3, DOI 10.1137/16M1082469의 독립 연구 계통을 대조했다. 모델/데이터의 수준, 관심 출력, 입력 범위와 상관관계를 포함한다.
- Chen et al. 2021의 PBE 자료와 고수준 계산·실험 자료 결합은 원문 보고인 `reported-primary`다. DOI 10.1038/s43588-020-00002-x, arXiv:2005.04338v3 Introduction, Results “Multi-fidelity Graph Networks”, Fig.1. 신경망 surrogate 표현도 해당 자료에 근거한다.
- XAI fidelity는 Ribeiro et al. 2016, §§2, 3.1–3.4, Eq.(2), DOI 10.1145/2939672.2939778와 Craven/Shavlik, NIPS 8 (1995), §3 “Empirical Evaluation”, pp.27–28를 대조했다. LIME의 구체 가중 제곱손실은 `reported-primary`로 기록한다. 참조 모델 예측 일치율과 정답 accuracy 비율을 구분한다.
- CNN kernel/filter와 channel·stride·padding·dilation·cross-correlation·shape는 PyTorch Conv2d 연산식/Parameters/Variables/Shape 및 TensorFlow tf.nn.conv2d의 patch 추출·filter shape를 대조했다. Goodfellow et al. Deep Learning Chapter 9, §§9.1–9.2,9.5와도 대조했다. 일반 convolution 식은 groups=1이고 공간 예제 조건을 명시했다.
- RF 점화식과 좌표 범위는 Araujo et al. Distill 2019, Problem setup, Single-path networks, Computing receptive field region, Arbitrary computation graphs, Other network operations를 대조했다. Luo et al. NIPS 2016 §§2–3은 RF와 gradient-based ERF의 독립 근거다. 최종 ERF 설명은 가중치·입력·영향량 및 영역 산정 기준을 포함한다.

## 자체 예제와 도식 검증

- 정답 [0,1,0,1], 원 모델·설명 모델 [0,0,1,1]을 대입하면 fidelity 1, accuracy 1/2다. 실제 학습 데이터가 아니다.
- Conv2d 채널 3→16, kernel3, groups1, bias 포함은 16×3×3×3+16=448개. n7,k3,s2,p1,d1의 출력 길이는 4다.
- 각 축 k3,d1,stride [1,2,1]의 (R,J)는 [(3,1),(5,2),(9,2)]다. 마지막 dilation만2이면 최종 R13이다. root와 ml_cnn_research가 각각 수식 대입과 입력 의존 집합 열거로 확인했다.
- 자체 SVG는 입력5×5→feature map3×3→출력1×1, 두 층 k3/s1/d1/p0를 표시한다. 최종 출력의 의존 입력 합집합25개를 재현 원본에서 assertion으로 확인했다. 출판 그림 및 학습 결과를 복제하지 않았다.
- 재현 원본은 `refs/quality/figure-source/cnn-receptive-field.py`다. XML, 벡터 요소, 동일 출력 재생성 및 PNG 미리보기의 글자·테두리·화살표를 확인했다. ml_rf_figure와 root, ml_cnn_research가 그림을 직접 보았다. 글꼴은 DejaVu Sans다. 그림의 최종 해시는 registry에 기록한다.

## 독립 검토

- 저자는 root다. ml_fidelity_research가 fidelity 전체와 glossary §1을 원문과 대조하고, §3 Empirical Evaluation, LIME 절 위치·샘플 집합·surrogate 출처를 교정한 최종본에 PASS를 회신했다.
- ml_cnn_research가 CNN 전체와 glossary §2, 수식·매개변수·연결 좌표·그림과 anchor를 독립 확인했다. 기울기의 미분 방향을 명확히 한 최종본에 PASS를 회신했다.
- ml_rf_figure는 도식 작성자다. 그림 검토자로는 별도의 ml_cnn_research를 기록한다.
- 모든 사전 항목의 링크는 명시 anchor를 이용한다. 자동 검사는 registry 무결성과 HTML을 확인하며, 과학 내용은 위 별도 원문 검토에 근거한다. 미해결 과학 주장 없음.
