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

# index operatorune bir aralik da verebilirsiniz. Bu durumda verdiginiz araliktaki tum elemanlari
#  baska bir liste seklinde elde edersiniz
# bir baska ifadeyle liste yi 'slice' etmis olursunuz

print(l[0: 2]) # Ekrana [1, 5] yazar
print(l[1: 4]) # Ekrana [5, 14, 'boun'] yazar
print(l[2: ]) # araligin 2. paramtresini vermezseniz otomatik olarak listenin sonuna kadar olan elemanlari alir
print(l[: 3]) # aralin ilk parametresini vermezseniz orada 0 yaziyormus gibi kabul eder
print('-----------')

# len fonksiyonunu kullanarak bir listenin içindeki eleman sayısını elde edebilirsiniz.

print(len(l)) # Ekrana '4' yazar

# + operatörü, stringlerde olduğu gibi listeleri de yan yana ekler

print(l + ['aa', 4.5]) # Ekrana [1, 5, 14, 'boun', 'aa', 4.5] yazar


