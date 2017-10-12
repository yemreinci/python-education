# toplam degiskeni tanimlanmadan kullanilmis

toplam = 0

for i in range(3):
  x = int(input(str(i) + '. sayiyi girin: '))
  toplam += x

print('Ortalama: ' + str(toplam/3))
