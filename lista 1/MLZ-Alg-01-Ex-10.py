import math

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))

soma = a + b
diferenca = a - b
produto = a * b
elevado = a ** b

if b != 0:
    quociente = a // b
    resto = a % b
else:
    quociente = "indefinido (divisão por zero)"
    resto = "indefinido (divisão por zero)"

if a > 0:
    log = math.log10(a)
else:
    log = "indefinido (log de número ≤ 0)"

print(
    f"\n\n"
    f"Valor de a: {a}\n"
    f"Valor de b: {b}\n\n"
    f"Soma de a e b: {soma}\n"
    f"Diferença quando b é subtraído de a: {diferenca}\n"
    f"Produto de a por b: {produto}\n"
    f"Quociente quando a é dividido por b: {quociente}\n"
    f"Resto quando a é dividido por b: {resto}\n"
    f"Logaritmo de a na base 10: {log}\n"
    f"a elevado a b: {elevado}"
)