'''
Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
formadas pelos seus dois primeiros e dois últimos dígitos.
Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
'''
import math 

def main():
    numero = int(input('Digite o número inicial: '))

    dois_ultimos = numero % 100
    dois_primeiros = math.floor(numero/ 100)
    
    if numero > 0:
        if math.sqrt(numero) == dois_primeiros + dois_ultimos:
            print(f'{numero} é um quadrado Perfeito')
        else:
            print(f'{numero} não é um quadrado perfeito ')
   
main()