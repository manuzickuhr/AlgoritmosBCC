def numero_ordinal(n):
    ordinais = [
        "",
        "primeiro",
        "segundo",
        "terceiro",
        "quarto",
        "quinto",
        "sexto",
        "sétimo",
        "oitavo",
        "nono",
        "décimo",
        "décimo primeiro",
        "décimo segundo"
    ]
    
    if 1 <= n <= 12:
        return ordinais[n]
    return ""

def main():
    for i in range(1, 13):
        print(f"{i}. {numero_ordinal(i)}")

main()