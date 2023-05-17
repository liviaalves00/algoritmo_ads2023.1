'''
Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação,
nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o
numero de identificação e o peso do boi mais magro e do boi mais gordo.
'''

def main():
    #Entrada
    numero_fichas = int(input('Digite o numero de fichas: '))
    
    id_maior = 0
    id_menor = 0

    peso_maior = -float('inf')
    peso_menor = float('inf')
    
    #Processamento
    for i in range(numero_fichas):
        peso_boi = float(input('Digite o peso do boi: '))
        if peso_boi > peso_maior:
            peso_maior = peso_boi
            id_maior = i
           
        if peso_boi < peso_menor:
            peso_menor = peso_boi
            id_menor = i

    #Saída
    print(f'Boi com maior peso: {peso_maior} ID: {id_maior}')
    print(f'Boi com menor peso: {peso_menor} ID: {id_menor}')

main()