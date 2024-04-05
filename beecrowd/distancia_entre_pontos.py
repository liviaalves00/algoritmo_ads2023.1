def main():
    x1, y1 = list(map(float, input().split())) 
    x2, y2 = list(map(float, input().split())) 

    distancia = calcular_distancia(x1, y1, x2, y2)

    print(f'{distancia:.4f}')

def calcular_distancia(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

main()