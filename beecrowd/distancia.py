def main():
    distancia = int(input())

    minutos = calcular_tempo_km(distancia)

    print(f'{minutos} minutos')

def calcular_tempo_km(distancia):
    return (60 * distancia) / 30

main()