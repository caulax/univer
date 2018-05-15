import math
import matplotlib.pyplot as plt
import numpy as np

h = 0.3
x = np.arange(-5, 5, h)

avarageX = []
for i,val in enumerate(x):
    if(i < len(x) - 1):
        avarageX.append( x[i] + (math.fabs(x[i] - x[i+1])  ) / 2 )

y = np.sin(x)

resultSpline = []
for i,val in enumerate(avarageX):
    resultSpline.append(y[i+1] + (x[i+1] - val) * ( (y[i] - y[i+1]) / h ))

totalyRes = np.sin(avarageX)

plt.plot(x,y, 'r-', avarageX,resultSpline, 'b-')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
