palavra = input("Digite uma palavra: ")
polidromo = ""

for i in range (len(palavra)-1, -1, -1):
    polidromo += palavra[i]

if polidromo == palavra:
    print(f"A palavra {palavra} é um polidromo")
else:
        print(f"A palavra {palavra} não é um polidromo")

