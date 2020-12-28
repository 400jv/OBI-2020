a = int(input())
b = int(input())
c = int(input())

viagens = 1

if (a + b) < c:
  print(viagens)
  exit()

if a == b and b < c:
  print(viagens +1)
  exit()

if (c == a):
  viagens += 1

if (c == b):
  viagens += 1

print(viagens)
