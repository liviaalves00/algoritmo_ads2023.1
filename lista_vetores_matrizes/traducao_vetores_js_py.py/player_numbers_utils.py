import random

def gerar_vetor_aleatorio(tamanho):
    vetor = [0] * tamanho

    for i in range(tamanho):
        vetor[i] = obter_numero_aleatorio()

    return vetor

def obter_numero_aleatorio(limite=100):
    return random.randint(0, limite)

def bye():
    tchaus = [
        "Arrivedercci", "Se divertiu ne? Pois agora vaza...", "Até nunca mais", "Não volte mais", "OH NO", "OH MY GOD"
    ]

    index = random.randint(0, len(tchaus) - 1)

    print(tchaus[index])

def obter_posicoes_em_vetor(vetor, valor):
    posicoes = []
    for i in range(len(vetor)):
        if vetor[i] == valor:
            posicoes.append(i)

    return posicoes
