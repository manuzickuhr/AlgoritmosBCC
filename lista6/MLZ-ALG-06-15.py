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


formula = input("Digite a expressão: ")

print(tokenizacao(formula))