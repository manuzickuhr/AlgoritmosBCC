quant = 0
soma = 0

while True:
    entrada = int(input("Digite um número (ou 0 para sair): "))
    
    if entrada == 0:
        break

    quant+= 1
    soma += entrada

media = soma / quant

if quant > 1:
    palavras = ["dos", "números"]
else:
    palavras = ["do", "número"]

print(f"A média {palavras[0]} {quant} {palavras[1]} é {media}")