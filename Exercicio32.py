n = int(input())
harmonico = 0
i = 1

while i <= n:
  harmonico = harmonico + (1 / i)
  i = i + 1
print(f"{harmonico:.4f}")
