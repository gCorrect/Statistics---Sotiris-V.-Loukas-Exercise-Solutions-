import scipy.stats

rv = scipy.stats.norm(75, 15)
print("rv", rv)

P = rv.cdf(100) - rv.cdf(50)
print("(i) P(50<=X<=100= ", P)

P = rv.cdf(250) - rv.cdf(90) # 250 is my estimation for rare event thats tends to P = 0
print("(ii) P(X>=90)= ", P)

P = rv.cdf(60) # 250 is my estimation for rare event thats tends to P = 0
print("(iii) P(X<=60)= ", P)

P = rv.cdf(250) - rv.cdf(85) # 250 is my estimation for rare event thats tends to P = 0
print("(iv) P(X>=85)= ", P)

P = rv.cdf(110) - rv.cdf(30)
print("(i) P(30<=X<=110= ", P)


# # stackOverFlow Example------------------------------------
# scipy.stats.norm(0, 1)
# # <scipy.stats.distributions.rv_frozen object at 0x928352c>
# scipy.stats.norm(0, 1).pdf(0)
# # 0.3989422804014327
# scipy.stats.norm(0, 1).cdf(0)
# # 0.5
# scipy.stats.norm(100, 12)
# # <scipy.stats.distributions.rv_frozen object at 0x928352c>
# scipy.stats.norm(100, 12).pdf(98)
# # 0.032786643008494994
# scipy.stats.norm(100, 12).cdf(98)
# # 0.43381616738909634
# scipy.stats.norm(100, 12).cdf(100)
# # 0.5