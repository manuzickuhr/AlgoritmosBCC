# Litros <=1 
vasilhame1 = int(input("Digite a quantidade de vasilhames de 1L ou menos: "))

# Litros >1
vasilhame2 = int(input("Digite a quantidade de vasilhames com mais de 1L: ")) 

credito = (vasilhame1 * 0.10) + (vasilhame2 * 0.25)

print(f"O total de crédito gerado é de R${credito:.2f}")