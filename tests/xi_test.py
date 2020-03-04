import pytest
from pyxi.pyxi import xi, xiPValue


def test_xi_and_p_val():

    x_1 = [10,  8, 13,  9, 11, 14,  6,  4, 12,  7,  5]
    y_1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
    x_2 = [10,  8, 13,  9, 11, 14,  6,  4, 12,  7,  5]
    y_2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.1,  6.13, 3.1,  9.13, 7.26, 4.74]
    x_3 = [0, 0, 0, 0, 1, 1, 2, 3]
    y_3 = [0, 1, 2, 3, 4, 5, 6, 7]
    x_4 = [8,  8,  8,  8,  8,  8,  8, 19,  8,  8,  8]
    y_4 = [6.58,  5.76,  7.71,  8.84,  8.47,  7.04,  5.25, 12.5 ,  5.56,  7.91,  6.89]

    xi_1 = xi(x_1, y_1)
    xip_1 = xiPValue(xi_1)

    xi_2 = xi(x_2, y_2)
    xip_2 = xiPValue(xi_2)

    xi_3 = xi(x_3, y_3)
    xip_3 = xiPValue(xi_3)

    xi_4 = xi(x_4, y_4)
    xip_4 = xiPValue(xi_4)

    # values from R code
    assert xi_1.correlation == 0.2749999999999999
    assert xip_1.asymptotic(ties=False, nperm=1000, factor=True) == 0.07841556446646347
    assert xip_1.permutation_test(nperm=1000) == 0.048

    assert xi_2.correlation == 0.6
    assert xip_2.asymptotic(ties=False, nperm=1000, factor=True) == 0.001004022
    assert xip_2.permutation_test(nperm=1000) == 0    

    assert xi_3.correlation == 0.725
    assert xip_3.asymptotic(ties=False, nperm=1000, factor=True) == 9.476043e-05
    assert xip_3.permutation_test(nperm=1000) == 0
    
    assert xi_4.correlation == 0.125
    assert xip_4.asymptotic(ties=False, nperm=1000, factor=True) == 0.2599336
    assert xip_4.permutation_test(nperm=1000) == 0.378
