def main():
    numero = int(input('Digite a sequência que você quer: '))
    somador = 0
    for c in range(1, numero + 1):
        somador += 1/numero
        print(f' + {1}/{c}', end = ' ')
    print('=', somador)
main()