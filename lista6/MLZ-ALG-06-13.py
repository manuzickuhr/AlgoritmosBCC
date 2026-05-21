def countRange(lista, max, min):
    eleMin = 0
    eleMax = 0

    for e in lista:
        if e >= max:
            eleMax+=1
        elif e < min:
            eleMin+=1

    return eleMax, eleMin

def main():

    lista = [1,2,2,3,4,5,5,5,5,5,6,7]
    print(countRange(lista, 5, 2))

main()