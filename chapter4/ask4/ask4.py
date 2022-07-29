import scipy.stats

rv = scipy.stats.norm(100, 15)
print("rv", rv)

P = rv.cdf(115) - rv.cdf(85)
print("(i) P(85<=X<=115= ", P)

P = rv.cdf(130) - rv.cdf(115) # 250 is my estimation for rare event thats tends to P = 0
print("(ii) P(115<=X<=130)= ", P)

P = rv.cdf(250) - rv.cdf(125) # 250 is my estimation for rare event thats tends to P = 0
print("(iii) P(X>=85)= ", P)


