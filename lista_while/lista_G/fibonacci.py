'''
Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
(0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.
'''
def main():
    #Entrada
    numero = int(input('Digite um número para a seuqencia: '))

    #verificacao de erro
    while numero < 2:
        print('Número inválido!!!')
        numero = int(input('Digite um número para a sequencia: '))

    #Processamento
    fibonacci = verificar_sequencia(numero)

    #Saída
    print(fibonacci)

def  verificar_sequencia(numero):
    termo1 = 0
    termo2 = 1
    print(f'{termo1} - {termo2} - ', end=' ')

    while numero >= 0:
        termo3 = termo1 + termo2
        print(termo3, end = '-')
        termo1 = termo2
        termo2 = termo3
        numero -= 1
    return numero

main()