import random
import numpy as np
import pytest

from xicor.xicor import Xi

'''
From Wikipedia:
Anscombe's quartet comprises four data sets that have nearly
identical simple descriptive statistics, yet have very different distributions
and appear very different when graphed. Each dataset consists of eleven
(x,y) points. They were constructed in 1973 by the
statistician Francis Anscombe to demonstrate both the importance of graphing
data before analyzing it and the effect of outliers and other influential
observations on statistical properties.
'''


@pytest.fixture
def anscombes_xis(anscombes_quartet):
    random.seed(2020)
    np.random.seed(2020)
    xis = {
        "xi_1": Xi(anscombes_quartet["x_1"], anscombes_quartet["y_1"]),
        "xi_2": Xi(anscombes_quartet["x_2"], anscombes_quartet["y_2"]),
        "xi_3": Xi(anscombes_quartet["x_3"], anscombes_quartet["y_3"]),
        "xi_4": Xi(anscombes_quartet["x_4"], anscombes_quartet["y_4"]),
    }

    return xis


def test_xi_correlations(anscombes_xis):
    random.seed(2020)
    np.random.seed(2020)
    assert anscombes_xis["xi_1"].correlation == 0.2749999999999999
    assert anscombes_xis["xi_2"].correlation == 0.6
    assert anscombes_xis["xi_3"].correlation == 0.6190476190476191
    assert anscombes_xis["xi_4"].correlation == 0.1000000000000002


def test_p_val_asymptotic(anscombes_xis):
    random.seed(2020)
    np.random.seed(2020)
    # values taken from R code
    assert anscombes_xis["xi_1"].pval_asymptotic(
        ties=False, nperm=1000) == 0.07841556446646347
    assert anscombes_xis["xi_2"].pval_asymptotic(
        ties=False, nperm=1000) == 0.0010040217037570187
    assert anscombes_xis["xi_3"].pval_asymptotic(
        ties=False, nperm=1000) == 0.04989192742513937
    assert anscombes_xis["xi_4"].pval_asymptotic(
        ties=False, nperm=1000) == 0.2599336349448975
