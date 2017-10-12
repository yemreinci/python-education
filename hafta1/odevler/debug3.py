# Bu program girilen 3 sayini ortalamasini bulmak icin yazilmis, hatayi bulabilir misiniz?

for i in range(3):
  x = int(input(str(i) + '. sayiyi girin: '))
  toplam += x
print('Ortalama: ' + str(toplam/3))
