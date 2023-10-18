dimensao = list(map(int, input().split()))
lista = list(map(int, input().split()))

i = 0
elemento = 0
matriz = []
while i < dimensao[0]:
    linha = []
    j = 0
    while j < dimensao[1]:
        linha.append(lista[elemento])
        j += 1
        elemento += 1
    matriz.append(linha)
    i += 1

for coluna in range (dimensao[1]):
    soma = 0
    linha = 0
    for elemento in matriz:
        soma += matriz[linha][coluna]
        linha += 1
    print(soma)