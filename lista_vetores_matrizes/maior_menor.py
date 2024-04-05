'''
Leia um vetor com N elementos, encontre e escreva o maior e o menor elemento e suas respectivas
posições no vetor.
'''
def main():
    qtd_elementos = int(input('Digite a quantidade de elementos do vetor: '))
    vetor = [int(input('Digite o elemento: ')) for c in range(qtd_elementos)]

    maior, menor = verificar_maior_menor(vetor)

    print(f'Maior valor: {maior}')
    print(f'Menor valor: {menor}')

def verificar_maior_menor(colecao):
    valor_maior = float('-inf')
    valor_menor = float('inf')
    for item in colecao:
        if item > valor_maior:
            valor_maior = item
        if item < valor_menor:
            valor_menor = item
    return valor_maior,valor_menor
main()