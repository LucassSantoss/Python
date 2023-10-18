segundos = int(input("Informe a quantidade de segundos que desejar: "))

dias = segundos // 86400
segundos = segundos % 86400
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

print(f"Nessa quantidade de segundos, temos: {dias:.0f} dias {horas:.0f} horas {minutos:.0f} minutos {segundos:.0f} segundos.")