n = int(input("Digite um número inteiro positivo: "))
a = 0

for i in range(1, n+1):
    a += 1/i

print(f"{a:.2f}")