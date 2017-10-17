a = []

while True:
    x = int(input())

    if x == 0:
        break

    a.append(x)

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[j] < a[i]:
            t = a[i]
            a[i] = a[j]
            a[j] = t


for x in a:
    print(x)