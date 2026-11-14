# ML 문서 RGLee-Wiki 규칙 재확인

## 조사 범위와 버전

- 2026-11-15에 GitHub connector의 `github_fetch`로 RGLee-Wiki 원문 네 파일을 직접 읽었다. 프로젝트가 지정한 pinned commit은 `c2ac6381caece612ec28eeb4ddddd1b75226cc2f`다. 확인 당시 default branch는 `main`, 그 HEAD는 `fe8a6bc07dbb7d63afc5b55684b056dc8d31bd52`이며 commit date는 2026-10-29다.
- pinned와 current main의 `AGENTS.md`, `refs/format.md`, `refs/research-workflow.md`, `refs/quality/README.md` 본문이 네 파일 모두 동일했다. 두 버전의 원문 텍스트를 `/tmp/ml-rules-source/`에 보관했다.
- 해당 텍스트 SHA-256은 AGENTS `e8276b721cf1721781060f797e24e5bdd7d526b3a8e612c5ba1c5b851657a51e`, format `35653b3b2ba5b94e32c52069550a3cab43d66675f9890d6d4174a60615dd66e3`, research-workflow `b9ba1d8fc25f66fcefce302473e6d9e17a9adf8e7c02fa6ee69aece15f7b273e`, quality README `6fc4910b854755a685649d0729830ae324d27ff35c46a267b05793c239cedd0f`다. Git blob SHA와는 다른 종류의 값이다.
- local fixture `/tmp/theory-wiki-ml-expansion-ro2aNX`의 AGENTS, ML index와 glossary/fidelity/CNN 본문, 해당 nav/index, 세 문서의 현재 registry 항목과 기존 evidence만 살폈다. 원본과 fixture의 docs/registry를 변경하지 않았다. 모든 위키 문서의 규칙 준수나 사실을 재검증한 결과로 확대할 수 없다.

## 반영할 항목

### 제목과 연결 문구

`refs/format.md` §3의 대표 영문 제목·sentence-case·동일한 nav/index 짧은 이름 규칙에 따라 아래 ML H1과 연결 라벨을 함께 맞춘다. 본문과 검색 표의 한글 용어는 유지한다.

- glossary.md L5의 한국어 H1을 `Machine learning glossary`로 정리한다.
- fidelity.md L5의 혼합형 H1을 `Fidelity and multi-fidelity learning` 등 범위가 드러나는 영문 제목으로 정리한다.
- cnn-kernel-receptive-field.md L5의 혼합형 title case H1을 `CNN kernels and receptive fields` 등 sentence case로 정리한다.
- machine-learning/index.md L1과 L3–5, computational-science/index.md L9 및 관련 nav 라벨을 대응시킨다. nav의 `Overview`는 기존 index 역할에 맞는다. 위 제안 제목 자체는 한 가지 구현 선택이다.

### 최초 약어 정의

`refs/format.md` §3은 `full English name (ABBR.)` 순서와 문서별 첫 사용 정의를 요구한다.

- glossary.md L7의 첫 CNN 전에 `convolutional neural network (CNN)`를 둔다.
- fidelity.md L17의 PBE는 `Perdew–Burke–Ernzerhof (PBE)`, L25의 DFT는 `density functional theory (DFT)`로 확장한다.
- fidelity.md L31의 XAI와 L57의 LIME는 각각 `Explainable artificial intelligence (XAI)`, `Local Interpretable Model-agnostic Explanations (LIME)` 순서로 둔다.
- cnn-kernel-receptive-field.md L7은 `Convolutional neural network (CNN)` 순서로 둔다. L15의 RGB는 `red–green–blue (RGB)` 등으로 정의한다.
- 한글 뜻의 병기는 검색 독자에게 필요할 때 보조할 수 있다. 위키 내 다른 문서의 첫 정의로 해당 문서의 첫 정의를 대신하지 않는다.

### CNN 핵심 기호와 캡션

`refs/format.md` §§4–6은 기호·규약·가정 정의와 캡션 수식 형식을 요구한다.

- CNN L15의 H,W,C에 높이·너비·채널 수 정의를 둔다. L26의 가중치 W와 폭 W가 겹치므로 크기는 H_in,W_in 등으로 구별할 수 있다.
- CNN L24–29의 식에 y가 출력, W가 학습 가중치, b_o가 출력 채널 bias, a/b가 kernel 내부 공간 인덱스라는 정의를 보충한다. 식의 groups=1 가정도 직접 적으면 적용 범위가 분명하다.
- CNN L65–73의 점화식에서 ℓ이 층 번호이고 k_ℓ,s_ℓ,d_ℓ이 해당 층의 kernel 폭·stride·dilation이라는 점을 명시한다. R,J의 원 입력 기준 의미는 이미 설명되어 있다.
- CNN L60 `<figcaption>`의 인라인 수식은 `$...$` 형식으로 맞춘다. 현재 pymdownx.arithmatex generic 설정을 확인했으므로 본문의 다른 delimiter를 렌더링 오류로 판정하지 않았다.

## 유지할 운영 기준과 남은 검증

- local AGENTS의 명시 예외에 따라 검증된 위키 자체 도식·수학 플롯, `/tmp` fixture, `reported-primary` 문헌 사실을 허용한다. upstream의 신규 그림 금지와 `experiment/` 사용 지침을 이번 문서의 수정 항목으로 채택하지 않았다.
- local quality registry와 checker를 사용한다. upstream `quality.sh`, `documents.yaml`, skill 이름의 도입이나 도구 전환은 이 감사 결과에 포함하지 않는다.
- RF 점화식·ERF 주장에는 현 registry에 Araujo와 Luo의 독립 provenance가 함께 기록되어 있다. 본문 한 문장의 단일 인용 표기만으로 독립 근거 미확보라고 판정하지 않았다. 기존 근거의 실제 source-support 검토와 이번 형식 감사를 구별한다.
- 의미보존 제목·기호 설명 변경은 기존 검증 근거와 연결해 기록한다. 새 평가·증강 문서는 전체 비자명 주장에 직접 확인한 독립 원문 근거 두 개 이상, 독립 사실 검토, 최종 문서·이미지·evidence hash와 strict build가 필요하다. 특정 논문 보고는 local `reported-primary` 규칙을 따른다.
- 이 감사에서 scientific source-support 전체를 재검증하거나 MkDocs build를 실행하지 않았다. root가 최종 변경을 통합한 뒤 기존 local 절차로 검증한다.

## 직접 확인한 upstream 원문

- [Pinned AGENTS](https://github.com/ryonggyulee/RGLee-Wiki/blob/c2ac6381caece612ec28eeb4ddddd1b75226cc2f/AGENTS.md), [current AGENTS](https://github.com/ryonggyulee/RGLee-Wiki/blob/fe8a6bc07dbb7d63afc5b55684b056dc8d31bd52/AGENTS.md)
- [Pinned format](https://github.com/ryonggyulee/RGLee-Wiki/blob/c2ac6381caece612ec28eeb4ddddd1b75226cc2f/refs/format.md), [current format](https://github.com/ryonggyulee/RGLee-Wiki/blob/fe8a6bc07dbb7d63afc5b55684b056dc8d31bd52/refs/format.md)
- [Pinned research workflow](https://github.com/ryonggyulee/RGLee-Wiki/blob/c2ac6381caece612ec28eeb4ddddd1b75226cc2f/refs/research-workflow.md), [current research workflow](https://github.com/ryonggyulee/RGLee-Wiki/blob/fe8a6bc07dbb7d63afc5b55684b056dc8d31bd52/refs/research-workflow.md)
- [Pinned quality README](https://github.com/ryonggyulee/RGLee-Wiki/blob/c2ac6381caece612ec28eeb4ddddd1b75226cc2f/refs/quality/README.md), [current quality README](https://github.com/ryonggyulee/RGLee-Wiki/blob/fe8a6bc07dbb7d63afc5b55684b056dc8d31bd52/refs/quality/README.md)

## 최종 범위 보충 감사

- root가 최초 세 문서의 제목, 최초 약어, CNN 기호와 캡션을 교정한 뒤 이를 다시 읽었다. H1은 대표 영문 sentence case, 본문은 한국어 설명으로 구성되었다. 과학 기호의 뜻을 보충하고 가중치에 mathcal W를 사용한 변경은 기존 식의 의미를 보존한다.
- 추가 문서를 포함한 여덟 ML 페이지의 H1, H2/H3 번호, H4 부재, article description, nav 단일 등록, 상대 파일과 명시 anchor, figure/figcaption 수를 읽기 전용 프로그램으로 검사했고 오류가 없었다. bibliography 재정렬 전후 일곱 article의 각 서지 항목 내용이 대응 mapping 아래 보존됨을 확인했다.
- 직접 URL을 단 본문 숫자 인용 43개를 bibliography 번호의 URL과 비교했다. training의 Adam 모멘트 문단에서 8이 Stanford 자료를 가리키는 불일치를 발견해 root에 전달했고 10으로 교정한 최종본에서 43개 모두 일치했다.
- Evaluation·augmentation 전체와 glossary §4/§6의 독립 과학 검토 결과는 `/tmp/ml-evaluation-augmentation-review.md`에 따로 기록했다. 이 기록의 전체 검토 범위를 다른 문서로 확대하지 않는다. 초기 세 문서는 이전 검증에서 바뀐 형식과 기호 설명만 확인했다.
- 원본과 fixture docs/registry의 최종 작성·등록·build는 root의 소유 범위다. 이 감사자는 `/tmp` 감사 기록에만 썼다.
