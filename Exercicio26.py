a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("EQUILATERO")
    elif a == b or b == c or a == c:
        print("ISOSCELES")
    else:
        print("ESCALENO")
else:
    print("INVALIDO")


