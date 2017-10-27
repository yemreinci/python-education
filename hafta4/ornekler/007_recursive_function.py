from matplotlib import pyplot as plt
from math import sqrt

def fibo(n): # fibonaccinin n. elemanini bulur
    if n <= 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

a = [fibo(i) for i in range(10)] # fibonacci sayilari
b = [1.618033 ** i for i in range(10)] # altin oranin usleri
diffs = [(b[i]-a[i])/a[i]*100 for i in range(10)] # aradaki fark (yuzde olarak)

print(a)

# fibonacci ve altin orani karsilastiralim

plt.plot(a)
plt.plot(b)
plt.plot(diffs)

plt.show()
