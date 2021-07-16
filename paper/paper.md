---
title: 'xicorr: A Python package a novel tie-breaking correlation metric'
tags:
  - Python
  - statistics
  - Correlation
authors:
  - name: Venkata Naga Pranathi Vemuri
    orcid: 0000-0002-5748-9594
    affiliation: 1
  - name: Phoenix Aja Logan
    orcid: 0000-0003-4581-0552
    affiliation: 2
  - name: Olga Borisovna Botvinnik
    orcid: 0000-0003-4412-7970
    affiliation: 1
affiliations:
 - name: Chan Zuckerberg Biohub
   index: 1
 - name: Chan Zuckerberg Initiative
   index: 2

date: 15 July 2021
bibliography: paper.bib
---


# Summary
## Python implementation of `xicor`

Tie-breaking in correlation computation is a challenging problem. Given two vectors $X$ and $Y$,
Computing correlations in sparse data, where the majority of the values are zero, is challenging as many of the pairwise comparisons result in ties.
$Xi$ is a novel coefficient of correlation introduced by @chatterjee2020new.

Only [`scipy.stats.kendalltau`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kendalltau.html) has multiple options of breaking ties.

![Correlation coefficients computed on Anscombe's quartet dataset. In particular, "dataset = IV" in the lower right corner has a Xi/$\Xi$ correlation of zero, as the majority of values in the $x$ variable are tied.](anscombes_quartet_correlations.svg)

This implementation is based on the [R implementation](https://statweb.stanford.edu/~souravc/xi.R) linked in the paper.


# Acknowledgements

We acknowledge funding from Chan Zuckerberg Biohub this project.

# References