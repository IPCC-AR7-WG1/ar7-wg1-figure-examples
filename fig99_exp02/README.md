Phytoplankton dynamics in the ocean
====================================
[![DOI](https://zenodo.org/badge/DOI/YOUR_ZENODO_DOI.svg)](https://doi.org/YOUR_ZENODO_DOI)
![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![GitHub release](https://img.shields.io/github/v/release/YOUR_ORG/YOUR_REPO?logo=github)

![Figure caption](/fig99_exp02/figure/fig_exp02.png?raw=true)

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
git clone https://github.com/IPCC-AR7-WG1/ar7-wg1-figure-examples.git
cd ar7-wg1-figure-examples
```

2. Create the environment

```bash
conda env create -f env/env_exp02.yml
```


## Expected image path

```bash
../fig99_exp02/figure/
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