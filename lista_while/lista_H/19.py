def main():
    numero_limite = int(input('Digite o número limite: '))
    somador = 0

    while numero_limite > 1:
        numero_limite -= 1
        somador += 1 / numero_limite
        print(f'1/{numero_limite}', end = ' + ')
        
    print(f'\nS = {somador:.2f}')
    
main()