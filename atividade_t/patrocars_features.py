import os 
from uuid import uuid4

def inicialization(tipo, cad_montadoras=None):
    if tipo == 'montadoras':
        montadoras = []
        with open('montadoras.txt', 'r') as file:
            data = file.read()
            lines = data.split('\n')

            for line in lines:
                if not line:
                    continue

                atributos = line.split('#')
                montadora = {'id': atributos[0], 'nome': atributos[1], 'pais': atributos[2], 'ano': atributos[3]}
                montadoras.append(montadora)

        return montadoras
    elif tipo == 'modelos':
        modelos = []
        with open('modelos.txt', 'r') as file:
            data = file.read()
            lines = data.split('\n')

            for line in lines:
                if not line:
                    continue

                atributos = line.split('#')

                modelo = {
                    'id': atributos[0],
                    'nome': atributos[1],
                    'montadora': obter_montadora_por_id(cad_montadoras, atributos[2])
                }

                modelos.append(modelo)

        return modelos

def obter_montadora_por_id(montadoras, montadora_id):
    for m in montadoras:
        if m['id'] == montadora_id:
            return m

    return None

def generate_montadora():
    id = str(uuid4())
    nome = input('Digite o nome da montadora: ')
    pais = input('Digite o país: ')
    ano = input('Digite o Ano: ')
    nova_montadora = {
        'id': id,
        'nome': nome,
        'pais': pais,
        'ano': ano,
        'modelos': []
    }

    return nova_montadora

def show_montadoras(montadoras):
    print('\n======== MONTADORAS ============')
    print('===================================')
    for m in montadoras:
        line = f"{m['id']} - {m['nome']} - {m['pais']} - {m['ano']}"
        print(line)
    print('===================================')

def show_modelos(modelos):
    print('\n======== MODELOS ============')
    print('===================================')
    for modelo in modelos:
        item = f"{modelo['id']} - {modelo['nome']} - {modelo['montadora']['nome']}"
        print(item)
    print('===================================')

def obter_index_montadora(montadoras):
    print('\n======== MONTADORASS ============')
    print('===================================')
    for i, m in enumerate(montadoras):
        line = f"{i}: {m['nome']}"
        print(line)
    print('===================================')
    code = int(input('Código da Montadora: '))

    return code

def remover_montadora(montadoras):
    index = obter_index_montadora(montadoras)
    nome = montadoras[index]['nome']
    montadoras.pop(index)
    print(f"Montadora ({nome}) removida com sucesso!")


def atualizar_montadora(montadoras):
    index = obter_index_montadora(montadoras)
    montadora = montadoras[index]
    print('Atualizar dados:')
    print(f"Nome atual: {montadora['nome']}")
    montadora['nome'] = input('Novo nome: ').strip() or montadora['nome']
    print(f"País atual: {montadora['pais']}")
    montadora['pais'] = input('Novo país: ').strip() or montadora['pais']
    print(f"Ano atual: {montadora['ano']}")
    montadora['ano'] = input('Novo ano: ').strip() or montadora['ano']

    print('Montadora atualizada com sucesso!')

def write_data(montadoras, modelos):
    data = ''
    for m in montadoras:
        data += f"{m['id']}#{m['nome']}#{m['pais']}#{m['ano']}\n"

    with open('montadoras.txt', 'w') as file:
        file.write(data)

    data = ''
    for modelo in modelos:
        data += f"{modelo['id']}#{modelo['nome']}#{modelo['montadora']['id']}\n"

    with open('modelos.txt', 'w') as file:
        file.write(data)

def generate_modelo(montadoras):
    index = obter_index_montadora(montadoras)
    montadora_selecionada = montadoras[index]
    nome = input('Nome: ')
    modelo = {}
    modelo['id'] = str(uuid4())
    modelo['nome'] = nome
    modelo['montadora'] = montadora_selecionada

    return modelo

def clear_screen():
    input('press enter...')
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

clear_screen()
