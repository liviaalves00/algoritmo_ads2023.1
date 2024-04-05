def main():
    #Entrada
    n = int(input())

    #Processamento
    lista_freq = []

    #Saída
    verificar_frequencia = verificar_freq(n, lista_freq)

    print(verificar_frequencia)

def verificar_freq(n, lista_freq):
    while n:
        n -= 1
        lista_freq.append(int(input()))
    lista_freq = set(lista_freq)
    return len(lista_freq)

main()