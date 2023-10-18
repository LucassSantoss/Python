num = int(input())
somaprimos = 0
i = 0

while i <= num:
    primo = 0
    divisor = 1
    while divisor <= (i // 2):
        if i % divisor == 0:
            primo += 1
        divisor += 1
    if primo == 1:
        somaprimos += i
    i += 1
print(somaprimos)
