qntd_numeros = int(input())
lista = list(map(int, input().split()))
procurar_numero = int(input())
resultado = -1
achou = False

i = 0
while achou != True and i < qntd_numeros:
    if lista[i] == procurar_numero:
        resultado = i
        achou = True
    i += 1
    
print(resultado)