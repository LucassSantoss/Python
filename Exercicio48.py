p1 = int(input())
d1 = int(input())
p2 = int(input())
d2 = int(input())
resposta = "NAO"

if (d1 > d2 and p2 > p1) or (d2 > d1 and p1 > p2):
    formulatempo = (p1 - p2) / (d2 - d1)
    if formulatempo >= 0 and formulatempo % 1 == 0:
        resposta = "SIM"
print(resposta)