record = []
current = []


while True:
    x = int(input())

    if x == 0:
        break

    if len(current) == 0 or current[-1] <= x:
        current.append(x)
    else:
        if len(current) > len(record):
            record = current

        current = [x]


if len(current) > len(record):
    record = current


for x in record:
    print(x)