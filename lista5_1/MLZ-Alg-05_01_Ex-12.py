def encaixa(a: int, b: int):
    a = str(a)
    b = str(b)

    la = len(a)
    lb = len(b)

    if lb > la or b != a[la - lb:]:
        return False
    else:
        return True

def main():

    resultado = encaixa(int(input("Digite um número: ")), int(input("Digite um número: ")))
    if resultado:
        print("B encaixa em A")
    else:
        print("B não encaixa em A")

main()