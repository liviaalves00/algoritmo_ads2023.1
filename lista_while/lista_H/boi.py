def main():
    numero = int(input('Digite o número de fichas: '))

    boi_mais_gordo = - float('inf')
    boi_mais_magro =  float('inf')
    id_menor = 0
    id_maior = 0

    while numero > 0:
        peso = int(input('Peso (kg): '))

        if peso > boi_mais_gordo:
            boi_mais_gordo = peso
            id_maior = numero

        if peso < boi_mais_magro:
            boi_mais_magro = peso
            id_menor = numero

        numero -=1 

    print(f'Boi de menor peso => ID: {id_menor} - {boi_mais_magro} kg')
    print(f'Boi de maior peso => ID: {id_maior} - {boi_mais_gordo} kg')
   
main()