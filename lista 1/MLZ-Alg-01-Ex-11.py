import math 

latitude = float(input("Digite a latitude do primeiro ponto: "))
longitude = float(input("Digite a longitude do primeiro ponto: "))
latitude1 = float(input("Digite a latitude do segundo ponto: "))
longitude1 = float(input("Digite a longitude do segundo ponto: "))

t1 = math.radians(latitude)
g1 = math.radians(longitude)
t2 = math.radians(latitude1)
g2 = math.radians(longitude1)

distancia = 6371.01 * math.acos(
    math.sin(t1) * math.sin(t2) +
    math.cos(t1) * math.cos(t2) * math.cos(g1 - g2)
)

print(f"A distância entre esses dois pontos é de: {distancia:.2f} km")