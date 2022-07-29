import numpy as np
import pandas as pd
import perfplot
from scipy.stats import itemfreq


a = [3,4,3,2,3,3,2,2,1,4,
          3,4,5,5,4,1,3,1,2,5,6]

def bincount(a):
    y = np.bincount(a)
    ii = np.nonzero(y)[0]
    return np.vstack((ii, y[ii])).T


def unique(a):
    unique, counts = np.unique(a, return_counts=True)
    return np.asarray((unique, counts)).T


def unique_count(a):
    unique, inverse = np.unique(a, return_inverse=True)
    count = np.zeros(len(unique), dtype=int)
    np.add.at(count, inverse, 1)
    return np.vstack((unique, count)).T


def pandas_value_counts(a):
    out = pd.value_counts(pd.Series(a))
    out.sort_index(inplace=True)
    out = np.stack([out.keys().values, out.values]).T
    return out


b = perfplot.bench(
    setup=lambda n: np.random.randint(0, 1000, n),
    kernels=[bincount, unique, itemfreq, unique_count, pandas_value_counts],
    n_range=[2 ** k for k in range(26)],
    xlabel="len(a)",
)
b.save("out.png")
b.show(equality_check=array_sorteq)