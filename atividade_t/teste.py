import random
import os

# Função para ler os pontos de um arquivo texto
def ler_pontos():
    pontos = []
    try:
        with open("pontos.txt", "r") as arquivo:
            for linha in arquivo:
                pontos.append(linha.strip())
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    return pontos

# Função para escrever os pontos em um arquivo texto
def escrever_pontos(pontos):
    with open("pontos.txt", "w") as arquivo:
        for ponto in pontos:
            arquivo.write(ponto + "\n")



# Função principal do sistema
def main():
    pontos = ler_pontos()
    pontos_vendidos = [ponto for ponto in pontos if ponto != "-"]
    pontos_nao_vendidos = [i+1 for i, ponto in enumerate(pontos) if ponto == "-"]
    valor_ponto = 0
    taxa_administracao = 0
    arrecadado = 0
    taxa = 0
    quantidade_premios = 0

    while True:
        print("\n===== MENU =====")
        print("1. Definir valor do ponto da rifa")
        print("2. Definir taxa de administração")
        print("3. Calcular valor arrecadado")
        print("4. Definir quantidade de prêmios")
        print("5. Realizar sorteio")
        print("6. Zerar/Resetar")
        print("7. Mostrar dados gerais da rifa")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor_ponto = float(input("Digite o valor do ponto da rifa: "))
        elif opcao == "2":
            taxa_administracao = float(input("Digite a taxa de administração da rifa (%): "))
        elif opcao == "3":
            arrecadado, taxa = calcular_arrecadado(len(pontos_vendidos), valor_ponto, taxa_administracao)
            print(f"Valor arrecadado: R${arrecadado:.2f}")
            print(f"Taxa de administração: R${taxa:.2f}")
        elif opcao == "4":
            quantidade_premios = int(input("Digite a quantidade de prêmios a serem rifados: "))
        elif opcao == "5":
            realizar_sorteio(pontos_vendidos, quantidade_premios)
        elif opcao == "6":
            pontos_vendidos = []
            pontos_nao_vendidos = list(range(1, len(pontos)+1))
            escrever_pontos(["-" for _ in range(len(pontos))])
            print("A rifa foi zerada/resetada.")
        elif opcao == "7":
            print(f"Quantidade de pontos disponíveis: {len(pontos)}")
            print(f"Quantidade de pontos vendidos: {len(pontos_vendidos)}")
            print(f"Quantidade de pontos não vendidos: {len(pontos_nao_vendidos)}")
            print("Lista de pontos vendidos:")
            print(pontos_vendidos)
            print("Lista de pontos não vendidos:")
            print(pontos_nao_vendidos)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

    clear_screen()

# Função para calcular o valor arrecadado e a taxa de administração
def calcular_arrecadado(pontos_vendidos, valor_ponto, taxa_administracao):
    arrecadado = pontos_vendidos * valor_ponto
    taxa = arrecadado * taxa_administracao / 100
    return arrecadado, taxa

# Função para realizar o sorteio dos prêmios
def realizar_sorteio(pontos_vendidos, quantidade_premios):
    if len(pontos_vendidos) < quantidade_premios:
        print("Não há pontos suficientes para realizar o sorteio.")
        return
    numeros_sorteio = random.sample(range(1, len(pontos_vendidos) + 1), quantidade_premios)
    print("Resultados do sorteio:")
    for numero in numeros_sorteio:
        print(f"Número sorteado: {numero}")
        print(f"Nome do ganhador: {pontos_vendidos[numero - 1]}")
        print("-----------------------")

def clear_screen():
    input('press enter...')
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

clear_screen()
if __name__ == "__main__":
    main()