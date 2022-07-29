# just an example of the t declaration from the scipy site
from scipy.stats import t
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)

df = 2.74
mean, var, skew, kurt = t.stats(df, moments='mvsk')

x = np.linspace(t.ppf(0.01, df),
                t.ppf(0.99, df), 100)
ax.plot(x, t.pdf(x, df),
       'r-', lw=5, alpha=0.6, label='t pdf')
rv = t(df)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

vals = t.ppf([0.001, 0.5, 0.999], df)
np.allclose([0.001, 0.5, 0.999], t.cdf(vals, df))

r = t.rvs(df, size=1000)

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
# -------------------------
z = scipy.stats.norm.ppf(0.95)
t1 = t.ppf(q=0.05,df= 15)

print("z", z)
print("t", t)

plt.show()
