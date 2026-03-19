matricula = int(input("Digite o número da matricula no formato AASDDD: "))
ano = matricula //10000
semestre = (matricula % 10000)//1000

print(f"O ano da matricula é {ano} e o semestre é: {semestre}")