# Girilen sayinin bolenlerini yazdiran program

x = int(input('Bir sayi girin: '))

for i in range(1, x+1):
  if x%i == 0:
    print(str(i) + ', ' + str(x) + '\'i boluyor')
