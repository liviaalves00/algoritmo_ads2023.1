def main():
    i = 0
    contador_impar = 0
    somador = 0
    
    for i in range(1, 100):
        if i % 2:
            contador_impar += 1
            somador += i / contador_impar
            print(f'{i} / {contador_impar} + ', end = '')
        i += 1
        
    print(f'\nS = {somador:.2f}')
    
main() 