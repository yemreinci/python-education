# dictionary (key, value) pairlerini (ciftlerini) sakladigimiz bir veri yapisidir.

d = {
    'kartal': 5,
    'ali': 2,
    2: 'yunus',
    10: 15
}

# Listelerde i'nci indise l[i] diyerek erişiyorduk.
# dict'lerde de benzer bir syntax var.
# d[x] diyerek d dict'inde x key'ine denk gelen (x'e map edilmiş) value'yu elde edebiliriz.
# Dikkat edin, dict'lerde indis kavrami yoktur. Dict icinde saklanan ciftler icin oncelik-sonralik sirasindan bahsetmek mumkun degildir.

print(d['kartal']) # ekrana 5 yazar
print(d[2]) # ekrana yunus yazar

x = 'ali'

print(d[x]) # ekrana 2 yazar

# Bir dicti tanimladiktan sonra keylere denk gelen valuelari degistirebilir,
#  var olan pairleri silebilir veya yeni pairler ekleyebiliriz.

d['kartal'] = 7
print(d['kartal']) # ekrana 7 yazar

del d['kartal'] # ('kartal', 7) pairini siler

d['veli'] = 3 # (veli, 3) pairini dictionary e ekler

print(d['veli']) # ekrana 3 yazar

