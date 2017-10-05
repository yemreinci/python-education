x = int(input('bir sayi giriniz: '))

if 0 <= x and x < 10:
    print('sayi [0, 10) arasinda')

    if x > 5:
        print('5 ten buyuk')
    else:
        print('5 ten kucuk')

elif x > 20:
    print('sayi 20 den buyuk')

    if x == 100:
        print('100 e esit')

else:
    print(':) :)')