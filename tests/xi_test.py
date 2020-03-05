import pytest
from pyxi.pyxi import xi

'''
From Wikipedia:
Anscombe's quartet comprises four data sets that have nearly identical simple descriptive statistics, yet have very different distributions and appear very different when graphed. Each dataset consists of eleven (x,y) points. They were constructed in 1973 by the statistician Francis Anscombe to demonstrate both the importance of graphing data before analyzing it and the effect of outliers and other influential observations on statistical properties. 
'''


@pytest.fixture
def anscombes_xis(anscombes_quartet):
    
    xis = {
        "xi_1": xi(anscombes_quartet["x_1"], anscombes_quartet["y_1"]),
        "xi_2": xi(anscombes_quartet["x_2"], anscombes_quartet["y_2"]),
        "xi_3": xi(anscombes_quartet["x_3"], anscombes_quartet["y_3"]),
        "xi_4": xi(anscombes_quartet["x_4"], anscombes_quartet["y_4"]),        
    }

    return xis


def test_xi_correlations(anscombes_xis):
    
    assert anscombes_xis["xi_1"].correlation == 0.2749999999999999
    assert anscombes_xis["xi_2"].correlation == 0.6
    assert anscombes_xis["xi_3"].correlation == 0.4761905
    assert anscombes_xis["xi_4"].correlation == 0.125
    

def test_p_val_asynptotic(anscombes_xis):

    # values taken from R code
    assert anscombes_xis["xi_1"].pval_asymptotic(ties=False, nperm=1000, factor=True) == 0.07841556446646347
    assert anscombes_xis["xi_2"].pval_asymptotic(ties=False, nperm=1000, factor=True) == 0.001004022
    assert anscombes_xis["xi_3"].pval_asymptotic(ties=False, nperm=1000, factor=True) == 0.01982494
    assert anscombes_xis["xi_4"].pval_asymptotic(ties=False, nperm=1000, factor=True) == 0.2599336

    
def test_p_val_permutations(anscombes_xis):
    
    # values taken from R code    
    assert anscombes_xis["xi_1"].pval_permutation_test(nperm=1000) == 0.048
    assert anscombes_xis["xi_2"].pval_permutation_test(nperm=1000) == 0    
    assert anscombes_xis["xi_3"].pval_permutation_test(nperm=1000) == 0.001
    assert anscombes_xis["xi_4"].pval_permutation_test(nperm=1000) == 0.378
