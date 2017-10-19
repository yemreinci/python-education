# dictionary (key, value) pairlerini sakladigimiz bir veri yapisidir.

d = {
    'kartal': 5,
    'ali': 2,
    2: 'yunus',
    10: 15
}

# d[] listelerdeki index yazdigimiz kisma bir "key" yazarak o key e denk gelen "value" u elde edebiliriz.

print(d['kartal']) # ekrana 5 yazar
print(d[2]) # ekrana yunus yazar

x = 'ali'

print(d[x]) # ekrana 2 yazar

# dictionary e tanimladiktan sonra keylere denk gelen valuelari degistirebilir,
#  silebilir veya yeni (key, value) pairleri ekleyebiliriz

d['kartal'] = 7
print(d['kartal']) # ekrana 7 yazar

del d['kartal'] # ('kartal', 7) pairini siler

d['veli'] = 3 # (veli, 3) pairini dictionary e ekler

print(d['veli']) # ekrana 3 yazar

