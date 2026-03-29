n = int(input("Digite um número inteiro positivo: "))
k = 1
a = 0

while k <= (2*n - 1):
    a += 1/k
    k +=2 

print(f"{a:.2f}")