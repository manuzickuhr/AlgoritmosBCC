pi = 3
for i in range(1, 16):
    print(f"Aproximação {i}: {pi:.10f}")
    if i %2==0:
        pi-= 4/(2*i * (2*i +1) * (2*i+2))
    else:
         pi+= 4/(2*i * (2*i +1) * (2*i+2))