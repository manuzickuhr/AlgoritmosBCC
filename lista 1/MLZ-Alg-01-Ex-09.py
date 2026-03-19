deposito = float(input("Digite o valor depositado na conta: "))
i = 0.12

montante1 = deposito * (1 + i)**1
montante2 = deposito * (1 + i)**2
montante3 = deposito * (1 + i)**3

print(
    f"{'Tempo:':<10}{'Saldo:':>15}\n"
    f"{'1 ano':<10}R$ {montante1:>10.2f}\n"
    f"{'2 anos':<10}R$ {montante2:>10.2f}\n"
    f"{'3 anos':<10}R$ {montante3:>10.2f}"
)