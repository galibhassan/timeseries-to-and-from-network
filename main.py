import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def getSlope(x1, y1, x2, y2):
    slope = (y1-y2)/(x1-x2)
    return slope


def isVisible(a, b, c):
    slope_ab = getSlope(a, b)
    slope_bc = getSlope(b, c)
    if(slope_bc > slope_ab):
        return True
    else:
        return False


x = np.arange(0, 4)
y = np.sin(x)

currentPointX = x[0]
currentPointY = y[0]

for i in range(len(x)-1):
    if i != 0:
        a = x[i], y[i]


print(x)
print(y)
plt.plot(x, y)
plt.scatter(x, y)
plt.show()
