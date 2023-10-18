a = 0
media = 0 
maiores = 0
idosos = 0
total = -1

while a >= 0:
    media += a
    if a >= 18:
        maiores += 1
    if a > 75:
        idosos += 1
    a = int(input())
    total += 1

if total >= 0:
    media = media / total
    idosos = (idosos / total) * 100


print(f"{media:.2f}")
print(maiores)
print(f"{idosos:.2f}%")