import random

def gerarSenha():
    comprimento = random.randint(7, 10)
    senha = ""
    
    for i in range(comprimento):
        caracter = random.randint(33, 126)
        senha += chr(caracter)
    
    return senha


def main():
    senha_gerada = gerarSenha()
    print("Senha gerada:", senha_gerada)


main()