'''
Escreva a tabuada dos números de 1 a 10.
'''
def main():

    multiplicador = 1

    for i in range(1, 11,1):
        for i in range(1, 11,1):
            tabuada = multiplicador * i
            print(f'{multiplicador} x {i} = {tabuada}\n')
        multiplicador += 1

main()