# Bu program kullanici '.' girene kadar kullanicidan kelimeler alir.
# Daha sonra kullanici bir kelime daha girdiginde, program bu kelimenin daha once kac defa girildigini ekrana yazar.

"""
ornek girdi:

ali
kartal
ali
veli
veli
ali
yunus
.
ali

ornek cikti
3
"""

d = {} # bos bir dictionary tanimliyoruz

while True:
    x = input()

    if x == '.':
        break

    if x not in d: # daha once x kelimesini girilmemisse onu dictionary e ekliyoruz
        d[x] = 1
    else:
        d[x] += 1 # daha once x kelimesi girilmemisse value sunu 1 artiriyoruz


y = input()

if y in d:
    print(d[y])
else:
    print(0)
