from random import randint
import random

def gerar_vetor():
    tamanho = int(input('Digite o Tamanho do vetor: '))
    vetor = [0] * tamanho
    return vetor

def gerar_vetor_aleatorio(tamanho):
    vetor = [random.randint(0, limite=100) for _ in range(tamanho)]
    return vetor

# def obter_numero_aleatorio(limite=100):
#     return random.randint(0, limite)

def preencher_vetor_automaticamente(vetor):
    valor_maximo = int(input('Digite o Limite máximo: '))
    valor_minimo = int(input('Digite o Limite mínimo: '))

    for i in range(len(vetor)):
        vetor[i] = randint(valor_minimo, valor_maximo)

def preencher_vetor_manualmente(vetor):
    for i in range(len(vetor)):
        item = input(f"Digite o valor para a posição {i}: ")
        vetor[i] = item

def mapear(vetor, funcao):
    novo_vetor = []
    for i in vetor :
        novo_vetor.append(funcao(i))
    return novo_vetor

def contar_positivos_negativos_zeros(vetor):
    positivos = sum(1 for i in vetor if i > 0)
    negativos = sum(1 for i in vetor if i < 0)
    zeros = sum(1 for i in vetor if i == 0)
    return f'Positivos: {positivos} \nNegativos: {negativos} \nZeros: {zeros}'

def ordem_crescente(vetor, opcao):
    return sorted(vetor, key=opcao)

def ordem_decrescente(vetor, opcao):
    return sorted(vetor, key=opcao, reverse=True)

def ordenar_numeros(vetor, opcao, N=None):
    if opcao == 'todos':
        vetor.sort()
        print(vetor)

    elif opcao == 'pares':
        vetor_pares = [numero for numero in vetor if numero % 2 == 0]
        vetor_pares.sort()
        for i, numero in enumerate(vetor):
            if numero % 2 == 0:
                vetor[i] = vetor_pares.pop(0)
        print(vetor)

    elif opcao == 'impares':
        vetor_impares = [numero for numero in vetor if numero % 2 != 0]
        vetor_impares.sort()
        for i, numero in enumerate(vetor):
            if numero % 2 != 0:
                vetor[i] = vetor_impares.pop(0)
        print(vetor)

    elif opcao == 'positivos':
        vetor_positivos = [numero for numero in vetor if numero > 0]
        vetor_positivos.sort()
        for i, numero in enumerate(vetor):
            if numero > 0:
                vetor[i] = vetor_positivos.pop(0)
        print(vetor)

    elif opcao == 'negativos':
        vetor_negativos = [numero for numero in vetor if numero < 0]
        vetor_negativos.sort()
        for i, numero in enumerate(vetor):
            if numero < 0:
                vetor[i] = vetor_negativos.pop(0)
        print(vetor)

    elif opcao == 'multiplos_positivos':
        N = int(input('Digite o valor de n: ' ))
        vetor_multiplos_positivos = [numero for numero in vetor if numero > 0 and numero % N == 0]
        vetor_multiplos_positivos.sort()
        for i, numero in enumerate(vetor):
            if numero > 0 and numero % N == 0:
                vetor[i] = vetor_multiplos_positivos.pop(0)
        print(vetor)

    elif opcao == 'multiplos_negativos':
        N = int(input('Digite o valor de n:'))
        vetor_multiplos_negativos = [numero for numero in vetor if numero < 0 and numero % N == 0]
        vetor_multiplos_negativos.sort()
        for i, numero in enumerate(vetor):
            if numero < 0 and numero % N == 0:
                vetor[i] = vetor_multiplos_negativos.pop(0)
        print(vetor)
    else:
        print('Opção inválida!')
        
def ordenar_numeros_decrescente(vetor, opcao, N=None):
    if opcao == 'todos':
        vetor.sort(reverse=True)
        print(vetor)
    elif opcao == 'pares':
        vetor_pares = [numero for numero in vetor if numero % 2 == 0]
        vetor_pares.sort(reverse=True)
        for i, numero in enumerate(vetor):
            if numero % 2 == 0:
                vetor[i] = vetor_pares.pop(0)
        print(vetor)

    elif opcao == 'impares':
        vetor_impares = [numero for numero in vetor if numero % 2 != 0]
        vetor_impares.sort(reverse=True)
        for i, numero in enumerate(vetor):
            if numero % 2 != 0:
                vetor[i] = vetor_impares.pop(0)
        print(vetor)

    elif opcao == 'positivos':
        vetor_positivos = [numero for numero in vetor if numero > 0]
        vetor_positivos.sort(reverse=True)
        for i, numero in enumerate(vetor):
            if numero > 0:
                vetor[i] = vetor_positivos.pop(0)
        print(vetor)

    elif opcao == 'negativos':
        vetor_negativos = [numero for numero in vetor if numero < 0]
        vetor_negativos.sort(reverse=True)
        for i, numero in enumerate(vetor):
            if numero < 0:
                vetor[i] = vetor_negativos.pop(0)
        print(vetor)

    elif opcao == 'multiplos_positivos':
        N = int(input('Digite o valor de n: '))
        vetor_multiplos_positivos = [numero for numero in vetor if numero > 0 and numero % N == 0]
        vetor_multiplos_positivos.sort(reverse=True)
        for i, numero in enumerate(vetor):
            if numero > 0 and numero % N == 0:
                vetor[i] = vetor_multiplos_positivos.pop(0)
        print(vetor)

    elif opcao == 'multiplos_negativos':
        N = int(input('Digite o valor de n: '))
        vetor_multiplos_negativos = [num for num in vetor if num < 0 and num % N == 0]
        vetor_multiplos_negativos.sort(reverse=True)
        for i, numero in enumerate(vetor):
            if numero < 0 and numero % N == 0:
                vetor[i] = vetor_multiplos_negativos.pop(0)
        print(vetor)
    else:
        print("Opção inválida!")

def maiores_elementos(vetor):
    return sorted(vetor, reverse=True) [:3]

def menores_elementos(vetor):
    return sorted(vetor)[:3]

def encontrar_maior_menor(vetor):
    return max(vetor), min(vetor)

def somar_elementos(vetor):
    return sum(vetor)

def somatorio_negativos(vetor):
    return sum(item for item in vetor if item < 0)

def somatorio_positivos(vetor):
    return sum(item for item in vetor if item > 0)

def somatorio_todos_positivos_negativos(vetor):
    soma_total = sum(vetor)
    soma_positivos = somatorio_positivos(vetor)
    soma_negativos = somatorio_negativos(vetor)
    return f'Todos: {soma_total} \nPositivos: {soma_positivos} \nNegativos: {soma_negativos}'

def calcular_media_mediana(vetor):
    vetor_ordenado = sorted(vetor)
    tamanho = len(vetor_ordenado)
    media = sum(vetor_ordenado) / tamanho

    if tamanho % 2 == 0:
        valor_um = tamanho // 2
        valor_dois = valor_um - 1
        mediana = (vetor_ordenado[valor_um] + vetor_ordenado[valor_dois]) / 2
    else:
        indice = tamanho // 2
        mediana = vetor_ordenado[indice]

    return f'Média: {media:.2f} \nMediana: {mediana}'

def calcular_media_mediana_positivos_negativos(vetor):
    positivos = []
    negativos = []
    
    for valor in vetor:
        if valor > 0:
            positivos.append(valor)
        elif valor < 0:
            negativos.append(valor)
    
    return f'Positivos: {calcular_media_mediana(positivos)} \nNegativos: {calcular_media_mediana(negativos)}'

def novo_vetor_igual_ou_nao(vetor): #alterar
        novo_vetor = gerar_vetor()
        preencher_vetor_automaticamente(novo_vetor)

        if all(i in vetor for i in novo_vetor):
            print('Novo vetor: ', novo_vetor)
            print('Vetor presente nos número e na ordem.')
        else:
            print('Novo vetor: ', novo_vetor)
            print('Vetor presente nos número e na ordem.')
            
def gerar_grupos(vetor):
    numero_grupos = int(input("Digite o número de grupos: "))
    tamanho_grupos = int(input("Digite o tamanho dos grupos: "))

    if numero_grupos * tamanho_grupos > len(vetor):
        print('Tamanho Invalido para formar os')
    else:
        random.shuffle(vetor)
        grupos = [vetor[i:i + tamanho_grupos] for i in range(0, len(vetor), tamanho_grupos)]
        print("Grupos gerados:")
        for i, grupo in enumerate(grupos):
            print(f"Grupo {i + 1}: {grupo}")

def sortear_positivo_negativo(vetor):
    positivos = [int(i) for i in vetor if i > 0]
    negativos = [i for i in vetor if i < 0]

    if positivos and negativos:
        positivo = random.choice(positivos)
        negativo = random.choice(negativos)
        print(f'Positivo sorteado: {positivo}')
        print(f'Número negativo sorteado: {negativo}')
    else:
        print('0 números positivos ou negativos')
      
def maiores_menores_media(vetor): #alterar aqui
    media = sum(vetor) / len(vetor)
    maiores = []
    menores = []
    
    for valor in vetor:
        if valor > media:
            maiores.append(valor)
        elif valor < media:
            menores.append(valor)
    
    print("Valor médio:", media)
    print("Números maiores que a média:", maiores)
    print("Números menores que a média:", menores)
  
def somar_media_positivos_produto_negativos(vetor):
    soma_media_positivos = 0
    produto_negativos = 1
    count_positivos = 0
    count_negativos = 0

    for valor in vetor:
        if valor > 0 and valor % 2 == 0:
            soma_media_positivos += valor
            count_positivos += 1
        elif valor < 0 and valor % 2 == 0:
            produto_negativos *= valor / 2
            count_negativos += 1 
    if count_positivos > 0:
        media_positivos = soma_media_positivos / count_positivos
    else:
        media_positivos = 0
    
    resultado = media_positivos + produto_negativos
    return resultado

def eliminar_multiplos(colecao, n, m):
    vetor_resultado = []
    
    for valor in colecao:
        if valor % n != 0 or valor % m != 0:
            vetor_resultado.append(valor)
    
    return vetor_resultado