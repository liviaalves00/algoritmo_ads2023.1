def main():
    tempo_gasto = int(input())
    velocidade_media = int(input())

    km = tempo_gasto * velocidade_media
    quantidade_litros = km / 12

    print(f'{quantidade_litros:.3f}')

main()