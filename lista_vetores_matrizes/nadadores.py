'''
Confira o resultado de uma competição de natação entre dois clubes. O programa deve ler o número da
prova e a quantidade de nadadores. O fim dos dados é indicado pelo número da prova igual a 0 e
quantidade de nadadores igual a 0. A seguir, para cada nadador deverá ler nome, classificação, tempo,
clube (“a” ou “b”) e determinar os pontos obtidos por cada clube, de acordo com o seguinte critério:
Ao final, o algoritmo deve escreva os totais de pontos de cada clube, indicando o clube vencedor.
'''
def main():
    #Entrada
    numero_prova = int(input('Digite o numero da prova: '))
    qtd_nadadores = int(input('Digite a quantidade de nadadores: '))
    
    pontos_clube_a = 0
    pontos_clube_b = 0

    #Processamento
    while numero_prova != 0 or qtd_nadadores != 0:
        contador = 0
        while contador < qtd_nadadores:
            nome = str(input('Digite seu nome: '))
            classificacao = int(input('Digite sua classificação: '))
            tempo = float(input('Digite o tempo que levou o percurso: '))
            clube = str(input('Digite qual o seu clube: '))

            verificar_classificacao = classificar_pontos(classificacao)
          

            verificacao_campeao = verificar_campeao(pontos_clube_a, pontos_clube_b)
            
            if clube == 'a':
                pontos_clube_a += verificar_classificacao
            else:
                pontos_clube_b += verificar_classificacao

            contador += 1
            numero_prova = int(input('Digite o numero da prova: '))
            qtd_nadadores = int(input('Digite a quantidade de nadadores: '))

    #Saída
    print(f'Pontos: {pontos_clube_a}')
    print(f'Pontos: {pontos_clube_b}')
    print(f'Campeão Clube: {verificacao_campeao}')

def  classificar_pontos(classificacao):
    if classificacao == 1:
        return 9
    elif classificacao == 2:
        return 6
    elif classificacao == 3:
        return 4
    elif classificacao == 4:
        return 3
    
def verificar_campeao(pontos_clube_a, pontos_clube_b):
    if pontos_clube_a > pontos_clube_b:
        return 'A'
    elif pontos_clube_b > pontos_clube_a:
        return 'B'
    
    return 'Empate'

main()