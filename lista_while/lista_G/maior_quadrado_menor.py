'''
Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o
maior quadrado menor que 38 é 36 (quadrado de 6).
'''
def main():
    #Entrada
    numero = int(input('Digite um número: '))
    
    #Processamento
    verificar_quadrado = maior_quadrado_menor(numero)
    
    #Saída
    print(f'O maior quadrado menor é {verificar_quadrado}')

def maior_quadrado_menor(numero):
    numero_quadrado = 0
    while numero_quadrado ** 2 <= numero:   
        numero_quadrado += 1

    numero_quadrado = numero_quadrado - 1
    quadrado = numero_quadrado ** 2
    return quadrado

main()
