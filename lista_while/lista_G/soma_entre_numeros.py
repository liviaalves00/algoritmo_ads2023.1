'''
Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.
'''
def main():
    numero = int(input('Digite um número: '))

    somatorio = 0

    while numero >= 1:
        somatorio += numero
        numero -= 1

    print(f'Soma entre os números: {somatorio}')

main()