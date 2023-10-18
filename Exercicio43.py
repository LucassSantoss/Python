n = int(input()) #numero inteiro
i = 1 #contador
fatorial = 1
somafatorial = 0

while i <= n:
    fatorial = fatorial * i
    i += 1
    somafatorial += fatorial

print(somafatorial + 1)

