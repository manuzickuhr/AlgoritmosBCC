tempo = int(input("Digite o total de segundos do intervalo: "))

dias = tempo // 86400
tempo %= 86400

horas = tempo // 3600
tempo %= 3600

minutos = tempo // 60

segundos = tempo % 60

print(f"{dias:02d}:{horas:02d}:{minutos:02d}:{segundos:02d}")