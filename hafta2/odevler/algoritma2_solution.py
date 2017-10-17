a = []

while True:
    x = int(input())

    if x == 0:
        break

    a.append(x)

b = []

for x in a:
    if x not in b:
        b.append(x)


for x in b:
    print(x)