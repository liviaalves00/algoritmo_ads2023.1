'''
Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.
'''
def main():
    #Entrada
    numero = int(input('DIGITE UM NÚMERO: '))
    somatorio = 0

    #Processamento
    for i in range(1, numero + 1):
        somatorio += i
    print(somatorio) #Saída

main()