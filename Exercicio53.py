num = int(input())
resposta = "N"
somadivisores = 0
i = 1
numeros = 1

while i <= (num / 2):
    if num % numeros == 0:
        somadivisores += numeros
    if somadivisores == num:
        resposta = "S"
    numeros += 1
    i += 1
print(resposta)