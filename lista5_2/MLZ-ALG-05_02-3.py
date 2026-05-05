def envioLoja(itens:int):
    taxaEnvio = 10.95 + (itens-1)*2.95
    return taxaEnvio

def main():
    itens = int(input("Digite a quantidade de itens: "))
    
    taxaEnvio = envioLoja(itens)
    
    print(f"Total de itens: {itens}")
    print(f"Total do envio: R$ {taxaEnvio:.2f}")

main()