# stringler karater dizilerini tutmak icin kullanilan yapilardir

str = 'aliveli4950'

# listelerin elemanlarini gezdigimiz gibi stringlerin de karakterlerini forla gezebiliriz

for ch in str:
    print(ch) # str icindeki karakterleri satir satir ekrana yazar

# yine listelerde oldugu gibi stringin herhangi bir indexindeki karakterine [] kullanarak ulasabiliriz

print(str[3]) # ekrana v yazar

# len fonksiyonu stringin uzunlugunu dondurur

print(len(str)) # ekrana 11 yazar

# split fonksiyonu string'i parametre olarak verdigimiz stringe gore parcalara boler.
# Olusan parcalari bir list icinde dondurur.

print('murat mehmet 123'.split(' ')) # ekrana ['murat', 'mehmet', '123'] yazar

# format fonksiyonu stringin icine yazdigimiz {x} seklinde ifadelere sirasi ile parametre olarak aldigi degerleri yerlestirir

print('{0} yasindasiniz. {1} yilinda dogdunuz.'.format(20, 1997)) # ekrana '20 yasindasiniz. 1997 yilinda dogdunuz' yazar

# Bunun yerine soyle de yapabilirdik:

print(20, 'yasindasiniz.',  1997, 'yilinda dogdunuz.')

# Ancak format fonksiyonunu kullanmak kodumuzu daha okunakli hale getirebilir
