mensagem = input("Digite a mensagem: ")
d = int(input("Digite o deslocamento: "))
mensagemCod = ""

for letra in mensagem:
    if letra.isalpha():
        if 'a' <= letra <= 'z':
            codigo = (ord(letra) - ord('a') + d) % 26 + ord('a')
        else:
            codigo = (ord(letra) - ord('A') + d) % 26 + ord('A')

        mensagemCod += chr(codigo)
    else:
        mensagemCod += letra

print(mensagemCod)