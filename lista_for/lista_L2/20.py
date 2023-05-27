def main():
    numero_final = int(input('Digite os números da sequência: '))
    soma = 0
    
    for i in range(1, numero_final + 1):
        soma += 1 / i if i % 2 == 0 else soma - 1 / i
        print('1/', i , '+' if i % 2 == 0 else '-', end = ' ')
        
    print(f' \nS = {soma:.2f}')

main()