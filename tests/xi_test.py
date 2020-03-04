import pytest
from pyxi.pyxi import xi, xiPValue


@pytest.fixture
def anscombes_xis(anscombes_quartet):
    
    xis = {
        "xi_1": xi(anscombes_quartet["x_1"], anscombes_quartet["y_1"]),
        "xi_2": xi(anscombes_quartet["x_2"], anscombes_quartet["y_2"]),
        "xi_3": xi(anscombes_quartet["x_3"], anscombes_quartet["y_3"]),
        "xi_4": xi(anscombes_quartet["x_4"], anscombes_quartet["y_4"]),        
    }

    return xis


@pytest.fixture
def anscombes_pvalues(anscombes_xis):

    p_vals = {
        "p_1": xiPValue(anscombes_xis["xi_1"]),
        "p_2": xiPValue(anscombes_xis["xi_2"]),
        "p_3": xiPValue(anscombes_xis["xi_3"]),
        "p_4": xiPValue(anscombes_xis["xi_4"]),        
    }

    return p_vals


def test_xi_correlations(anscombes_xis):
    
    assert anscombes_xis["xi_1"].correlation == 0.2749999999999999
    assert anscombes_xis["xi_2"].correlation == 0.6
    assert anscombes_xis["xi_3"].correlation == 0.725
    assert anscombes_xis["xi_4"].correlation == 0.125
    

def test_p_val_asynptotic(anscombes_pvalues):

    # values taken from R code
    assert anscombes_pvalues["p1"].asymptotic(ties=False, nperm=1000, factor=True) == 0.07841556446646347
    assert anscombes_pvalues["p2"].asymptotic(ties=False, nperm=1000, factor=True) == 0.001004022
    assert anscombes_pvalues["p3"].asymptotic(ties=False, nperm=1000, factor=True) == 9.476043e-05
    assert anscombes_pvalues["p4"].asymptotic(ties=False, nperm=1000, factor=True) == 0.2599336

    
def test_p_val_permutations(anscombes_pvalues):
    
    # values taken from R code    
    assert anscombes_pvalues["p1"].permutation_test(nperm=1000) == 0.048
    assert anscombes_pvalues["p2"].permutation_test(nperm=1000) == 0    
    assert anscombes_pvalues["p3"].permutation_test(nperm=1000) == 0
    assert anscombes_pvalues["p4"].permutation_test(nperm=1000) == 0.378
