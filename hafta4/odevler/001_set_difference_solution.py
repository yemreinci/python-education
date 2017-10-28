l1 = []

while True:
  x = int(input())
  if x == 0:
    break
  l1.append(x)

s2 = {}

while True:
  x = int(input())
  if x == 0:
    break
  s2[x] = 0

for i in l1:
  if i not in s2:
    print(i)
