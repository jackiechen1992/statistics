#-*- coding:utf-8 -*-
# 大数定理
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

def law_of_large_numbers():
    x = np.arange(1,1001,1)
    r = bernoulli.rvs(0.3, size = 1000)
    y = []
    rsum = 0.0
    for i in range(1000):
        if r[i] == 1:
            rsum = rsum + 1
        y.append(rsum/(i + 1))
    plt.plot(x, y, color = 'red')
    plt.show()

law_of_large_numbers()