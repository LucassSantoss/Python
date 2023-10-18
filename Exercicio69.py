string = input()
caracter = input()
qntd_vezes_caracter = 0

for i in string:
    if i == caracter:
        qntd_vezes_caracter += 1

print(qntd_vezes_caracter)
