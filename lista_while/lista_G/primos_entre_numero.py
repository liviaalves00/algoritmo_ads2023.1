'''
Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.
'''
def main():
    #Entrada
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    #Processamento
    while limite_inferior <= limite_superior:
        contador = 0
        divisao = 1
        novo_numero = limite_inferior

        while divisao <= novo_numero:
            if novo_numero % divisao == 0:
                contador += 1
            divisao += 1

        #Saída
        if contador <= 2 and novo_numero != 0 and novo_numero != 1:
            print(novo_numero)
        limite_inferior += 1

main()