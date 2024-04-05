#Leia um vetor com N elementos, ordene-o e escreva-o em ordem crescente.

def main():
    qtd_elementos = int(input('Digite a quantidade de elementos do vetor: '))
    vetor = [int(input('Digite o elemento: ')) for c in range(qtd_elementos)]

    # percorrer = lenlen(vetor)
    # vetor_ordenado = vetor.sort(key=percorrer)
    sort()
    print(vetor.sort())


main()