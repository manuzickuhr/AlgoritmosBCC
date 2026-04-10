while True: 
    bit = input("Digite 8 bits (enter para sair): ")

    if bit == "":
        break

    if len(bit) != 8 or not all(c in "01" for c in bit):
        print("Erro: digite exatamente 8 bits (0 ou 1)")
        continue

    bitParidade = bit.count("1") % 2

    print(f"Bit de paridade (par): {bitParidade}")