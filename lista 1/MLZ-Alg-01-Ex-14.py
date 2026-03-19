import math

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

l = (lado1 + lado2 + lado3)/2

area = math.sqrt(l*(l - lado1) * (l - lado2) * (l - lado3))

print(f"A área do triângulo é {area:.2f}")