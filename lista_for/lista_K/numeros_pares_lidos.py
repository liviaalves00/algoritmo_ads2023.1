'''
Leia LimiteSuperior e LimiteInferior e escreva todos os números pares entre os limites lidos.
'''

def main():
    #Entrada
    limite_inferior  = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    #Procesamento
    verificar_par = par(limite_inferior , limite_superior + 1)

    #Saída
    print(verificar_par)

def par(inicial, final):
    for i in range(inicial, final):
        if i % 2 == 0 and i != 0:
            print(i)
        


main()