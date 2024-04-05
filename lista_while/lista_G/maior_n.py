'''
Leia N e uma lista de N números e escreva o maior número da lista.
'''
def main():
    # Entrada
    numero = int(input('Digite um número:  '))
    lista_numeros = []

    index_lista = 0
    while index_lista < numero:
        numero = int(input(f'Digite o número: '))
        lista_numeros.append(numero)
        index_lista += 1

    # Processamento
    maior_numero = encontrar_maior_numero(lista_numeros)

    # Saída
    print(f'O maior número da lista é: {maior_numero}')

def encontrar_maior_numero(lista):
    maior = lista[0] 
    i = 1

    while i < len(lista):
        if lista[i] > maior:
            maior = lista[i]
        i += 1

    return maior

main()