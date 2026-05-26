def caracterUnico(texto:str):
    palavraNova = set()
    for caracter in texto:
        palavraNova.add(caracter)

    return len(palavraNova) == len(texto)

print(caracterUnico("amor"))