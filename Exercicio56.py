i = 0
media = 0
lista_temperaturas = list(map(int, input().split()))

while i < len(lista_temperaturas):
    media += lista_temperaturas[i]
    i += 1
media = media / len(lista_temperaturas)

acima_media = 0
i = 0
while i < 7:
    if lista_temperaturas[i] > media:
        acima_media += 1
    i += 1
print(f"{acima_media}")