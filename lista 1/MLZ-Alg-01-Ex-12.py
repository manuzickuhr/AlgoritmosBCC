import math

raio = float(input("Digite um raio: "))

area = raio**2 * math.pi
volume = 4/3 *math.pi *raio **3

print(f"Área do círculo: {area:.2f}")
print(f"Volume da esfera: {volume:.2f}")