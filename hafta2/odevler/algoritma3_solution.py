a = []

while True:
    x = int(input())

    if x == 0:
        break

    a.append(x)

for i in range(len(a)):
    mn = 0

    for j in range(len(a)):
        if a[j] < a[mn]:
            mn = j

    print(a[mn])

    del a[mn]