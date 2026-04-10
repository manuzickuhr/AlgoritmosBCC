fator = 2
num = int(input("Digite um número intero: (maior ou igual a 2) "))

if num<2:
    print("O número deve ser maior ou igual a 2")
    exit()

while fator<=num:
    if num % fator==0:
        print(fator)
        num = num // fator
    else:
        fator+=1