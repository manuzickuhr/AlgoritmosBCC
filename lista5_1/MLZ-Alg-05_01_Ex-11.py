def conta_digitos(n: int, d:int):
    if d <= 0 or d>9:
        raise ValueError("O número deve ser maior que zero e menor ou igual a nove.")
    
    return str(n).count(str(d))

def permutacao(a: int, b: int):
    if len(str(a)) != len(str(b)):
        return False
    
    for d in range(1, 10):
        if conta_digitos(a, d) != conta_digitos(b, d):
            return False
        return True
        
def main():
    resultado = permutacao(5412434, 4321445)
    if resultado:
        print("A é permutação de B")
    else:
        print("A não é permutação de B")
    

main()