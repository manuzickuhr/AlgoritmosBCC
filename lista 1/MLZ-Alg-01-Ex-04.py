largura = float(input("Digite a largura do terreno em metros: "))
profundidade = float(input("Digite a profundidade do terreno em metros: "))

area = largura * profundidade

hectares = area / 10000

palavraHectare = ""

if hectares == 1:
    palavraHectare = "hectare"
else:
    palavraHectare = "hectares"

print(f"O terreno tem {hectares:.2f} {palavraHectare}.")