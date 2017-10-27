# stringler karater dizilerini tutmak icin kullanilan yapilardir

str = 'aliveli4950'

# listelerin elemanlarini gezdigimiz gibi stringlerrin de karaterlerini forla gezebiliriz

for ch in str:
    print(ch) # ekranan tek tek karakterleri yazar

# yine listelerde oldugu gibi stringin herangi bir indexindeki karakterine [] kullanarak ulasabiliriz

print(str[3]) # ekrana v yazar

# len fonksiyonu stringin uzunlugunu dondurur

print(len(str)) # ekrana 11 yazar

# split fonksiyonu string i verdiginiz ozel bir splitter stringinden parcalari bolup bir list olarak dondurur

print('murat mehmet 123'.split(' ')) # ekrana ['murat', 'mehmet', '123'] yazar

# format fonksiyonu stringin icine yazdigimiz {x} seklinde ifadelere sirasi ile parametre olarak aldigi degerleri yerlestirir

print('{0} yasindasiniz. {1} yilinda dogdunuz.'.format(20, 1997)) # ekrana 20 yasindasiniz. 1997 yilinda dogdunuz yazar

