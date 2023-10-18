n = int(input()) #numero a ser digitado
i = 1 #contador
somadivisores = 0
primo = 0

while i <= n:
    if n % i == 0:
        somadivisores += 1
        i += 1
    else:
        i += 1
if somadivisores == 2:
    primo = 1
print(primo)
