from random import randrange # random package indan randrange fonksiyonunu programiza import ediyoruz

a = []

for i in range(1000000):
    a.append(randrange(10 ** 9)) # listenin icini rasgele sayilarla dolduruyoruz


print('ilk 10 eleman:')
print(a[:10]) # olusan listenin ilk 10 elemanina bakmak icin yazdiralim

print('siralaniyor...')

a.sort()

print('bitti: ')
print(a[:10]) # siralandiktan sonraki ilk 10 elemmani