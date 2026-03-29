n = int(input("Digite um número inteiro positivo: "))

k = 1
a = 0.0

while k <= n:
    if k % 2 == 0:
        a -= 1 / k   
    else:
        a += 1 / k  
    
    k += 1

print(f"{a:.2f}")