eleitores = int(input())
votosbranco = int(input())
votosnulo = int(input())
votosvalido = int(input())

porvotosbranco = (votosbranco * 100) / eleitores
porvotosnulo = (votosnulo * 100) / eleitores
porvotosvalido = (votosvalido * 100) / eleitores

ausentes = eleitores - (votosbranco + votosnulo + votosvalido)
porausentes = (ausentes * 100) / eleitores

print(f"Nulos: {porvotosnulo:.2f}%")
print(f"Brancos: {porvotosbranco:.2f}%")
print(f"Validos: {porvotosvalido:.2f}%")
print(f"Ausentes: {porausentes:.2f}%")
