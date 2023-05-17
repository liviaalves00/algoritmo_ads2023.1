'''
Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de
um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área
não pode ser negativo.
'''
def main():
    coordenada_x = int(input('Digite a coordenada x: '))
    coordenada_y = int(input('Digite a coordenada y: '))

    calculo_area_triangulo = calcular_area_triangulo(coordenada_x, coordenada_y)

    print(calculo_area_triangulo)

def calcular_area_triangulo(x, y):
    area = abs((x * y) / 2)
    return area

main()