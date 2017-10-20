d = {}
record = 0

while True:
  x = int(input())
  if x == 0:
    break
  if x not in d:
    d[x] = 1
  else:
    d[x] += 1
  if record not in d or d[x] > d[record]:
    record = x

print(record)
