import math
a = float(input())
b = float(input())
c = float(input())

delta = b**2 - (4 * a * c)

x1 = (-b + delta**(1/2)) / (2 * a)
x2 = (-b - delta**(1/2)) / (2 * a)

somaraizes = x1 + x2

if delta >= 0:
    print(f"{somaraizes:.2f}")
else:
    print(math.nan)

