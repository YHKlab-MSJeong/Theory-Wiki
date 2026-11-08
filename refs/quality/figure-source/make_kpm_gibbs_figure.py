#!/usr/bin/env python3
"""Reproduce a dimensionless Chebyshev/KPM Gibbs-ringing illustration.

The left panel expands a Heaviside step and the right panel expands a delta
peak at x=0, both with N=64 moments. It is an analytic demonstration, not
material data. Equations follow Weiße et al., Rev. Mod. Phys. 78, 275 (2006),
Sec. II.C and Fig. 1.
"""
from pathlib import Path
import argparse
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss


def jackson_coefficients(n_moments: int) -> np.ndarray:
    """Jackson damping factors for m=0,...,N-1 (Weiße et al. Eq. 71)."""
    n = np.arange(n_moments, dtype=float)
    angle = np.pi / (n_moments + 1)
    return ((n_moments - n + 1) * np.cos(n * angle)
            + np.sin(n * angle) / np.tan(angle)) / (n_moments + 1)


def chebyshev_dos(moments: np.ndarray, x: np.ndarray,
                  damping: np.ndarray | None = None) -> np.ndarray:
    """Reconstruct the DOS/function with the modified Chebyshev moments."""
    if damping is None:
        damping = np.ones_like(moments)
    theta = np.arccos(x)
    orders = np.arange(len(moments))[:, None]
    t_values = np.cos(orders * theta[None, :])
    series = damping[0] * moments[0] + 2 * np.sum(
        (damping[1:] * moments[1:])[:, None] * t_values[1:], axis=0
    )
    return series / (np.pi * np.sqrt(1 - x * x))


def moments_of_step(n_moments: int) -> np.ndarray:
    """Compute mu_m=integral_0^1 T_m(x) dx by Gauss-Legendre quadrature."""
    nodes, weights = leggauss(512)
    x = (nodes + 1) / 2
    weights = weights / 2
    theta = np.arccos(x)
    orders = np.arange(n_moments)[:, None]
    return np.sum(weights[None, :] * np.cos(orders * theta[None, :]), axis=1)


def make_figure(output: Path, n_moments: int = 64) -> None:
    plt.rcParams.update({
        "font.family": "Noto Sans CJK JP",
        "font.size": 9,
        "axes.labelsize": 9,
        "axes.titlesize": 9,
        "legend.fontsize": 7.5,
        "svg.fonttype": "none",
        "savefig.bbox": "tight",
    })
    x_step = np.linspace(-0.96, 0.96, 4001)
    step_mu = moments_of_step(n_moments)
    jackson = jackson_coefficients(n_moments)
    step_raw = chebyshev_dos(step_mu, x_step)
    step_jackson = chebyshev_dos(step_mu, x_step, jackson)

    x_delta = np.linspace(-0.72, 0.72, 3601)
    delta_mu = np.cos(np.arange(n_moments) * np.pi / 2)
    delta_raw = chebyshev_dos(delta_mu, x_delta)
    delta_jackson = chebyshev_dos(delta_mu, x_delta, jackson)

    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.05), constrained_layout=True)
    ax = axes[0]
    step_exact = np.where(x_step < 0, 0.0, np.where(x_step > 0, 1.0, 0.5))
    ax.plot(x_step, step_exact, color="black",
            linestyle=(0, (3, 2)), linewidth=1.15, label=r"기준 함수 $\Theta(x)$")
    ax.plot(x_step, step_raw, color="#D73027", linewidth=1.15,
            label="유한 차수 절단")
    ax.plot(x_step, step_jackson, color="#1F77B4", linewidth=1.45,
            label="Jackson 감쇠")
    ax.set_xlim(-0.8, 0.8)
    ax.set_ylim(-0.18, 1.22)
    ax.set_xlabel(r"스케일된 에너지 $x$")
    ax.set_ylabel(r"$f(x)$")
    ax.set_title(r"(a) 점프: 절단 진동과 Jackson 감쇠")
    ax.legend(loc="upper left", frameon=False)

    ax = axes[1]
    ax.axvline(0, color="black", linestyle=(0, (3, 2)), linewidth=1.15,
               label=r"기준 위치 $\delta(x)$")
    ax.plot(x_delta, delta_raw, color="#D73027", linewidth=1.15,
            label="유한 차수 절단")
    ax.plot(x_delta, delta_jackson, color="#1F77B4", linewidth=1.45,
            label="Jackson 감쇠")
    ax.set_xlim(-0.55, 0.55)
    ax.set_ylim(-2.0, 24.0)
    ax.set_xlabel(r"스케일된 에너지 $x$")
    ax.set_ylabel("근사 DOS")
    ax.set_title(r"(b) 고립 준위: 진동 억제와 피크가 넓어짐")
    ax.legend(loc="upper right", frameon=False)

    for ax in axes:
        ax.grid(False)
        ax.tick_params(direction="in", top=True, right=True, length=3.2, width=0.8)
        for spine in ax.spines.values():
            spine.set_linewidth(0.8)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, format=output.suffix.lstrip("."), dpi=180)
    if output.suffix.lower() == ".svg":
        svg_text = output.read_text(encoding="utf-8")
        output.write_text("\n".join(line.rstrip() for line in svg_text.splitlines()) + "\n", encoding="utf-8")
        fig.savefig(output.with_suffix(".png"), dpi=220)
    plt.close(fig)

    # Numerical checks relevant to the interpretation of the demonstration.
    raw_overshoot = max(0.0, np.max(step_raw - 1), -np.min(step_raw))
    jackson_overshoot = max(0.0, np.max(step_jackson - 1), -np.min(step_jackson))
    assert jackson[0] == 1.0
    assert np.all(np.isfinite(step_raw)) and np.all(np.isfinite(delta_jackson))
    assert max(np.max(step_raw - 1), -np.min(step_raw)) > 0.05
    assert max(np.max(step_jackson - 1), -np.min(step_jackson)) < 1e-3
    assert np.max(step_raw) > 1.05 and np.min(step_raw) < -0.05
    assert np.min(step_jackson) > -1e-10
    assert np.min(delta_raw) < -0.1
    assert np.min(delta_jackson) > -1e-10
    print(f"N={n_moments}; step overshoot raw={raw_overshoot:.5f}, "
          f"Jackson={jackson_overshoot:.5f}; delta min raw={np.min(delta_raw):.5f}, "
          f"Jackson={np.min(delta_jackson):.5f}; delta peak raw={np.max(delta_raw):.5f}, "
          f"Jackson={np.max(delta_jackson):.5f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--moments", type=int, default=64)
    args = parser.parse_args()
    make_figure(args.output, args.moments)
