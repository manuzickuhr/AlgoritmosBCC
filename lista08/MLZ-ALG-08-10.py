def decodificar(lista):
    if len(lista) == 0:
        return []

    valor = lista[0]
    quantidade = lista[1]

    return [valor] * quantidade + decodificar(lista[2:])

compactada = ["A", 12, "B", 4, "A", 6, "B", 1]

print("Compactada:")
print(compactada)

print("Descompactada:")
print(decodificar(compactada))