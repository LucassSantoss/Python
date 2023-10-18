qntd_numeros = int(input())
lista = list(map(int, input().split()))
procurar = int(input())
resultado = 0

for i in range (qntd_numeros):
    if lista[i] == procurar:
        resultado += 1

print(resultado)
