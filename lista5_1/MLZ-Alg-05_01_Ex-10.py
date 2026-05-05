def conta_digitos(n: int, d:int):
    if d <= 0 or d>9:
        raise ValueError("O número deve ser maior que zero e menor ou igual a nove.")
    
    return str(n).count(str(d))

def main():
    print(conta_digitos(1334, 3))

main()

