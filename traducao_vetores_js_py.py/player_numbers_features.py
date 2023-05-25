from player_numbers_utils import gerar_vetor_aleatorio, obter_posicoes_em_vetor


def gerar_vetor(): #gera o vetor de acordo com o tamanho
    tamanho = int(input("Quantos elementos? "))
    numeros = gerar_vetor_aleatorio(tamanho)
    return numeros

def localizar_posicoes(numeros): #encontrar posicoes dos vertores
    numero = int(input("Número: "))
    posicoes = obter_posicoes_em_vetor(numeros, numero)

    if len(posicoes) > 0: #verificar as posicoes
        print(f"Número {numero} localizado nas posições: {posicoes}")
    else:
        print("Número não pertence aos vetores!")

def multiplicar_cada_numero_por_n(numeros): #multiplicar cada elemento pelo n desejado(mapeamento)
    vetor = [0] * len(numeros)
    n = int(input("Multiplicador: "))

    for i in range(len(numeros)):
        vetor[i] = numeros[i] * n

    return vetor

def limpar_tela():
    input('press enter...')
    import os
    os.system('cls')  # Limpa o terminal (no windows)

limpar_tela()

