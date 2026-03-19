import math

l = float(input("Digite o tamanho de um lado do polígono regular: "))
n = int(input("Digite o número de lados do polígono regular: "))

area = (n * l**2) / (4* math.tan(math.pi/n))

print(f"A área do polígono é {area:.2f}")