def main():
    #Entrada
    A, B, C = map(int, input().split())

    #Processamento
    bolo = verificar_bolo(A, B, C)

    #Saída
    print(bolo)

def verificar_bolo(A, B, C):
    return (min(A // 2, B // 3, C // 5))

main()