'''
Leia um número, calcule e escreva seu fatorial.
'''
def main():
    #Entrada
    numero = int(input('Digite um número:'))
    fatorial = 1

    #Processamento
    calculo_fatorial= calcular_fatorial(numero, fatorial)
    

    #Saída
    print(calculo_fatorial)

def calcular_fatorial(numero, fatorial):
    while numero >= 1:
        fatorial = fatorial * numero
        numero -= 1
    return fatorial

main()
   