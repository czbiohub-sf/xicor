pyxi
================================
![Tests](https://travis-ci.com/czbiohub/pyxi.svg?)
[![codecov](https://codecov.io/gh/czbiohub/pyxi/branch/master/graph/badge.svg)](https://codecov.io/gh/czbiohub/pyxi)

xi correlation method adapted for python

## What is pyxi?

Pyxi is an implementation of the "xi" correlation metric described in Chatterjee, S. (2019, September 22). A new coefficient of correlation. [arxiv.org/abs/1909.10140](https://arxiv.org/abs/1909.10140). It is based off the R code mentioned in the paper: https://statweb.stanford.edu/~souravc/xi.R 

-   Free software: MIT license
-   Documentation: https://czbiohub.github.io/pyxi

Installation
------------

The package can be installed from PyPI using `pip` here:

```
pip install pyxi
```

### Developmental install

To install this code and play around with the code locally, clone this github repository and use `pip` to install:

```
git clone https://github.com/czbiohub/pyxi.git
cd pyxi

# The "." means "install *this*, the folder where I am now"
pip install .
# or you could install using
python setup.py install
```

Usage
-----

```
from pyxi.pyxi import Xi
xi_obj = Xi([1, 2, 3], [1, 2, 3])
correlation = xi_obj.correlation
pvals = xi_obj.pval_asymptotic(ties=False, nperm=1000)

```
