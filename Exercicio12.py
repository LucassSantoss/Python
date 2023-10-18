import math
larguraparede = float(input())
alturaparede = float(input())
valorlata = float(input())
rendimentolata = float(input())

areaparede = larguraparede * alturaparede
quantidadelata = (areaparede / rendimentolata)
resultado = math.ceil(quantidadelata)
valortotal = resultado * valorlata

print(f"{resultado:.0f}")
print(f"{valortotal:.2f}")