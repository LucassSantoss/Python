segundos = int(input())

dias = segundos // 86400
segundos = segundos % 86400
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

print(f"{dias:.0f} {horas:.0f} {minutos:.0f} {segundos:.0f}")