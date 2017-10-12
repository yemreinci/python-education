# Bu program, 'list' veri yapısını nasıl kullanabileceğimizi gösteriyor.

# Köşeli parantez içine birkaç eleman yazarak bir list oluşturabiliriz.
l = [1, 5, 14, 'boun']

# Boş bir listeyi de bu yolla oluşturabiliriz.
bos = []

# Bir list'i print fonksiyonu ile ekrana yazıp, içeriğini görebiliriz.

print(l)
print(bos)
print('-----------')

# Bir list'in içerdiği elemanları for ile gezebiliriz.

for i in l:
  print(i*2)
print('-----------')

# index operatörünü ([]) kullanarak listenin belirli bir elemanına erişebiliriz.

print(l[3]) # Ekrana 'boun' yazar.
print(l[0]) # Ekrana '1' yazar
print('-----------')

# index operatörüne negatif indis de verebiliriz. Bu durumda python saymaya tersten başlar.

print(l[-1]) # Ekrana 'boun' yazar
print(l[-2]) # Ekrana '14' yazar
print('-----------')

