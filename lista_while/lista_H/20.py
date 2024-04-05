def main():
    numero_final = int(input('Digite os números da sequência: '))
    soma = 0
    contador = 0
    
    while contador < numero_final:
        contador += 1
        soma += 1 / contador if contador % 2 == 0 else soma - 1 / contador
        print('1/', contador , '+' if contador % 2 == 0 else '-', end = ' ')
        
    print(f' \nS = {soma:.2f}')

main()