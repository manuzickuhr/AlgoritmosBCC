palavras = []

while True:
    palavra = input("Digite uma palavra(enter para sair): ")
    if palavra =="":
        break
    if palavra in palavras:
        continue
    palavras.append(palavra)

for palavra in palavras:
    print(palavra)