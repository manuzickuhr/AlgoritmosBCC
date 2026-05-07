def base_para_decimal(num, base):
    referencia = "0123456789ABCDEF"
    decimal = 0
    num = num.upper()
    num_invertido = num[::-1]
    
    for i in range(len(num_invertido)):
        digito = num_invertido[i]
        valor_digito = referencia.find(digito)
        decimal += valor_digito * (base ** i)
    return decimal

def decimal_para_base(num, base):
    if num == 0: return "0"
    referencia = "0123456789ABCDEF"
    resultado = ""
    while num > 0:
        resto = num % base
        resultado = referencia[resto] + resultado
        num = num // base
    return resultado

def main():
    print("--- Conversor de Bases Numéricas (2 a 16) ---")
    
    num_entrada = input("Digite o número: ").strip()
    base_origem = int(input("Base origem: "))
    base_destino = int(input("Base destino: "))

    if not (2 <= base_origem <= 16 and 2 <= base_destino <= 16):
        print("Erro: As bases devem estar entre 2 e 16.")
        return

    if base_origem == base_destino:
        resultado_final = num_entrada
        
    elif base_origem == 10:
        valor_decimal = int(num_entrada)
        resultado_final = decimal_para_base(valor_decimal, base_destino)
        
    else:
        valor_decimal = base_para_decimal(num_entrada, base_origem)
        
        if base_destino == 10:
            resultado_final = valor_decimal
        else:
            resultado_final = decimal_para_base(valor_decimal, base_destino)

    print(f"\nResultado: ({num_entrada}) na base {base_origem} é ({resultado_final}) na base {base_destino}")

main()