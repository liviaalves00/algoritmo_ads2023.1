'''
Leia um número, calcule e escreva seu fatorial.
'''

def main():
    #Entrada
    numero = int(input('Digite um número: '))
     
    #Processamento
    fatorial = calcular_fatorial(numero)

    #Saída
    print(fatorial)


def calcular_fatorial(numero):
    contador = 1
    for i in range(1, numero + 1):
        contador *= i
    return contador

main()