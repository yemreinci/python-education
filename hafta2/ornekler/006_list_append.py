# Önceki örnekte (005) kod içine gömülü bir list kullandık.
# Bu örnekte programın çalışırken aldığı verileri kullanarak bir list oluşturacağız.
# Kullanıcının girdiği sayıları bir list içine ekleyip, kullanıcı 0 girince o zamana kadar yazdığı sayıları tersten yazdıracağız.

l = []

while True:
  x = int(input())
  if x == 0:
    break
  l.append(x) # Bu komutla 'l' listesinin sonuna x'i ekliyoruz. Listenin eleman sayısı bir artıyor.

print('Girdiginiz sayilar (tersten): ')
for i in reversed(l): # 'reversed' fonksiyonu, kendisine verilen list'i tersine çevirir.
  print(i)
