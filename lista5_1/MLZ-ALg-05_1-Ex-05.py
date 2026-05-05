def potencia(x:float, y:float):
    resultado = 1
    for i in range(y):
        resultado *= x
    return resultado


def main():
    print(potencia(2,3))

main()