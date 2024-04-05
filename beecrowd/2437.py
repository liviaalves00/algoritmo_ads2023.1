def main():
    #Entrada
    x1, y1, x2, y2 = input().split()

    #Processamento
    distancia = calcular_distancia(x1, y1, x2, y2 )

    #Saída
    print(distancia)

def calcular_distancia(x1, y1, x2, y2 ):
    return (abs(int(x2) - int(x1))) + (abs(int(y2) - int(y1)))

main()