'''
Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.
'''
from math import sqrt

def main():
    #Entrada
    lado_a = int(input('Digite o primeiro lado: '))
    lado_b = int(input('Digite o primeiro lado: '))
    lado_c = int(input('Digite o primeiro lado: '))
    
    #Processamento
    verificacao_lados = verificar_lados(lado_a, lado_b, lado_c)

    #Saída 
    print(verificacao_lados)
    
def verificar_lados(lado_a, lado_b, lado_c):
    if (lado_a ** 2) == (lado_b ** 2 + lado_c **2):
        return f'Hipotenusa: {lado_a} Catetos: {lado_b} ; {lado_c}'
    if (lado_b ** 2) == (lado_a ** 2 + lado_c **2):
        return f'Hipotenusa: {lado_b} Catetos: {lado_a} ; {lado_c}'
    if (lado_c ** 2) == (lado_a ** 2 + lado_b **2):
        return f'Hipotenusa: {lado_c} Catetos: {lado_a} ; {lado_b}'
    
main()