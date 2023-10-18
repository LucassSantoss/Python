num1 = int(input())
num2 = int(input())
resto = 0


while num2 != 0:
    resto = num1 % num2
    num1 = num2 
    num2 = resto
print(num1)


    