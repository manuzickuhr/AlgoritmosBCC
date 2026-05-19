import random

def sorteia_mega_sena():
    bilhete = random.sample(range(1, 60), 6)
    bilhete.sort()
    return bilhete

print(sorteia_mega_sena())