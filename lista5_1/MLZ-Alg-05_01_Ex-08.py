def digitos(n: int):
    if n <= 0:
        raise ValueError("O número deve ser maior que zero.")
    
    contador = 0
    while n > 0:
        n //= 10
        contador += 1
    
    return contador

def main():
    print(digitos(200))

main()