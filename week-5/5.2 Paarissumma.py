def paarissumma(n):
  if n % 2 != 0:
    n = n - 1
  if n <= 0:
    return 0
  else:
    return n + paarissumma(n - 2)

print(paarissumma(10))
