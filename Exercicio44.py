a = int(input())
b = int(input())
i = 1 #contador
aux = a

if a != 0 and b != 0:
    while i < b:
        a += aux
        i += 1
else:
    a = 0
print(a)