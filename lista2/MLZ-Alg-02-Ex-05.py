centavos = int(input("Digite a quantidade de centavos: (de 0 a 99) "))

#moedas de 50, 25, 10, 5 e 1
#troco com a menor quantidade de moedas

m50 = centavos // 50
centavos %= 50

m25 = centavos // 25
centavos %= 25

m10 = centavos // 10
centavos %= 10

m5 = centavos // 5

m1 = centavos % 5

print(f"Troco:\n 50 centavos: {m50}\n 25 centavos: {m25}\n 10 centavos: {m10}\n 5 centavos: {m5}\n 1 centavo: {m1} ")