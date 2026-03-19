n = int(input("Digite um número inteiro de 4 dígitos: "))
#d1 digito 1 
d1 = n // 1000 #pega o número do milhar 
n %= 1000

d2 = n // 100 #pega o número da centena
n %= 100

d3 = n // 10 #pega o número da dezena

d4 = n % 10 #pega o número da unidade

soma = d1 + d2 + d3 + d4
print(soma)

