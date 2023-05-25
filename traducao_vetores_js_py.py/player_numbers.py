from player_numbers_features import multiplicar_cada_numero_por_n, localizar_posicoes, gerar_vetor, limpar_tela
from player_numbers_utils import bye


def main():
    opcoes = menu() #chama menu
    numeros = []

    opcao = int(input(opcoes))

    while opcao != 0: #opcoes da função menu
        if opcao == 1:
            numeros = gerar_vetor()
        elif opcao == 2:
            print(f"Existem {len(numeros)} itens.")
        elif opcao == 3:
            print(numeros)
        elif opcao == 4:
            localizar_posicoes(numeros)
        elif opcao == 5:
            print("Vetores Anteriores: ")
            print(numeros)
            numeros = multiplicar_cada_numero_por_n(numeros)
            print("Vetores atuais: ")
            print(numeros)
            
        limpar_tela()
        opcao = int(input(opcoes))

    bye()

def menu(): #funcionaem python tambem :) muito daora
    menu = "***** Play Numbers *****"
    menu += "\n-----------------------"
    menu += "\n1 - Gerar Números"
    menu += "\n2 - Mostrar Qtd Números gerados"
    menu +="\n3 - Mostrar números"
    menu +="\n4 - Buscar número"
    menu += "\n5 - Multiplicar números por N"
    menu += "\n0 - Sair"
    menu += "\n\n>> "

    return menu

main()
