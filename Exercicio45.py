a = int(input())
b = int(input())
potencia = a
i = 1 #contador
aux = a


if b == 0:
    potencia = 1
else: 
    while i < b:
        j = 0
        potencia = 0
        while j < aux:
            potencia += a
            j += 1
        a = potencia
        i += 1
print(potencia)