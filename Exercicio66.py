qntd_numeros = int(input())
lista = list(map(int, input().split()))
lista_par = []
lista_impar = []

for i in range (qntd_numeros):
    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    elif lista[i] % 2 != 0:
        lista_impar.append(lista[i])

for i in lista_par:
    print(i, end=" ")
print()

for i in lista_impar:
    print(i, end=" ")
print()