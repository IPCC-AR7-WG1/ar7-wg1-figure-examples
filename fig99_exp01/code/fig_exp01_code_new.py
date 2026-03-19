"""
Example code based on AR6
"""

from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

REGIONS = [
    "Northern Europe",
    "W. & C. Europe",
    "Mediterranean",
    "Sahara/Sahel",
    "West Africa",
]

PMIP4_CMIP6_MODELS = [
    "AWI-ESM-1-1-LR",
    "CESM2",
    "EC-Earth3-LR",
    "FGOALS-f3-L",
    "FGOALS-g3",
    "GISS-E2-1-G",
    "HadGEM3-GC31-LL",
    "INM-CM4-8",
    "IPSL-CM6A-LR",
    "MIROC-ES2L",
    "MPI-ESM1-2-LR",
    "MRI-ESM2-0",
    "NESM3",
    "NorESM1-F",
    "NorESM2-LM",
    "UofT-CCSM-4",
]

PMIP3_CMIP5_MODELS = [
    "BCC-CSM1-1",
    "CCSM4",
    "CNRM-CM5",
    "CSIRO-Mk3L-1-2",
    "CSIRO-Mk3-6-0",
    "EC-EARTH-2-2",
    "FGOALS-g2",
    "FGOALS-s2",
    "GISS-E2-R",
    "HadGEM2-CC",
    "HadGEM2-ES",
    "IPSL-CM5A-LR",
    "MIROC-ESM",
    "MPI-ESM-P",
    "MRI-CGCM3",
]

CMIP6_MODEL_COLORS = {
    "AWI-ESM-1-1-LR": (0.600, 0.000, 1.000),
    "CESM2": (0.2627, 0.6980, 0.8471),
    "EC-Earth3-LR": (0.4863, 0.3882, 0.7216),
    "FGOALS-f3-L": (0.9725, 0.6039, 0.1098),
    "FGOALS-g3": (0.9725, 0.6039, 0.1098),
    "GISS-E2-1-G": (0.4667, 0.1137, 0.4824),
    "HadGEM3-GC31-LL": (0.4784, 0.5451, 0.1490),
    "INM-CM4-8": (0.9686, 0.2627, 0.2627),
    "IPSL-CM6A-LR": (0.3569, 0.3255, 0.6824),
    "MIROC-ES2L": (0.7216, 0.3725, 0.7137),
    "MPI-ESM1-2-LR": (0.3647, 0.6314, 0.6353),
    "MRI-ESM2-0": (0.6784, 1.000, 0.1843),
    "NESM3": (0.6824, 0.6667, 0.6667),
    "NorESM1-F": (0.9451, 0.2275, 0.6549),
    "NorESM2-LM": (0.9451, 0.2275, 0.6549),
    "UofT-CCSM-4": (0.8039, 0.8039, 0.000),
}

PMIP3_COLOR = (37 / 255, 81 / 255, 204 / 255)


# ---------------------------------------------------------------------
# Data Loading
# ---------------------------------------------------------------------

def load_model_data(filepath: Path) -> tuple[Dict[str, np.ndarray], Dict[str, np.ndarray]]:
    """Load PMIP3 and PMIP4 model data."""
    data = pd.read_csv(filepath, header=205)

    pmip4 = {
        model: data[str(i + 2)].dropna().to_numpy(float)
        for i, model in enumerate(PMIP4_CMIP6_MODELS)
    }

    pmip3 = {
        model: data[str(i + 18)].dropna().to_numpy(float)
        for i, model in enumerate(PMIP3_CMIP5_MODELS)
    }

    return pmip3, pmip4


def load_reconstruction_data(filepath: Path) -> List[List[float]]:
    """Load reconstruction data grouped by region."""
    df = pd.read_csv(filepath, header=21)

    region_col = df["1"]
    value_col = df["2"]

    grouped = {region: [] for region in REGIONS}

    for region, value in zip(region_col, value_col):
        if region in grouped:
            grouped[region].append(value)

    return [grouped[r] for r in REGIONS]


# ---------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------

def create_plot(recons, pmip3, pmip4):
    """Generate Figure 3.11."""
    fig, ax = plt.subplots(figsize=(18 / 2.54, 12 / 2.54))

    ax.set_title("Precipitation change at the Mid-Holocene", loc="left", fontsize=11)
    ax.set_ylim(-400, 800)
    ax.set_xlim(0, 5)

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    p1 = np.arange(0.3, 5.3, 1)
    p2 = np.arange(0.5, 5.5, 1)
    p3 = np.arange(0.7, 5.7, 1)

    # Reconstructions
    ax.boxplot(recons, positions=p1, widths=0.1, showfliers=False)

    # PMIP3 models
    for i, (model, values) in enumerate(pmip3.items()):
        ax.plot(
            p2,
            values,
            marker="o",
            color=PMIP3_COLOR,
            fillstyle="none",
            linestyle="None",
            ms=5,
            label="PMIP3 models" if i == 0 else None,
        )

    # PMIP4 models
    for model, values in pmip4.items():
        ax.plot(
            p3,
            values,
            marker="o",
            color=CMIP6_MODEL_COLORS[model],
            fillstyle="none",
            linestyle="None",
            ms=6,
            label=model,
        )

    ax.axhline(0, color="grey", linestyle="dotted", linewidth=0.5)

    ax.set_xticks(p2)
    ax.set_xticklabels(REGIONS, fontsize=9)
    ax.set_ylabel("(mm yr$^{-1}$)", fontsize=9)

    legend = ax.legend(edgecolor="None", facecolor="None", fontsize=9)
    for line, text in zip(legend.get_lines(), legend.get_texts()):
        text.set_color(line.get_color())

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main():
    base = Path("../data/final_data")

    model_file = base / "map_midHolocene_models.csv"
    recon_file = base / "map_midHolocene_reconstructions.csv"

    pmip3, pmip4 = load_model_data(model_file)
    reconstructions = load_reconstruction_data(recon_file)

    create_plot(reconstructions, pmip3, pmip4)


if __name__ == "__main__":
    main()