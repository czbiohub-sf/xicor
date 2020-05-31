pyxi
================================
![Tests](https://travis-ci.com/czbiohub/pyxi.svg?)

xi correlation method adapted for python

## What is pyxi?

Pyxi is an implementation of the "xi" correlation metric described in Chatterjee, S. (2019, September 22). A new coefficient of correlation. [arxiv.org/abs/1909.10140](https://arxiv.org/abs/1909.10140). It is based off the R code mentioned in the paper: https://statweb.stanford.edu/~souravc/xi.R 


```
from pyxi.pyxi import Xi
xi_obj = Xi([1, 2, 3], [1, 2, 3])
correlation = xi_obj.correlation
pvals = xi_obj.pval_asymptotic(
        ties=False, nperm=1000)

```