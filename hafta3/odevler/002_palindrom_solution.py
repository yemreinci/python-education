l = []

while True:
  x = input()
  if x == '0':
    break
  l.append(x)

res = True

for i in range(len(l)):
  if l[i] != l[len(l)-i-1]:
    res = False
    break

if res:
  print('Evet')
else:
  print('Hayir')

