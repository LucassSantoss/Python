qntd_numeros = int(input())
lista = list(map(int, input().split()))
numeros = list(map(int, input().split()))
soma = 0

if numeros[0] <= (qntd_numeros - 1) and numeros[1] <= (qntd_numeros - 1) and numeros[0] >= 0 and numeros[1] >= 0:
    if numeros[0] > numeros[1]:
        maior = numeros[0]
        menor = numeros[1]
    else:
        maior = numeros[1]
        menor = numeros[0]
    while menor <= maior:
        soma += lista[menor]
        menor += 1
    print(soma)
else:
    print("INVALIDO")