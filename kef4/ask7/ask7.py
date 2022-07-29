import scipy.stats

rv = scipy.stats.norm(85, 15)
print("rv", rv)

P = rv.cdf(250) - rv.cdf(100) # 250 is my estimation for rare event thats tends to P = 0
print("(i) P(X>=100)= ", P)

P = rv.cdf(115) - rv.cdf(70)
print("(ii) P(70<=X<=115= ", P)
