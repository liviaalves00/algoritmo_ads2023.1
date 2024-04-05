'''
A SERASA começou a implantar o Serasa Score 2.0 em 2021. O Score é uma forma de avaliar o perfil do consumidor no momento da aquisição de crédito,
seja cartão de crédito ou financiamento de um veículo, apartamento ou empréstimo pessoal.
Desta forma são avaliadas algumas entradas de dados históricos consumidor e, caso não esteja negativado, apresentando um valor entre 0 e 1000
Baseado nisso, faça um programa que receba valores de 0 a 100 em cada um dos 3 critérios de cálculo, ou seja, como se fosse uma Escala, no item a.
você pode ter de 0 a 100, se for 100, por exemplo, significa 100% dos pontos previstos, assim Score 1.0 (260) e Score 2.0 (620),
se fosse 50% então esse item a. seria 130 e 310, respectivamente em cada Score 1.0 e 2.0.
Aplique essa formula de cada uma e apresente o valor do Score tanto versão Score 1.0 quanto na versão Score 2.0.
'''

def main():
    print(20 * '=', 'SIMULADOR SERASA', 20 * '=')
    print()
    print('Digite valores de 0 a 100 em cada umas das três perguntas...')
    print()
    #Entrada
    criterio_a = int(input('Dados positivos (cartão de crédito, consórcio, consignado, empréstimos e financiamentos) comportamentos de pagamento, tempo dos contratos e tipos de contratos: ' ))
    while not criterio_a <= 100:
        criterio_a = int(input('Digite novamente os dados positivos:'))
    criterio_b = int(input('Informações de dívidas, histórico de regularização e em aberto: '))
    while not criterio_b <= 100:
        criterio_b = int(input('Digie novamente as informações de dívida: '))
    
    criterio_c = int(input('Consultas para novos contratos de serviço ou crédito: '))
    while not criterio_c <= 100:
        criterio_c = int(input('Digite novamente as consultas para novos contratos de serviço ou crédito: '))

    #Processamento obs: decomposição/pensamento computacional
    #comecei lavando o banheiro da escola
    score_a = calcular_score_a(criterio_a)
    score_b = calcular_score_b(criterio_b)
    score_c = calcular_score_c(criterio_c)

    score_a2 = calcular_score_a2(criterio_a)
    score_b2 = calcular_score_b2(criterio_b)
    score_c2 = calcular_score_c2(criterio_c)

    total_score_um = (score_a + score_b + score_c) * 10 
    total_score_dois = (score_a2 + score_b2 + score_c2) * 10 

    categoria = definir_categoria(total_score_um)
    categoria_dois = definiir_categoria_dois(total_score_dois)

    #Saída
    mostrar_resultados(score_a, score_b, score_c, score_a2, score_b2, score_c2, total_score_um, total_score_dois, categoria, categoria_dois)

def calcular_score_a(a):
    return a * 0.26

def calcular_score_b(b):
    return b * 0.57 

def calcular_score_c(c):
    return c * 0.17

def calcular_score_a2(a2):
    return a2 * 0.62

def calcular_score_b2(b2):
    return b2 * 0.17

def calcular_score_c2(c2):
    return c2 * 0.17

def definir_categoria(um):
    if um <= 400:
        return 'BAIXO'
    elif um <= 600:
        return 'REGULAR'
    elif um <= 800:
        return 'BOM'
    elif um <= 1000:
        return 'MUITO BOM'

def definiir_categoria_dois(dois):
    if dois <= 300:
        return 'BAIXO'
    elif dois <= 500:
        return 'REGULAR'
    elif dois <= 700:
        return 'BOM'
    elif dois <= 1000:
        return 'MUITO BOM'
    
def mostrar_resultados(a, b, c, a2, b2, c2, total1, total2, cat, cat2):
    print('=' * 50)
    print(f'Score 1 A: {a}')
    print(f'Score 1 B: {b:.2f}')
    print(f'Score 1 C: {a}')
    print(f'Score 2 A: {a2}')
    print(f'Score 2 B: {b2}')
    print(f'Score 2 C: {c2}')
    print(f'Total Score 1: {total1}')
    print(f'Total Score 2: {total2}')
    print(f'Categoria Score 1: {cat}')
    print(f'Categoria Score 2: {cat2}')
    print('=' * 50)

main()