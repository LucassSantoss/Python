qntd_numeros = int(input())
i = 2
num1 = int(input())
num2 = int(input())
ordem = 1

while i < qntd_numeros:
    num3 = int(input())
    if num1 <= num2 and num2 <= num3:
        ordem = 1
    elif num1 >= num2 and num2 >= num3:
        ordem = -1
    else:
        ordem = 0
    i += 1
print(ordem)