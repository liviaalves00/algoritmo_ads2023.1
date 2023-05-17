'''
Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025.
'''
import math 
def main():

    numero = int(input('Número (entre 1000 e 9999): '))
    
    dois_ultimos  = numero % 100

    dois_primeiros = math.floor(numero/100)

    if (numero >= 1000 and numero <= 9999):
        if (dois_primeiros+ dois_ultimos)**2 == numero:
            print(f'O número ${numero} obedece a característica.')

        else:
            print(f'Não obedece a característica')
    
    else:
        print('Número inválido, tente novamente entre 1000 e 9999.')

main()