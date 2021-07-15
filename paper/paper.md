# Python implementation of `xicor`

Tie-breaking in correlation computation is a challenging problem. Given two vectors $X$ and $Y$,
Computing correlations in sparse data, where the majority of the values are zero, is challenging as many of the pairwise comparisons result in ties.
$Xi$ is a novel coefficient of correlation introduced by @chatterjee2020new.

This implementation is based on the [R implementation](https://statweb.stanford.edu/~souravc/xi.R) linked in the paper.