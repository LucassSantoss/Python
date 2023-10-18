qntd_numeros = int(input())
lista = list(map(int, input().split()))


i = 0
while i < qntd_numeros - 1:
    aux = lista[i]
    lista[i] = lista[i + 1]
    lista[i + 1] = aux
    i += 2

for elemento in lista:
    print(elemento, end=" ")
