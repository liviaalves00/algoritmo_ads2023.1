'''
Leia N e escreva todos os números inteiros de 1 a N.
'''

def main():
    #Entrada
    numero = int(input('Digite um número: '))
    contador = 0
    
    #Processamento/Saída
    while contador != numero:
        contador += 1
        print(contador)


main()