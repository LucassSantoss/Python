qntd_numeros = int(input())
lista_a = list(map(int, input().split()))
lista_b = list(map(int, input().split()))
lista_c = []

for i in range (qntd_numeros):
    lista_c.append(0)
    lista_c[i] = lista_a[i] + lista_b[i]

for elemento in lista_c:
    print(elemento, end=" ")

 