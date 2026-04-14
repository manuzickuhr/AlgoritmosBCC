x = float(input("Digite um número positivo: "))

if x<0:
    print("O número não pode ser negativo")
    exit()

raiz = x/2
while abs(raiz * raiz - x)  > 10**(-12):
    raiz = (raiz + (x/raiz))/2

print(f"A raiz aproximada é de: {raiz} ")