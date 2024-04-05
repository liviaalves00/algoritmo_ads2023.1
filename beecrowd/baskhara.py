import math
def main():
    a,b,c = list(map(float, input().split()))

    delta = (math.pow(b, 2)) - ((4 * a) * c)

    if delta < 0 or a == 0:
        print(f'Impossivel calcular')
        return 
    else:
        raiz_delta = math.sqrt(delta)
    
        R1 = (-b + raiz_delta) / (2 * a)
        R2 = (-b - raiz_delta) / (2 * a)

        print(f'R1 = {R1:.5f}')
        print(f'R2 = {R2:.5f}')
   
main()