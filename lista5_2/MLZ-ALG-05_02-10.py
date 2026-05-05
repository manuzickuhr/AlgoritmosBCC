def isPrimo(num: int):
    if num <= 1:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True


def main():
    num = int(input("Digite um número inteiro: "))

    if isPrimo(num):
        print(f"{num} é primo.")
    else:
        print(f"{num} não é primo.")


main()