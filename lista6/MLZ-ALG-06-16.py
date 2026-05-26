def paraPostFix(infix:list):
    operadores = []
    postfix = []

    for token in infix:
        if token.lstrip("+-").isdigit():
            postfix.append(token)
        elif token in "*/^()+-":
            