qntd_numeros = int(input())
lista = list(map(int, input().split()))
maior = lista[0]
posicao_maior = 0

i = 1
while i < len(lista):
    if lista[i] > maior:
        maior = lista[i]
        posicao_maior = i
    i += 1

print(maior)
print(posicao_maior)