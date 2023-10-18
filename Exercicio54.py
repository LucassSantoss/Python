qntd_numeros = int(input())
if qntd_numeros > 0:
    num = int(input())
    maior = num
    i = 1
    soma = 1
    sequencia = 1
    while i < qntd_numeros:
        num = int(input())
        if num >= maior:
            sequencia += 1
        else:
            sequencia = 1
        if sequencia > soma:
            soma = sequencia
        maior = num
        i += 1
else:
    soma = 0
print(soma)

