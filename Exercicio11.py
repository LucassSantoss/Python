salariofixo = float(input())
dinheirodasvendas = float(input())

comissao = 0.18 * dinheirodasvendas

total = salariofixo + comissao

print(f"{total:.2f}")
