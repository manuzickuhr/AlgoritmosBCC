frase = input("Digite uma frase: ")
novaFrase = ""

for letra in frase:
    if letra.isalnum():  
        novaFrase += letra.lower()

polidromo = ""

for i in range(len(novaFrase)-1, -1, -1):
    polidromo += novaFrase[i]

if polidromo == novaFrase:
    print(f"A frase '{frase}' é um palíndromo")
else:
    print(f"A frase '{frase}' não é um palíndromo")