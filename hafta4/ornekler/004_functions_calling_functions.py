def sum(a, b): # verilen iki sayiyi toplayan fonksiyon
    return a + b

def sqr(a): # verilen sayinin karesini alan fonksiyon
    return a * a

def sqr_sum(a, b): # verilen iki sayinin toplaminin karesini bulan fonksiyon
    return sqr(sum(a, b))


print(sqr_sum(2, 3)) # ekrana 25 yazar