def corrigir_maiusculas(texto: str):
    resultado = ""
    proxima_deve_ser_maiuscula = True 

    for char in texto:
        if char != " " and proxima_deve_ser_maiuscula:
            resultado += char.upper()
            proxima_deve_ser_maiuscula = False
        else:
            resultado += char

        if char in ".!?":
            proxima_deve_ser_maiuscula = True

    return resultado

def main():
    entrada = input("Digite o texto: ")
    texto_corrigido = corrigir_maiusculas(entrada)
    print("Resultado:", texto_corrigido)

main()