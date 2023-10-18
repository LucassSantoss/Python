quantidadenumeros = int(input())
numero = int(input())
i = 1
maior = numero
menor = numero
soma = numero

while i < quantidadenumeros:
    numero = int(input())
    if numero > maior:
        maior = numero
        soma = soma + maior
    elif numero < menor:
        menor = numero
        soma = soma + menor
    else:
        soma = soma + numero
    i = i + 1 
print(maior)
print(menor)
print(soma)
