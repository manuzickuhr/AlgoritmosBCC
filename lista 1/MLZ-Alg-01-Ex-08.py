b = int(input("Quantas bugigangas você deseja? "))
q = int(input("Quantas quinquilharias você deseja? "))

pesoPedido = (b * 0.075) + (q*  0.112)

print(f"Seu pedido pesa {pesoPedido:.3f} kg")