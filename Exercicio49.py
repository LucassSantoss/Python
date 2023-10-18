idade = int(input())
qntd_velas = idade
altura = int(input())
maior = altura
i = 1
soma = 1

while i < qntd_velas:
    altura = int(input())
    if altura >= maior:
        if altura > maior:
            maior = altura
            soma = 1
        elif altura == maior:
            soma += 1
    i += 1
print(soma)