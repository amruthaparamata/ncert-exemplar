import numpy as np

from scipy.stats import bernoulli
simlen = 10000
p = 10/100

y = 0
for i in range(5):
    x = bernoulli.rvs(p, size=simlen)
    y = y + x

count = 0

for i in range(simlen):
    if (y[i] < 2):
       count = count+1 


print(count/simlen)
