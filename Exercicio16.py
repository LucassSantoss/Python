a = int(input())
b = int(input())
aux = 0

if b > a:
    aux = a
    a = b
    b = aux
print(a)
