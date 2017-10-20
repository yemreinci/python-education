l = []

while True:
  x = input()
  if x == '0':
    break
  l.append(x)

sec = int(input())

for _ in range(sec):
  for i in reversed(range(len(l))):
    if l[i] == 'o':
      if i < len(l)-1 and l[i+1] == '.':
          l[i] = '.'
          l[i+1] = 'o'

print(l)
