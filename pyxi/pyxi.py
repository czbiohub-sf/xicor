import pandas as pd
import numpy as np
import scipy.stats as ss
from collections import namedtuple


class xi:
    
    def __init__(self, x, y):
        self.raw_x = pd.Series(x)
        self.raw_y = pd.Series(y)
    
    @property
    def sample_size(self):
        return len(self.raw_x)
    
    @property 
    def data(self):
        CorrData = namedtuple('CorrData', ['x', 'y'])
        both_not_null = self.raw_x.isnull() & self.raw_y.isnull()
        x = self.raw_x[~both_not_null]
        y = self.raw_y[~both_not_null]  
        return CorrData(x, y)
    
    @property
    def x_ordered_rank(self):
        # PI is the rank vector for x, with ties broken at random
        # Not mine: source (https://stackoverflow.com/a/47430384/1628971)
        return self.data.x.sample(frac=1).rank(method='first').reindex_like(self.data.x)
        
    @property
    def y_rank_max(self):
        # f[i] is number of j s.t. y[j] <= y[i], divided by n.
        return self.data.y.rank(method="max")/self.sample_size
        
    @property
    def g(self):
        # g[i] is number of j s.t. y[j] >= y[i], divided by n.
        return pd.Series(
            [1-i for i in self.data.y]
        ).rank(method="max")/self.sample_size
    
    @property
    def x_ordered(self):
        # order of the x's, ties broken at random.
        return np.argsort(self.x_ordered_rank) 
    
    @property
    def x_rank_max_ordered(self):
        # Rearrange f according to ord.
        return [self.y_rank_max[i] for i in self.x_ordered]  

    @property
    def mean_absolute(self):
        return np.mean(
            np.abs(
                [
                    x-y for x, y
                    in zip(
                        self.x_rank_max_ordered[0:(self.sample_size-1)], 
                        self.x_rank_max_ordered[1:self.sample_size]
                    )
                ]
            )
        )*(self.sample_size-1)/(2*self.sample_size) 
    
    @property
    def inverse_g_mean(self):
        # C = np.mean(self.g*(1-self.g))
        return np.mean(self.g*(1-self.g))
    
    @property
    def correlation(self):
        """xi correlation"""
        return 1 - self.mean_absolute/self.inverse_g_mean

    @classmethod
    def xi(cls, x, y):
        return cls(x, y)

    def pval_asymptotic(self, ties=False, nperm=1000, factor=True):
        # If there are no ties, return xi and theoretical P-value:

        if ties:
            return 1-ss.norm.cdf(
                np.sqrt(
                    self.sample_size
                )*self.correlation/np.sqrt(2/5)
            )

        # If there are ties, and the theoretical method is to be used for calculation P-values:
        # The following steps calculate the theoretical variance in the presence of ties:
        sorted_ordered_x_rank = sorted(self.x_rank_max_ordered)
        
        ind = [i+1 for i in range(self.sample_size)]
        ind2 = [2*self.sample_size - 2*ind[i-1]+1 for i in ind]
        
        a = np.mean(
            [i*j*j for i, j in zip(ind2, sorted_ordered_x_rank)]
        )/self.sample_size
        
        c = np.mean(
            [i*j for i, j in zip(ind2, sorted_ordered_x_rank)]
        )/self.sample_size
        
        cq = np.cumsum(sorted_ordered_x_rank)
        
        m = [
            (i + (self.sample_size - j)*k)/self.sample_size
            for i, j, k in zip(cq, ind, sorted_ordered_x_rank)
        ]
        
        b = np.mean([np.square(i) for i in m])
        v = (a - 2*b + np.square(c))/np.square(self.inverse_g_mean)
        
        return 1-ss.norm.cdf(
            np.sqrt(self.sample_size)*self.correlation/np.sqrt(v)
        )

    # def pval_permutation_test(self, nperm=1000):
    #     # If permutation test is to be used for calculating P-value:
    #     r = np.zeros((nperm,), dtype=float)
    #     for idx,val in enumerate(r):
    #     # x1 = runif(n, 0, 1)
    #         x1 = np.random.uniform(0, 1, self.sample_size)
    #         x1_xi = self.xi(x1, self.data.y).correlation
    #         r[idx] = x1_xi

    #     # Return xi and P-value based on permutation test:
    #     return (np.mean([ri for ri in r if ri > self.correlation]))

