import numpy as np
import scipy.stats as ss

class Xi:
    """
    x and y are the data vectors
    """

    def __init__(self, x, y):

        self.x = np.array(list(x))
        self.y = np.array(list(y))
        x_tiebroken = self.x.copy()
        a,ix,c = np.unique(x_tiebroken,return_counts=True,return_inverse=True)
        f = c[ix] > 1
        x_tiebroken[f] = x_tiebroken[f] + np.random.rand(f.sum())*1e-6
        self.x_ordered = np.argsort(x_tiebroken, kind='quicksort')  
        self.sample_size = len(self.x)

        _,b,c = np.unique(self.y[self.x_ordered],return_counts=True,return_inverse=True)
        self.f = np.cumsum(c)[b]        
        _,b,c = np.unique(-self.y[self.x_ordered],return_counts=True,return_inverse=True)
        self.g = np.cumsum(c)[b]  
        self.numerator = self.sample_size*np.abs(np.diff(self.f)).sum()       
        self.denominator = 2*(self.g*(self.sample_size-self.g)).sum()
        self.correlation = 1 - self.numerator / self.denominator


    @classmethod
    def xi(cls, x, y):
        return cls(x, y)

    def pval_asymptotic(self, ties=False, nperm=1000):
        """
        Returns p values of the correlation

        Args:
            ties: boolean
                If ties is true, the algorithm assumes that the data has ties
                and employs the more elaborated theory for calculating
                the P-value. Otherwise, it uses the simpler theory. There is
                no harm in setting tiles True, even if there are no ties.
            nperm: int
                The number of permutations for the permutation test, if needed.
                default 1000

        Returns:
            p value
        """
        # If there are no ties, return xi and theoretical P-value:

        if not ties:
            return 1 - ss.norm.cdf(
                np.sqrt(self.sample_size) * self.correlation / np.sqrt(2 / 5)
            )

        # If there are ties, and the theoretical method
        # is to be used for calculation P-values:
        # The following steps calculate the theoretical variance
        # in the presence of ties:
        sorted_ordered_x_rank = sorted(self.y[self.x_ordered])

        ind = [i + 1 for i in range(self.sample_size)]
        ind2 = [2 * self.sample_size - 2 * ind[i - 1] + 1 for i in ind]

        a = (
            np.mean([i * j * j for i, j in zip(ind2, sorted_ordered_x_rank)])
            / self.sample_size
        )

        c = (
            np.mean([i * j for i, j in zip(ind2, sorted_ordered_x_rank)])
            / self.sample_size
        )

        cq = np.cumsum(sorted_ordered_x_rank)

        m = [
            (i + (self.sample_size - j) * k) / self.sample_size
            for i, j, k in zip(cq, ind, sorted_ordered_x_rank)
        ]

        b = np.mean([np.square(i) for i in m])
        v = (a - 2 * b + np.square(c)) / np.square(self.denominator)

        return 1 - ss.norm.cdf(
            np.sqrt(self.sample_size) * self.correlation / np.sqrt(v)
        )
