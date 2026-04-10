produtos = [4.95, 9.95, 14.95, 19.95, 24.95]

print("Preço Original | Valor do Desconto | Preço com Desconto")
print("-------------------------------------------------------")

for produto in produtos:
    produtoDesconto = produto * 0.6
    valorDesconto = produto - produtoDesconto
    
    print(f"{produto:14.2f} | {valorDesconto:18.2f} | {produtoDesconto:19.2f}")