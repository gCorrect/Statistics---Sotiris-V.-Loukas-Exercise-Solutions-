import scipy.stats

rv = scipy.stats.norm(75, 15)
print("rv", rv)

P = rv.cdf(100) - rv.cdf(50)  
print("(i) P(50<=X<=100= ", P)

P = rv.cdf(250) - rv.cdf(90) # 250 is my estimation for rare event thats tends to P = 0
print("(ii) P(X>=90)= ", P)

P = rv.cdf(60) 
print("(iii) P(X<=60)= ", P)

P = rv.cdf(250) - rv.cdf(85) # 250 is my estimation for rare event thats tends to P = 0
print("(iv) P(X>=85)= ", P)

P = rv.cdf(110) - rv.cdf(30)
print("(i) P(30<=X<=110= ", P)

