base = int(input())
expoente = int(input())
resultado = 1
i = 1

if expoente != 0:
  while i <= expoente:
    resultado = resultado * base
    i = i + 1
else:
  resultado = 1
print(resultado)

  