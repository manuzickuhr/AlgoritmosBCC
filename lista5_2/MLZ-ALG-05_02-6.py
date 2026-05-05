def centralizar(texto: str, largura: int):
    espacos_totais = largura - len(texto)
    
    if espacos_totais <= 0:
        return texto  # não cabe ou já é maior
    
    espacos_frente = espacos_totais // 2
    
    return " " * espacos_frente + texto

def main():
    texto = input("Digite a string: ")
    largura = int(input("Digite a largura do terminal: "))
    
    resultado = centralizar(texto, largura)
    
    print("'" + resultado + "'")  # aspas só pra visualizar os espaços

main()