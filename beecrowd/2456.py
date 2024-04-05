import random

def main():
    #Entrada
    carta1, carta2, carta3, carta4, carta5  = (input().split())

    #Processamento
    cartas = carta1, carta2, carta3, carta4, carta5

    carta_ordenada = verificar_ordenacao(cartas)
    
    #Processamento
    print(carta_ordenada)

def verificar_ordenacao(cartas):
   
    for i in cartas:
        if cartas == sortedcartas:
            return 'C'
        if cartas == sorted(cartas, reverse=True):
            return 'D'
        else:
            return 'N'

# def verificar_ordenacao(cartas):
#     sortedcartas = sorted(cartas) 
#     if cartas == sortedcartas:
#         return 'C'
#     elif cartas == sorted(cartas,reverse = False):
#         return 'D'
#     else:
#         return 'N'
   
main()