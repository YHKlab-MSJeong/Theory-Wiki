# Dielectric response

유전 응답은 전기장에 대한 전자 분극과 이온 격자의 응답으로 나뉜다. 이 문서 묶음은 Born 유효전하, DFPT 계산, high-\(\kappa\) 재료 탐색, 기계학습 모델을 그 연결 관계에 따라 안내한다.

- [유전 응답과 유전율 텐서](dielectric-response.md)
- [Born 유효전하](born-effective-charge.md)
- [DFPT 유전 응답 계산](dfpt-dielectric-response.md)
- [High-\(\kappa\) 유전체의 재료 기준](high-k-screening.md)
- [2015년 산화물 탐색 사례](cases/yim-2015-high-k-oxides.md)
- [2018년 비산화물 탐색 사례](cases/lee-2018-nonoxide-dielectrics.md)
- [Born 유효전하 기계학습: SevenNet-Polar](ml-born-effective-charge.md)
- [Yu–Kumagai 유전 텐서 기계학습 사례](cases/takigawa-2026-prx-ionic-dielectric-ml.md)

## 1. 문서 간 연결

정적 격자 유전 응답에서 전자 항 \(\varepsilon_\infty\)와 이온 항은 서로 다른 입력을 갖는다. 이온 항은 Born 유효전하와 조화 포논의 주파수·고유벡터에 의해 정해진다. 따라서 BEC 예측 모델은 이온 유전율을 얻는 데 필요한 물리량 하나를 제공하지만, 그 자체가 유전율 텐서 전체를 직접 예측했다는 뜻은 아니다. [Born 유효전하](born-effective-charge.md), [DFPT 계산](dfpt-dielectric-response.md)

## 2. 읽는 순서

처음에는 [유전 응답](dielectric-response.md)에서 전체 분해를 확인한 뒤, [Born 유효전하](born-effective-charge.md)와 [DFPT 계산](dfpt-dielectric-response.md)으로 넘어간다. 응용 기준은 [High-\(\kappa\) 유전체](high-k-screening.md)에서 다루며, 마지막 네 문서는 논문별 계산 범위와 ML 접근의 차이를 정리한다.
