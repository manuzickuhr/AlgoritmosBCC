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
    mes = int(input("Digite o mês (1-12): "))
    ano = int(input("Digite o ano: "))

    dias = diaMes(mes, ano)

    if dias == -1:
        print("Mês inválido")
    else:
        print(f"O mês {mes} do ano {ano} tem {dias} dias.")


main()