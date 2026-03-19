suco = float(input("Digite o valor do suco: "))
pratoPrincipal = float(input("Digite o valor do prato principal: "))
sobremesa = float(input("Digite o valor da sobremesa: "))

conta = (suco + pratoPrincipal + sobremesa) + 0.10 * (suco + pratoPrincipal + sobremesa)

print(f"Sua conta é de R${conta:.2f}")