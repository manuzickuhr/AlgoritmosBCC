dia = int (input("Digite o número de dias: "))
hora = int (input("Digite o número de horas: "))
minuto = int(input("Digite o número de minutos: "))
segundo = int (input("Digite o número de segundos: "))


#1 dia * 24 horas * 60 minutos * 60 segundos = 86400
tempo = (dia*86400) + (hora * 3600) + (minuto * 60)+ segundo

print(f"O número total de segundos do intervalo de tempo informado é de: {tempo}")