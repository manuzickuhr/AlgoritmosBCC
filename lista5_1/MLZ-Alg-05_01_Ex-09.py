def eh_bissexto(ano: int):
    if ano%400==0 or (ano%4==0 and ano%100 !=0):
        return True
    else:
        return False

def main():
    resultado = eh_bissexto(2026)
    if resultado==True:
        print('Ano bissexto. ')
    else:
        print('Não é ano bissexto.')

main()