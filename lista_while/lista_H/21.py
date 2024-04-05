def main():
    contador = 0
    contador_impar = 0
    somador = 0
    
    while contador <= 99:
        if contador % 2:
            contador_impar += 1
            somador += i / contador_impar
            print(f'{contador} / {contador_impar} + ', end = '')
        i += 1
        
    print(f'\nS = {somador:.2f}')
    
main() 