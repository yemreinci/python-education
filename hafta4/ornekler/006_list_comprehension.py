# List comprehension, Python'un cok esnek ve guclu bir ozelligidir.
# Halihazirda var olan bir dizinin elemanlarini gezer, her eleman uzerinde belirtilen bir kodu calistirir ve sonuclari sirayla iceren yeni bir list olusturur.

a = [i for i in range(5)] # Bu ornekte range fonksiyonu [0, 1, 2, 3, 4] listesini donduruyormus gibi dusunebiliriz
b = [i * i for i in a]

print(a) # ekrana [0, 1, 2, 3, 4] yazar
print(b) # ekrana [0, 1, 4, 9, 16] yazar

# Sadece belirli bir kosulu saglayan elemanlar uzerinde islem yapmayi tercih edebiliriz:

c = [i+1 for i in b if i>=4]
print(c) # ekrana [5, 10, 17] yazar
