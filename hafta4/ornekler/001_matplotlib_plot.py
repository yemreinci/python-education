from matplotlib import pyplot as plt
from math import sin, exp, cos

x = []
sinx = []
cosx = []

i = 0
while i < 10:
    x.append(i)
    sinx.append(sin(i))
    cosx.append(cos(i))

    i += 0.01

plt.plot(x, sinx)
plt.plot(x, cosx)

plt.show()