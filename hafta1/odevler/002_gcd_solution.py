n = int(input())
m = int(input())

gcd = 1  # ebob

for i in range(1, min(n, m)+1):

    if n % i == 0 and m % i == 0:
        gcd = i


print(gcd)