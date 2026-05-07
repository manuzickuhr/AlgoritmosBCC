def dataMagica(dia:int, mes:int, ano:int):
    return (dia * mes) == (ano % 100)

def eh_bissexto(ano: int):
    if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
        return True
    return False


def diaMes(mes, ano):
    meses = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if mes == 2 and eh_bissexto(ano):
        return 29

    return meses.get(mes, -1)

def main():
    contador = 0
    for ano in range(1901, 2001):
        for mes in range(1, 13):
            # Precisamos iterar de 1 até o número de dias do mês
            for dia in range(1, diaMes(mes, ano) + 1):
                if dataMagica(dia, mes, ano):
                    print(f"{dia:02d}/{mes:02d}/{ano} é uma Data Mágica!")
                    contador += 1
    
    print(f"\nTotal de datas mágicas encontradas: {contador}")

main()