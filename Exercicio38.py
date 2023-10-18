quantidadenumeros = int(input())
numero = int(input())
i = 1
maior = numero

while i < quantidadenumeros:
    numero = int(input())
    if numero > maior:
        maior = numero
    i = i + 1 
print(maior)