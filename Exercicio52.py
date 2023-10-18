num = int(input())
resposta = "N"
numeros = 1
i = 0

if num >= 0:
    while i <= (num / 2):
        if numeros * (numeros + 1) * (numeros + 2) == num:
            resposta = "S"
        numeros += 1
        i += 1
    print(resposta)