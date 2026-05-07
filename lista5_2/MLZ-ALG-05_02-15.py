def hex2int(num: str) -> int:
    num = num.upper()
    referencia = "0123456789ABCDEF"
    
    if len(num) == 1 and num in referencia:
        return referencia.find(num)
    else:
        return "Erro: Entrada deve ser um único dígito hexadecimal (0-F)."

def int2hex(num: int) -> str:
    referencia = "0123456789ABCDEF"
    
    if 0 <= num <= 15:
        return referencia[num]
    else:
        return "Erro: O valor deve estar entre 0 e 15."

print(f"Hex 'B' -> Decimal: {hex2int('b')}")  # Saída: 11
print(f"Decimal 14 -> Hex: {int2hex(14)}")   # Saída: E