ateXkm = float(input())
valor1 = float(input())
valor2 = float(input())
quilometragem = float(input())
valortotal = 0

if quilometragem <= ateXkm:
    valortotal = valor1 * quilometragem
    print(f"{valortotal:.2f}")
else:
    valortotal = valor2 * quilometragem
    print(f"{valortotal:.2f}")


