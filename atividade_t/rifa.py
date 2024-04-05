from rifa_features import*
# import sys
# sys.path.append("./data/dados_rifa.txt")

pessoas_file = open("dados_rifa.txt", "r")

pessoas = pessoas_file.readlines()
pessoas = mapear(pessoas, lambda x: x.strip())

data = {
        'pessoas' : pessoas,
        'valor_ponto': 0,
        'quantidade_premios': 0,
        'max_premios': 0,
        'taxa_adm' : 0,
        'pontos_sorteados' : [],
        'pontos_disponiveis' : pontos_disponiveis(pessoas),
        'pontos_comprados' : pontos_comprados(pessoas)
    }

def main():
    data = data.copy()
    while True:
        verificar_nulos(data)
        clear_screen()
        opcao = obter_numero_intervalo(menu(), 10, 0)
        if opcao == 0:
            print('Tchau coração! ')
            break
        if opcao == 1:
            obter_numero_de_pontos(data)
        if opcao == 2:
            numero_cada_pessoa_posicao(data)
        if opcao == 3:
            data['valor_ponto'] = 0
        if opcao == 4:
            dados_gerais(data)
        if opcao == 5:
            for i in range(100):
                print('Resetando!')
                clear_screen()
            del data
            data = data.copy()
            print('Resetado!')
        if opcao == 6:
            print('GANHADORES!!!!')
            while not data['quantidade_premios'] <= 0:
                fazer_sorteio(data)
            print('=================')
            dados_gerais(data)
            break
        clear_screen()

def menu():
   menu_options = input('=========================== PATROBET1: RIFA ===================================')
   menu_options += '1 - Obter total de pontos'
   menu_options += '2 - Obter Ponto e nome de cada participante'
   menu_options += '3 - Definir novo valor do ponto'
   menu_options += '4 - Dados Gerais'
   menu_options += '5 - Resetar Rifa'
   menu_options += '6 - Sortear Rifa'
   menu_options += '0 - Sair'
   menu_options += '\n\n>>'

   return menu_options

def obter_numero_intervalo(max:float, min:float):
    numero = float(input('Digite um número: '))
    if not min <= numero <= max:
        obter_numero_intervalo(f'Digite um número pertencente ao intervalo ({min}) -> ({max}): ', max, min)
    return numero

main()