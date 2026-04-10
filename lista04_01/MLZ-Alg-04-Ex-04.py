import math

perimetro = 0
vertice = None
primeiro = None 

while True:
    entradaX = input("Digite a coordenada x de um ponto (enter para sair): ")
    if entradaX == "":
        break

    entradaX = int(entradaX)
    entradaY = int(input("Digite a coordenada y de um ponto: "))

    if primeiro is None:
        primeiro = (entradaX, entradaY)

    if vertice:
        distancia = math.sqrt((entradaY - vertice[1])**2 + (entradaX - vertice[0])**2)
        perimetro += distancia

    vertice = (entradaX, entradaY)

if vertice and primeiro:
    distancia = math.sqrt((primeiro[1] - vertice[1])**2 + (primeiro[0] - vertice[0])**2)
    perimetro += distancia

print(perimetro)