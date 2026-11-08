# 논문과 배경 이론 문서 보강: 변경 검토

- 검토일 2026-11-09. 범위는 아래 baseline 이후 변경분이며, 과거 검토를 다시 수행했다고 표현하지 않는다.
- Yim·Lee 저자: papers_yim_lee; 독립 검토: paper_inventory 및 통합 담당자가 Yim 원문 PDF의 구조 제외 조건을 별도 확인. Yim 원문 PDF pp.2–5, Fig.3–4, Table 1; Lee PMC Results, Methods, Figs.2–5, Table 1.
- Takigawa 저자: paper_takigawa; 독립 검토: papers_yim_lee. APS PDF §§II.A–B, IV.A–B, Fig.2–4, Tables I–III. 안정성의 Γ점 4번째 주파수 0.2 THz 기준을 재대조했다.
- SevenNet 저자: paper_inventory; 독립 검토: paper_takigawa. arXiv v3 §§2.1–2.4, 4.2, 4.4–4.7, Tables 1–3, Fig.1–2, 7–8, Supplement §10 Eq.(S1). 본문 PS-M 0.063e와 Abstract/Table 1의 0.0063e, Fig.2 본문 PS-L과 캡션 PS-M의 불일치를 명시한다. 손실의 성분 정규화에 대한 리뷰 수정 후 재검토했다.
- Born 저자: papers_yim_lee; 독립 검토: paper_inventory. Wu–Vanderbilt–Hamann §II.A Eqs.(3)–(8), exciting tutorial §§1–3, FHI-aims 매뉴얼 §3.42, Gonze–Lee §VII Eq.(46), Baroni §§II.C.2, II.D.2, EPW 장거리 기여. 가상 단위 예제 2×1.602176634e−19×1e−12/1e−28 = 3.204353268e−3 C/m².
- DFPT 저자: paper_takigawa; 독립 검토: papers_yim_lee. Gonze–Lee §§III–VIII, Baroni §§II.C, II.D.2, III.B Eq.(150), Takigawa §IV.B Eqs.(6)–(10); SI 모드합의 정규화, 단위 및 고정 전기장 경계 조건 검토. Shpiro et al. §2 Eqs.(12)–(13)로 움직이는 비직교 기저와 overlap 변화를 확인했다. 주파수 1.1배일 때 1/1.1²=0.826446.
- High-κ 저자: 통합 담당자; 독립 검토: paper_inventory. Robertson 2004 §1.2 Eqs.(2)–(3), §§2.4,4 및 Wilk et al. 2001 §§II, V.A Eq.(11), VI.A, Lee 2018 Fig.5. 직렬층 EOT 0.5+3.9×5/20=1.475 nm, electron/hole barrier 부호와 가정을 재검산했다.
- HamGNN 및 DFTH 수정은 기존 내용에 대한 이론 문서 연결 및 MkDocs 열린 접이식 블록으로의 서식 변경이다. 기존 주장의 의미와 출처를 유지했다.
- 논문별 수치·사례는 원문 보고값으로만 표기하며 일반적 보증이나 독립 재현으로 확대하지 않는다. 관련 이론 사실은 별개 출처 두 개 이상으로 확인한다. 인용 위치, 링크, 기존 그림 해시, 한글 문장을 확인했다. Humanizer는 변경 범위에 한정하며 과학 검토와 별개다.

## 이전 문서 해시
- `computational-materials-science/dielectric-response/born-effective-charge.md`: `5b67a5374621e086ba6a53d90a1f5edb5334f6f3a20b982e55ea9e1c8c5b1b8c`
- `computational-materials-science/dielectric-response/dfpt-dielectric-response.md`: `8c5ce526f70b2774e9144f5c89f27e7afccd9891aef9bd4ca86997c1e23e3d56`
- `computational-materials-science/dielectric-response/high-k-screening.md`: `8ac184c932a24ad92435f38f9434e73a610358e9c809235c211b5a03a14e0f76`
- `computational-materials-science/dielectric-response/yim-2015-high-k-oxides.md`: `2b1313ba84562aebbec1c520e100fc4c810220f25cf226e3c111042369fdd777`
- `computational-materials-science/dielectric-response/lee-2018-nonoxide-dielectrics.md`: `e641e804e0660d3e278ab056012b62e644d0f53b1cf98f383213f29b0fcedcc7`
- `computational-materials-science/dielectric-response/takigawa-2026-prx-ionic-dielectric-ml.md`: `fa0b115a214e94b985ae4bcc660ee856bc113582eb13505878ee4b7cbd3df124`
- `computational-materials-science/dielectric-response/ml-born-effective-charge.md`: `22da0df98eb835e3d51ff5387ccb1150543f2464586aa1a62a3325c9751d1c76`
- `computational-materials-science/quantum-transport/hamgnn-negf.md`: `69bb19aadd81c644b23c9665589c06959db9ecc9193610c72f9e913496cca94c`
- `computational-materials-science/quantum-transport/dfth-negf.md`: `ec8ff055836992c3309b1afbffdb5ea04c96a0f2cfef2e6d2e81ec9b35e2ba68`
