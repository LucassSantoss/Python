dimensao = list(map(int, input().split()))
lista = list(map(int, input().split()))

elemento = 0
for i in range (dimensao[0]):
    soma_linha = 0
    for j in range (dimensao[1]):
        soma_linha += lista[elemento]
        elemento += 1
    print(soma_linha)

