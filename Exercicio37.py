x = int(input())
primeiro = x
contador = 0

while x >= 0:
    x = int(input())
    if x == primeiro:
        contador = contador + 1
print(contador)


