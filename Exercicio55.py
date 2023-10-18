num = int(input())
auxnum = num
invertido = 0
resto = 0
resposta = "N"


while num != 0:
    resto = num % 10
    invertido = (invertido * 10) + resto
    num = num // 10
if invertido == auxnum:
    resposta = "S"
print(resposta)
