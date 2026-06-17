def mdc(a, b):
    if b == 0:
        return a

    return mdc(b, a % b)

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print("MDC =", mdc(a, b))