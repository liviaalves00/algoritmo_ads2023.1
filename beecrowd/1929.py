def main():
    #Entrada
    A, B, C, D = map(int, input().split())

    #Processamento
    verificar_triangulo = verificar_possivel_triangulo(A, B, C, D)

    #Saída
    print(verificar_triangulo)

def verificar_possivel_triangulo(A, B, C, D):  
    if A < B + C and B < A + C and C < A + B:
        return 'S'
    elif A < B + D and B < A + D and D < A + B:
        return 'S'
    elif A < C + D and C < A + D and D < A + C:
        return 'S'
    elif B < C + D and C < B + D and D < B + C:
        return 'S'
    else:
        return 'N'
    
main()