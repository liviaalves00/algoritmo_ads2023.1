def main():

    numero = float(input())
  
    if 0 <= numero <= 25:
        print('Intervalo [0,25]')
    if 25 < numero <= 50:
        print('Intervalo (25,50]')
    if 50 < numero <= 75:
        print('Intervalo (50,75]')
    if 75 < numero <= 100:
        print('Intervalo (75,100]')
    if numero < 0 or numero > 100:
        print('Fora de intervalo')

main()