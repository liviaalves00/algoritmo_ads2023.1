from io_utils import*

def gerar_vetor(n, valor_padrao=None):
    vetor = [valor_padrao] * n
    return vetor



def gerar_vetor_padrao(n, valor_padrao = 0):
    vetor = [None] * n
    return vetor

def preencher_vetor_manual(tamanho):
    vetor = []
    for i in range(tamanho):
        elemento = input(f'Digite o elemento {i + 1}: ')
        vetor.append(elemento)
    return vetor

# def preencher_vetor_manual(vetor):
#     for i in range(len(vetor)):
#         novo_item = input('Digite o item a ser adicionado: ')
#         novo_item = float(novo_item)
#     vetor[i] = novo_item
#     if len(vetor) == 0:
#         print('vetor vazio!')
#         return

def preencher_vetor_automaticamente(max,min):
    lista = []
    while min <= max:
        append_numero(lista, min)
        min += 1
    return lista


def mostrar_vetor(vetor):
    print("Vetor:")
    for i, elemento in enumerate(vetor):
        return f'Posição {i}: {elemento}'

# def mostrar_vetor(vetor, max_valores = 10):
#     if obter_tamanho(vetor) == 0:
#         print('vetor vazio!')
#         return 
#     elif len(vetor) > max_valores:
#         print(f'{vetor[0] : max_valores - 1}\b {len(vetor - max_valores - 1)}\b  ({len(vetor) - max_valores} itens) {vetor[len(vetor) - 1]}')
#     else:
#         print(vetor)

