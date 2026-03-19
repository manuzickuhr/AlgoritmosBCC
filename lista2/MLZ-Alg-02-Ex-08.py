numero = int(input ('Digite um número inteiro com 3 algarismos: '))

c= numero //100
numero %=100
d = numero // 10
u = numero % 10

u = u*100
d = d*10

nInverso = c + u + d

print(f"O número inverso é: {nInverso}")