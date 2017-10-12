# Döngü içinde döngü kullanabiliriz.
# Bu program kullanıcının girdiği sayıdan küçük olan bütün asal sayıları buluyor.
# Bu kodun büyük bölümü 003'ün for içine alınmış hali

n = int(input())
for x in range(2, n):
    divider = 0

    for i in range(2, x):
        if x % i == 0:
            divider = i
            break

    if divider == 0:
        print(x, 'Asal')
