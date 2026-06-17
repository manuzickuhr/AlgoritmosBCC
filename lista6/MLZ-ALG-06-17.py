def tokenizacao(formula: str):

    tokens = []
    caracter = ""

    for f in formula:

        # ignora espaços
        if f == " ":
            continue

        # operadores e parênteses
        if f in "*/^()":

            if caracter != "":
                tokens.append(caracter)
                caracter = ""

            tokens.append(f)

        # + ou -
        elif f in "+-":

            # sinal do número
            if caracter == "" and (
                len(tokens) == 0 or tokens[-1] in "+-*/^("
            ):
                caracter += f

            # operador
            else:
                if caracter != "":
                    tokens.append(caracter)
                    caracter = ""

                tokens.append(f)

        # dígitos
        elif f.isdigit():
            caracter += f

    # adiciona último número
    if caracter != "":
        tokens.append(caracter)

    return tokens


def precedencia(op):
    if op in "+-":
        return 1
    elif op in "*/":
        return 2
    elif op == "^":
        return 3
    return 0


def paraPostFix(infix: list):
    operadores = []
    postfix = []

    for token in infix:
        if token.lstrip("+-").isdigit():
            postfix.append(token)

        elif token in "+-*/^":
            while (len(operadores) > 0 and
                   operadores[-1] != "(" and
                   precedencia(token) < precedencia(operadores[-1])):
                postfix.append(operadores.pop())

            operadores.append(token)

        elif token == "(":
            operadores.append(token)

        elif token == ")":
            while operadores[-1] != "(":
                postfix.append(operadores.pop())

            operadores.pop()

    while len(operadores) > 0:
        postfix.append(operadores.pop())

    return postfix

def avaliaPostFix(postfix: list):
    valores = []

    for token in postfix:
        if token.lstrip("+-").isdigit():
            valores.append(int(token))

        else:
            direita = valores.pop()
            esquerda = valores.pop()

            if token == "+":
                resultado = esquerda + direita
            elif token == "-":
                resultado = esquerda - direita
            elif token == "*":
                resultado = esquerda * direita
            elif token == "/":
                resultado = esquerda / direita
            elif token == "^":
                resultado = esquerda ** direita

            valores.append(resultado)

    return valores[0]

formula = input("Digite a expressão: ")

tokens = tokenizacao(formula)
postfix = paraPostFix(tokens)
resultado = avaliaPostFix(postfix)

print("Tokens:", tokens)
print("Pós-fixada:", postfix)
print("Resultado:", resultado)