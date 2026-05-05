import random

def sorteia_dado():
    return random.randint(1, 6)

def lanca_dado():
    n1 = n2 = n3 = n4 = n5 = n6 = 0

    for i in range(1000000):
        resultado = sorteia_dado()

        if resultado == 1:
            n1 += 1
        elif resultado == 2:
            n2 += 1
        elif resultado == 3:
            n3 += 1
        elif resultado == 4:
            n4 += 1
        elif resultado == 5:
            n5 += 1
        else:
            n6 += 1

    return n1, n2, n3, n4, n5, n6

def main():
    total = 1000000
    n1, n2, n3, n4, n5, n6 = lanca_dado()

    print("Resultados:")
    print(f"1: {n1} ({n1/total*100:.2f}%)")
    print(f"2: {n2} ({n2/total*100:.2f}%)")
    print(f"3: {n3} ({n3/total*100:.2f}%)")
    print(f"4: {n4} ({n4/total*100:.2f}%)")
    print(f"5: {n5} ({n5/total*100:.2f}%)")
    print(f"6: {n6} ({n6/total*100:.2f}%)")

main()