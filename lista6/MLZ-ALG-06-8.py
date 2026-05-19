def somente_palavras(texto):
    texto = texto.replace(",", " ")
    texto = texto.replace(";", " ")
    texto = texto.replace("!", " ")
    texto = texto.replace("?", " ")
    texto = texto.replace(".", " ")

    palavras = texto.split()
    return palavras

def main():
    texto = input("Digite uma frase: ")
    texto_novo = somente_palavras(texto)

    print(texto_novo)

main()