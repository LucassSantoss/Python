base = int(input())
expoente = int(input())
potencia = base
i = 1
auxbase = base

if expoente == 0:
    potencia = 1
else:
    while i < expoente:
        j = 0
        potencia = 0
        while j < auxbase:
            potencia += base
            j += 1
        base = potencia
        i += 1
print(potencia)