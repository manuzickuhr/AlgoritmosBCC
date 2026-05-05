def encaixa(a: int, b: int):
    a = str(a)
    b = str(b)

    la = len(a)
    lb = len(b)

    if lb > la or b != a[la - lb:]:
        return False
    else:
        return True

def menor_segmento_de_maior(menor: int, maior: int):
    s_menor = str(menor)
    s_maior = str(maior)
    lb = len(s_menor)
    for i in range(len(s_maior) - lb + 1):
        janela = int(s_maior[i:i + lb])
        if encaixa(janela, menor):
            return True
    return False

def main():
    a = int(input("Digite a:"))
    b = int(input("Digite b:"))

    if a == b:
        print("é segmento")
        return

    if a < b:
        menor, maior = a, b
    else:
        menor, maior = b, a

    if menor_segmento_de_maior(menor, maior):
        print("É segmento")
    else:
        print("Não é segmento")

main()