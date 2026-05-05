def trianguloValido(a: int, b: int, c: int):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    return True

def trianguloValido(a: int, b: int, c: int):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    return True


def main():
    a = int(input("Digite o lado A: "))
    b = int(input("Digite o lado B: "))
    c = int(input("Digite o lado C: "))

    if trianguloValido(a, b, c):
        print("Os lados podem formar um triângulo.")
    else:
        print("Os lados não podem formar um triângulo.")


main()