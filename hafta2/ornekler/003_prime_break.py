# for ve while döngülerinden çıkmak için 'break' komutunu kullanabiliriz.
# Bu program, girilen sayının asal olup olmadığını test ediyor.
# Kendisinden küçük bir sayıya bölündüğünü tespit ettiğinde, döngüden çıkıyor.

x = int(input())
divider = 0

for i in range(2, x):
  if x % i == 0:
    divider = i
    break

if divider == 0:
  print('Asal')
else:
  print('Asal degil, ', divider, '\'a bolunuyor.')
