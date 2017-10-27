import matplotlib.pyplot as plt
from random import gauss

l = []

for i in range(100000):
  l.append(gauss(10, 25))

plt.hist(l, bins=250)
plt.show()
