preco = float(input())
desconto = float(input())
desconto = desconto / 100

precododesconto = preco * desconto

total = preco - precododesconto

print(f"{total:.2f}")