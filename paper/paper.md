# Python implementation of `xicor`

Tie-breaking in correlation computation is a challenging problem. Given two vectors $X$ and $Y$,
Computing correlations in sparse data, where the majority of the values are zero, is challenging as many of the pairwise comparisons result in ties.
$Xi$ is a novel coefficient of correlation introduced by @chatterjee2020new.

Only [`scipy.stats.kendalltau`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kendalltau.html) has multiple options of breaking ties.

This implementation is based on the [R implementation](https://statweb.stanford.edu/~souravc/xi.R) linked in the paper.