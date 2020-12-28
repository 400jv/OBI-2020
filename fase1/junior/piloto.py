a = int(input())
b = int(input())
c = int(input())

if (b - a) < (c - b):
  print(1)
  exit()

if (b - a) > (c - b):
  print(-1)
  exit()

print(0)
exit()
