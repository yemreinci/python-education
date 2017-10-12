# Bu program girilen ismin tanidik olup olmadigini bulmak icin yazilmis, hatayi bulabilir misiniz?

isim = input('Bir isim girin: ')

if not isim == 'kartal' or isim == 'yunus':
    print('Yabanci')
else:
    print('Tanidik')

