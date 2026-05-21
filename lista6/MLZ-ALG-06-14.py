def precedencia(operador:str):
    if operador == "+" or operador == "-":
        return 1
    elif operador == "*" or operador=="/":
        return 2
    elif operador=="^":
        return 3
    else:
        return -1
    
def main():
    operador = input("Digite um operador (+, -, *, / ou ^): ")
    result = precedencia(operador)
    if result==(-1):
        print("Operador inválido")
        exit()
    print(f"Precedencia: {result}")

main()