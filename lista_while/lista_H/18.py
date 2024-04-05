def main():
    numero_n = int(input('Digite o número da sequência que você quer: '))
    contador = 0
    somador = 0

    while contador <= numero_n:
        print(f' + {1}/{contador}', end = ' ')
        contador += 1
        somador += 1/numero_n

    print(f'= {1/somador:.2f}')

main()