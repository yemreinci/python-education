from matplotlib import pyplot as plt

def fibo(n): # fibonaccinin n inci elemanini bulur
    if n <= 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

a = [fibo(i) for i in range(7)] # fibonacci sayilari
b = [1.618033 ** i for i in range(7)] # altin oranin usleri

print(a) # ekrana [1, 1, 2, 3, 5, 8, 13] yazar

# fibonacci ve altin orani karsilastiralim

plt.plot(a)
plt.plot(b)

plt.show()
