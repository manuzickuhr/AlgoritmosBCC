data = int(input('Digite uma data no formato DDMMAA:'))

dia = data // 10000
mes = (data % 10000) // 100
ano = data % 100

print(f"a data invertida é: {ano:02d}/{mes:02d}/{dia:02d}")