n = int(input()) #numero a ser digitado
i = 1 #contador
somaprimos = 0 #soma dos numeros primos

while i <= n:
    divisor = 1
    j = 0

    while divisor <= i // 2:
        if i % divisor == 0:
            j += 1
        divisor += 1

    if j == 1:
        somaprimos += i
    
    i += 1

print(somaprimos)