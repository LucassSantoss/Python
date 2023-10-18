dimensao = list(map(int, input().split()))
lista = list(map(int, input().split()))

elemento = 0
for linha in range (dimensao[0]):
    for coluna in range (dimensao[1]):
        print(lista[elemento], end=' ')
        elemento += 1
    print()