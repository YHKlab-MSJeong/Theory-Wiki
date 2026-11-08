---
description: Lee 등 2018년 비산화물 유전율·밴드갭 탐색의 대상과 계산 범위를 요약한다.
---

# Lee et al. 2018: non-oxide dielectrics

Lee 등은 산화물 중심의 유전체 후보 탐색을 비산화물로 확장해, 고유전율과 넓은 밴드갭을 함께 만족할 가능성이 있는 조성을 조사했다. 대상에는 탄화물, 질화물, 황화물, 인화물과 할로겐화물이 포함됐다. [1, Abstract and Introduction]

<figure markdown="span">

  ![비산화물 화합물의 계산 전자·이온 유전율과 밴드갭을 비교한 논문 Figure 4.](images/lee-2018-fig4.png)

  <figcaption markdown="1">
  **그림 1.** M. Lee, Y. Youn, K. Yim, S. Han, “High-throughput ab initio calculations on dielectric constant and band gap of non-oxide dielectrics,” *Scientific Reports* 8, 14794 (2018), Fig. 4, [DOI](https://doi.org/10.1038/s41598-018-33095-6). [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). 원문 PDF에서 페이지 여백과 논문 캡션을 덜어 내고 도판 영역을 수록했다. 축·데이터·색상은 수정하지 않았다.
  </figcaption>
</figure>

## 1. 계산 파이프라인

논문은 869개 이원 화합물을 조사하고, 그중 절연체 449개의 유전 응답을 표로 정리한다. 별도로 415개 삼원 불화물을 추가 평가해 BiF\(_3\), LaF\(_3\), BaBeF\(_4\) 등을 후보로 제시한다. 계산 방법에는 VASP와 DFPT가 쓰였으며, Born 유효전하와 포논 주파수·유전 응답이 이온 기여를 평가하는 데 포함된다. 저자들은 DFPT 민감성을 고려해 k점 밀도를 높였다고 기술한다. 이 수와 계산 내용은 논문 보고값이며 독립 재현 결과를 뜻하지 않는다. [1, Abstract, Methods, and Results]

<figure markdown="span">

  ![86개 이원 불화물과 415개 삼원 불화물의 밴드갭과 유전율 지도. 점 색은 figure of merit를, 원형 테두리 색은 선별된 안정·준안정 후보를 나타낸다.](images/lee-2018-fig5.png)

  <figcaption markdown="1">
  **그림 2.** M. Lee, Y. Youn, K. Yim, and S. Han, “High-throughput ab initio calculations on dielectric constant and band gap of non-oxide dielectrics,” *Scientific Reports* 8, 14794 (2018), Fig. 5, [DOI](https://doi.org/10.1038/s41598-018-33095-6), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). 원문 PDF에서 페이지 여백과 논문 캡션을 덜어 내고 도판 영역을 수록했다. 데이터·축·범례·색상은 수정하지 않았다.
  </figcaption>
</figure>

이 접근은 물성 표와 후보 검색을 연결하지만, 계산된 bulk 값이 합성 가능성이나 계면 성능을 직접 예측하지는 않는다. 예를 들어 열·화학 안정성, 전극·반도체와의 밴드 정렬, 결함과 박막 성장성은 별도 검증 대상이다. [1, Discussion; 2, §2–4]

## 2. 보고된 후보와 해석 경계

저자들은 3원 불화물 중 BaBeF\(_4\)에 대해 밴드갭 9.7 eV와 유전율 17을 계산 보고값으로 제시한다. 이는 특정 구조 및 계산 설정에 대한 논문 보고값이며 독립 재현 결과가 아니다. 이 결과를 실험에서 확인된 소자 성능이나 보편적인 조성 경향으로 확대해서는 안 된다. [1, Results]

유전 응답의 계산식과 BEC·포논의 역할은 [DFPT 유전 응답](dfpt-dielectric-response.md)과 [Born 유효전하](born-effective-charge.md)에서 설명한다. 같은 수치를 비교하려면 정적/전자 유전율, 구조상, 밴드갭 계산법과 단위·평균 규약을 일치시켜야 한다. [1, Methods; 3, §II–III]

## 3. 참고 문헌

1. M. Lee, Y. Youn, K. Yim, and S. Han, “High-throughput ab initio calculations on dielectric constant and band gap of non-oxide dielectrics,” *Scientific Reports* **8**, 14794 (2018), https://doi.org/10.1038/s41598-018-33095-6.
2. J. Robertson, *European Physical Journal Applied Physics* **28**, 265–291 (2004), https://doi.org/10.1051/epjap:2004206.
3. X. Gonze and C. Lee, *Physical Review B* **55**, 10355 (1997), https://doi.org/10.1103/PhysRevB.55.10355.
