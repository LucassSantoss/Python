qntd_numeros = int(input())
numero = int(input())
numero2 = int(input())
if numero > numero2:
    maior = numero
    menor = numero2
else:
    maior = numero2
    menor = numero

for i in range (qntd_numeros - 2):
    numero3 = int(input())
    if numero3 >= maior:
        menor = maior
        maior = numero3
    elif numero3 < maior and numero3 > menor:
        menor = numero3

print(maior)
print(menor)
        
