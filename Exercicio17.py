velocidadelimite = int(input())
multa = float(input())
adicionalmulta = float(input())
velocidaderadar = int(input())
multafinal = 0

if velocidaderadar > velocidadelimite:
    multafinal = multa + ((velocidaderadar - velocidadelimite) * adicionalmulta)
print(f"{multafinal:.2f}")