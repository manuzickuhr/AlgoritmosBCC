print("Conversão de Temperaturas")
print(f"Celsius \t Fahrenheit")

for i in range (0, 101, 10):
    c = i
    f = c * (9/5) + 32

    print(f"{c} \t {f}")