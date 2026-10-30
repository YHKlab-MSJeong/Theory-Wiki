---
description: 계면 거칠기의 통계 모형과 전자 산란 모형을 구분해 설명한다.
---

# Surface-roughness scattering model

## 1. 계면 높이의 통계적 기술

평균 계면에서의 높이 편차를 \(\Delta(\mathbf r)\)라 두면, 이 문서의 통계적 surface-roughness model은 autocorrelation \(C(\mathbf r)=\langle\Delta(\mathbf r)\Delta(\mathbf0)\rangle\)와 Fourier spectrum \(S(\mathbf q)\)를 정한다. 예를 들어 exponential 모형은

\[
C(r)=\Delta_{\mathrm{rms}}^2\exp\!\left(-\frac{\sqrt2 r}{\Lambda}\right)
\]

처럼 쓸 수 있다. \(\Delta_{\mathrm{rms}}\)는 RMS height, \(\Lambda\)는 이 정의에서의 correlation length다. Gaussian과 exponential은 서로 다른 correlation 함수 모형이고, \(\exp(-r/\Lambda)\)와 \(\exp(-\sqrt2r/\Lambda)\)는 같은 exponential 모형에서도 length convention이 다르다. [Badami, Ch. 2 §2.2.2, 식 (2.24)–(2.26)](https://air.uniud.it/retrieve/e27ce0c5-bae9-055e-e053-6605fe0a7873/Badami_PhDThesisUploaded.pdf), [Sano, §II.A, 식 (3)–(5)](https://arxiv.org/html/2604.22155)

## 2. 통계에서 산란률로 가는 추가 가정

rough interface가 confinement potential을 \(\delta U\)만큼 바꾸면 상태 \(\lvert k\rangle\) 사이의 elastic transition rate는 Born 또는 Fermi golden-rule 근사에서

\[
W_{k\rightarrow k'}=\frac{2\pi}{\hbar}\left|\langle k'\lvert\delta U\rvert k\rangle\right|^2\delta(E_{k'}-E_k)
\]

로 쓴다. ensemble-averaged \(\lvert M_{kk'}\rvert^2\)에는 roughness autocorrelation의 Fourier spectrum \(S(\mathbf q)\)와 wavefunction overlap·경계 전위 변조가 반영된다. screening은 선택한 모형에서 추가될 수 있다. 따라서 \(\Delta_{\mathrm{rms}}\)와 \(\Lambda\)만으로 보편적인 mobility나 scattering rate를 정할 수 없다. [Sano, §II.C, 식 (11)](https://arxiv.org/html/2604.22155), [Badami, Ch. 2 §2.1, 식 (2.1)–(2.2)](https://air.uniud.it/retrieve/e27ce0c5-bae9-055e-e053-6605fe0a7873/Badami_PhDThesisUploaded.pdf)

## 3. 보고해야 할 항목

모형을 제시할 때에는 \(C(r)\) 또는 \(S(q)\)의 함수형과 \(\Lambda\) convention, \(\Delta_{\mathrm{rms}}\), 계면별 correlation, wavefunction·screening 계산법, Born 근사의 사용 여부를 함께 적는다. 실험 AFM의 거칠기와 전자에 유효한 buried interface spectrum은 같다고 가정하지 말고, 필요한 경우 독립적으로 calibration한다.

## 4. 참고 문헌

1. C. Alexander, A. Asenov, *Statistical MOSFET Current Variation Due to Variation in Surface Roughness Scattering* (2011), §II.A, https://in4.iue.tuwien.ac.at/pdfs/sispad2011/pdf/10-1.pdf.
2. O. Badami, PhD thesis (2017), Ch. 2, https://air.uniud.it/retrieve/e27ce0c5-bae9-055e-e053-6605fe0a7873/Badami_PhDThesisUploaded.pdf.
3. N. Sano, *Microscopic Modeling of Surface Roughness Scattering in Inversion Layers of MOSFETs Based on Ando’s Linear Model* (2026 preprint), §II–III, https://arxiv.org/html/2604.22155.
