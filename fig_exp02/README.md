Phytoplankton dynamics in the ocean
====================================
[![DOI](https://zenodo.org/badge/DOI/YOUR_ZENODO_DOI.svg)](https://doi.org/YOUR_ZENODO_DOI)
![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![GitHub release](https://img.shields.io/github/v/release/YOUR_ORG/YOUR_REPO?logo=github)

Figure 2.31  From the IPCC Working Group I Contribution to the Sixth Assessment Report: Chapter 2
![Figure caption](/fig02_31/figure/IPCC_AR6_WGI_Figure_2_31.png?raw=true)

## Contents

- [Contents](#contents)
- [Description](#description)
- [Installation](#installation)
- [Expected image path](#expected-image-path)
- [How to cite](#how-to-cite) 
  - [Figure Citation](#figure-citation)
  - [Repository Citation](#repository-citation)
- [Disclaimer](#disclaimer)


## Description

(a) Climatology of chlorophyll-a concentration derived from ocean-colour data (1998–2018); (b) Linear trends in chlorophyll concentration. Trends are calculated using OLS regression with significance assessed following AR(1) adjustment after Santer et al. (2008) (‘×’ marks denote non-significant changes). (c) Histogram of linear trends in chlorophyll concentration, after area weighting and with per-pixel uncertainty estimates based on comparison with in situ data. Further details on data sources and processing are available in the chapter data table (Table 2.SM.1).

## Installation

1. Clone the repository

```bash
git clone https://github.com/YOUR_ORG/YOUR_REPO.git
cd YOUR_REPO
```

2. Create the environment

All code is written in python 3.7+ and mainly uses commonly available packages. The plotting functions are based on cartopy which can be a bit difficult to install, it therefore advisable to use the [conda](https://docs.conda.io/en/latest/miniconda.html) package manager:

```
conda env create -f environment.yml
conda activate ipcc
```

Download, load, and process the OC-CCI files as follows:

```
>>> import chl_analysis
>>> chl_analysis.process()
```
The parallelized setup is based on a machine with at least 32GB RAM. Change the *islice* attribute in the *process* function to a lower value if memory is an issue. For example:

```
>>> chl_analysis.process(islice=270)
```

Generate the figures with:

```
>>> chl_analysis.plot_chl_clim()
>>> chl_analysis.plot_hatched_chl_trend()
```


## Expected image path

```bash
../fig02_31/figure/
```

## How to cite

If you use this repository or any of its contents in your work, please cite it appropriately.

### Repository Citation
This repository includes a `CITATION.cff` file for citation. You can generate a citation in your preferred format using:

```bash
cffconvert --format bibtex
```

### Figure Citation
If you use Figure <figure number eg 3.4> from the IPCC report included in this repository, please cite it as:

Provide a full citation of the IPCC report chapter containing the figure, according to the IPCC editorial citation rules.


## Disclaimer
Please note that figures in this repository may differ from those in the published version due to the editorial process. The repository contains the latest available versions prior to publication.


# 🟡Checklist Before Finalizing (delete when you complete the README.md)

- Updated title and badges

- Correct figure number and chapter

- Real image path and preview

- Descriptive summary in the Description section

- Image output paths match the real output

- At least one scientific source listed

- Figure and repository citation are accurate
