'''
Escreva a tabuada dos números de 1 a 10.
'''
def main():
    #Entrada
    numero_inicial = 1
    contador = 0

    #Processamento/saída
    while numero_inicial <= 10:
        resultado_multiplicacao =  contador * numero_inicial
        print(f'{contador} x {numero_inicial} = {resultado_multiplicacao}')
        contador += 1
        
        if contador == 10:
            print()
            contador = 0
            numero_inicial += 1  
        
main()