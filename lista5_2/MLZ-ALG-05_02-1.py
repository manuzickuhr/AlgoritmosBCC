import math

def hipotenusa(lado1, lado2):
    return math.sqrt(lado1**2 + lado2**2)

def main():
    lado1 = float(input("Digite o primeiro lado menor: "))
    lado2 = float(input("Digite o segundo lado menor: "))

    h = hipotenusa(lado1, lado2)

    print(f"Hipotenusa: {h}")

main()