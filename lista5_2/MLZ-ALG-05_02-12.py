def isSenhaValida(senha:str):
     tem_maiuscula = any(char.isupper() for char in senha)
     tem_minuscula = any(char.islower() for char in senha)
     tem_numero = any(char.isdigit() for char in senha)
     return len(senha)>=8 and tem_maiuscula and tem_minuscula and tem_numero

def main():
    senha_usuario = input("Digite a senha para validar: ")
    
    if isSenhaValida(senha_usuario):
        print("Senha válida! Segurança aprovada.")
    else:
        print("Senha inválida! A senha deve ter pelo menos 8 caracteres, "
              "incluindo maiúsculas, minúsculas e números.")

main()