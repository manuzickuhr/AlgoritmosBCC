def limpar_texto(texto):
    texto_limpo = ""

    for caractere in texto.lower():
        if caractere.isalpha():  # mantém apenas letras
            texto_limpo += caractere

    return texto_limpo


def anagramas(frase1, frase2):
    frase1 = limpar_texto(frase1)
    frase2 = limpar_texto(frase2)

    letras1 = {}
    letras2 = {}

    for letra in frase1:
        if letra in letras1:
            letras1[letra] += 1
        else:
            letras1[letra] = 1

    for letra in frase2:
        if letra in letras2:
            letras2[letra] += 1
        else:
            letras2[letra] = 1

    return letras1 == letras2


print(anagramas("William Shakespeare", "I am a weakish speller"))
print(anagramas("amor", "roma"))
print(anagramas("python", "java"))