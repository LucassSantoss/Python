n = int(input())
primo = 0
divisores = 1
somadivisores = 0

while divisores <= (n // 2):
    if n % divisores == 0:
        somadivisores += 1
    divisores += 1

if somadivisores == 1:
    primo = 1
print(primo)