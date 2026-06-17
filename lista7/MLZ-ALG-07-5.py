def anagramas(palavra1, palavra2):
    letras1 = {}
    letras2 = {}

    # Conta letras da primeira palavra
    for letra in palavra1:
        if letra in letras1:
            letras1[letra] += 1
        else:
            letras1[letra] = 1

    # Conta letras da segunda palavra
    for letra in palavra2:
        if letra in letras2:
            letras2[letra] += 1
        else:
            letras2[letra] = 1

    return letras1 == letras2


print(anagramas("amor", "roma"))   
print(anagramas("python", "java")) 