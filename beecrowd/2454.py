def main():
    #Entrada
    p, r = (input().split())

    #Processamento
    fliper = verificar_flpi(p, r)

    #Saída
    print(fliper)

def verificar_flpi(p, r):
    if p == '0':
        return 'C'
    elif r == '0':
        return 'B'
    else:
        return 'A'

main()