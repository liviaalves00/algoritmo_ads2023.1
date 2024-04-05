'''
Leia um vetor A com 20 elementos, calcule e escreva o valor de S.
S = (A[1] - A[20])2 + (A[2] - A[19])2 + ... + (A[9] - A[12])2 + (A[10] - A[11])2
'''
def main():
    vetor_a = [int(input(f'Digite o elemento do vetor: ')) for i in range(21)]
    
    somar_s = somatorio(vetor_a)

    print(f'S = {somar_s}')

def somatorio(colecao):
    somar = 0 
    for c in range(len(colecao)):
        somar += (colecao[c] - colecao[21 - 1]) ** 2
    return somar

main()