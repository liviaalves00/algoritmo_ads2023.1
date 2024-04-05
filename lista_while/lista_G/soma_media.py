'''
Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.
'''
def main():
    # Entrada
    numero = int(input('Digite um número: '))
    lista_numeros = []

    # Processamento
    calcular_soma_media(numero, lista_numeros)

def calcular_soma_media(numero, lista_numeros):
    soma = 0
    while len(lista_numeros) < numero:
        novo_numero = int(input('Digite um número: '))
        lista_numeros.append(novo_numero)
        soma += novo_numero

    print(f'Soma: {soma}')
    print(f'Média: {soma / numero:.2f}') # Saída

main()
