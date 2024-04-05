'''
Leia um número (vetor com 8 elementos) na base binária, calcule e escreva este número na base
hexadecimal e na base decimal.
'''
def  main(): #
    qtd_digitos = 8
    vetor_binario = [int(input('> ')) for c in range(qtd_digitos)]


    hexa = binario_para_hexadecimal(vetor_binario)
    #decimal = binario_para_decimal(vetor_binario)

    print(hexa)

def  binario_para_hexadecimal(vetor_binario):
    contador = 0
    for item in len(vetor_binario):
        if contador <= 4:
            contador += vetor_binario[len(vetor_binario) - 1 - item] * 2 ** item
            contador += 1
    return contador

#def binario_para_decimal(vetor_binario):

main()