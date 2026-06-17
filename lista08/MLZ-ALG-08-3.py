def palindromo(texto):
    texto = ''.join(c.lower() for c in texto if c.isalnum())

    def verificar(s):
        if len(s) <= 1:
            return True

        if s[0] != s[-1]:
            return False

        return verificar(s[1:-1])

    return verificar(texto)

frase = input("Digite uma frase: ")

if palindromo(frase):
    print("É palíndromo")
else:
    print("Não é palíndromo")