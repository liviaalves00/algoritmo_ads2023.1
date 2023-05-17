'''
Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.
'''
def main():
    #Entrada
    numero = int(input('Digite um número: '))
    limite_inferior  = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    verificar_multiplos = multiplos(numero, limite_inferior , limite_superior + 1)

    print(verificar_multiplos)

def multiplos(numero, inicial, final):
    for i in range(inicial, final):
        if i % numero == 0:
            return i


main()