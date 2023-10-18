n = int(input()) #dinheiro
c = int(input()) #preço do chocolate
m = int(input()) #quantidade de embalagens para desconto

chocolates = n // c
embalagens = chocolates

while embalagens >= m:
    embalagens -= m
    embalagens += 1
    chocolates += 1
print(chocolates)