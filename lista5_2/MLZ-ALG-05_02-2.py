import math

def tarifa(distancia):
    tarifaInicial = 4.00
    tarifaM = 0.25
    bloco = 0.14

    blocos = math.ceil(distancia / bloco) #arredonda para cima por que se começar um novo 140 metros o táxi já cobra inteiro

    tarifaFinal = tarifaInicial + blocos * tarifaM
    return tarifaFinal

def main():
    distancia = float(input("Digite a distância percorrida em km: "))
    
    valor = tarifa(distancia)
    
    print(f"Distância: {distancia} km")
    print(f"Valor da corrida: R$ {valor:.2f}")

main()