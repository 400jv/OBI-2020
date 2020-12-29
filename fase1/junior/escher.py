n = int(input())
if not (3 <= n <= 1000): exit()

sequencia = input().split(' ')
if not (1 <= len(sequencia) <= n): exit()

for x in range(len(sequencia)):
  sequencia[x] = int(sequencia[x])
  if not (1 <= sequencia[x] <= 1000): exit()

soma = sequencia[0] + sequencia[n -1]

for x in range(1, len(sequencia)):
  if sequencia[x] + sequencia[n - (x+1)] != soma:
    print("N")
    exit()

print("S")
