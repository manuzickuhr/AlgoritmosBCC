def is_integer(texto: str):
    texto = texto.strip()
    
    if not texto:  
        return False

    if texto[0] in ("+", "-"):
        return len(texto) > 1 and texto[1:].isdigit()
    
    return texto.isdigit()

def main():
    entrada = input("Digite algo para verificar se é um inteiro: ")

    if is_integer(entrada):
        print("Sim, isso representa um número inteiro.")
    else:
        print("Não, isso não é um número inteiro.")

main()