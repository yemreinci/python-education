a = []

while True:
    x = input()

    if x == '0':
        break

    a.append(x)


for i in range(len(a)):
    for j in range(i+1, len(a)):
        print(a[i], a[j])
