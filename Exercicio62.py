qntd_numeros = int(input())
lista = list(map(int, input(). split()))
lista_inversa = []

i = qntd_numeros - 1
while i >= 0:
    lista_inversa.append(lista[i])
    i -= 1

for elemento in lista_inversa:
    print(elemento, end=' ')

