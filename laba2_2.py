import math
import matplotlib.pyplot as plt
import numpy as np


def xfrange(start, stop, step):
    i = 0
    res = []
    while start + i * step < stop:
        res.append(start + i * step)
        i += 1
    return res

def lagrange(x, f, r):
    res = 0
    n = len(x)
    for j in range(0, n):
        tmp = 1
        for i in range(0, n):
            if(i != j):
                tmp *= (r - x[i])/(x[j]-x[i])
                # print "tmp = ", tmp
        res += tmp * f[j]
    return res


x = [-9, 0, 10, 20, 30, 40, 50, 60]

y = np.sin(x)

data_for_func = np.linspace(-10,60,1000)
func = np.sin(data_for_func)

data_for_lag = np.linspace(-10,60,100)
lag_data = [lagrange(x, y, r) for r in data_for_lag]

plt.plot(data_for_lag,lag_data, 'g-', x,y, 'ro', data_for_func, func, 'b-')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()