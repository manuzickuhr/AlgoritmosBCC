n = int(input("Digite um número inteiro de 3 dígitos: "))

c = n // 100 #pega o número da centena
n %= 100

d = n // 10 #pega o número da dezena

u = n % 10 #pega o número da unidade

print(f"Centena: {c}\nDezena: {d}\nUnidade: {u}")