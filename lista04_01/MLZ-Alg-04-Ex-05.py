valorTotal = 0

while True:
    entrada = input("Digite a idade do visitante: (enter quando o grupo acabar)")

    if entrada=="":
        break
    entrada = int(entrada)
    if entrada <= 2:
        continue
    elif entrada >2 and entrada <=12:
        valorTotal +=14
    elif entrada >=65:
        valorTotal += 18
    else:
        valorTotal+= 23

print(f"O preço das entradas é de: {valorTotal:.2f}")