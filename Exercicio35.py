penultimo = 0
ultimo = 1
soma = 1
n = int(input())
i = 1

while i <= n:
    print(f"{soma}", end=' ')
    soma = penultimo + ultimo
    penultimo = ultimo
    ultimo = soma
    i = i + 1
