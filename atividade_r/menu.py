from menu_featuress import*
from happy_utils import*

def main():
    menu = show_menu()
    vetor_numeros = []
    opcoes = int(input(menu))

    while opcoes != 0:
        if opcoes == 1:
            vetor_numeros = gerar_vetor()
        elif opcoes == 2:
            preencher_vetor_manualmente(vetor_numeros)
        elif opcoes == 3:
            preencher_vetor_automaticamente(vetor_numeros)
        elif opcoes == 4:
            print(vetor_numeros)
        elif opcoes == 5:
            print('Antes: ')
            print(vetor_numeros)
            expoente = int(input('Digite o N: '))
            vetor_numeros = mapear(vetor_numeros, lambda i: i ** int(expoente))
            print(vetor_numeros)
        elif opcoes == 6:
            print(vetor_numeros)
            print(contar_positivos_negativos_zeros(vetor_numeros))
        elif opcoes == 7:
            print(vetor_numeros)
            print(somatorio_todos_positivos_negativos(vetor_numeros))
        elif opcoes == 8:
            print(vetor_numeros)
            print(calcular_media_mediana(vetor_numeros))
            print(calcular_media_mediana_positivos_negativos(vetor_numeros))
        elif opcoes == 9:
            print(vetor_numeros)
            print(encontrar_maior_menor(vetor_numeros))
        elif opcoes == 10:
            print(vetor_numeros)
            print(sortear_positivo_negativo(vetor_numeros))
        elif opcoes == 11:
            print(vetor_numeros)
            vetor_numeros = gerar_grupos(vetor_numeros)
            print(vetor_numeros)
        elif opcoes == 12:
            print(vetor_numeros)
            print(novo_vetor_igual_ou_nao(vetor_numeros))
            print(vetor_numeros)
        elif opcoes == 13:
            print(vetor_numeros)
            print('Maiores: ')
            print(maiores_elementos(vetor_numeros))
        elif opcoes == 14:
            print(vetor_numeros)
            print('Menores: ')
            print(menores_elementos(vetor_numeros))
        elif opcoes == 15:
            print(vetor_numeros)
            print(maiores_menores_media(vetor_numeros))
        elif opcoes == 16:
            print(vetor_numeros)
            print(somar_media_positivos_produto_negativos(vetor_numeros))
        elif opcoes == 17:
            print('Antes: ')
            print(vetor_numeros)
            opcao = input('Choose one: T P I P N MP MN:')
            print('Depois: ')
            print(ordenar_numeros(vetor_numeros, opcao))
        elif opcoes == 18:
            print('Antes: ')
            print(vetor_numeros)
            opcao = input('Choose one: T P I P N MP MN:')
            print('Depois:')
            print(ordenar_numeros_decrescente(vetor_numeros, opcao))
        elif opcoes == 19:
            
            print(vetor_numeros)
            n = int(input('Digite o valor de N: '))
            m = int(input('Digite o valor de M: '))
            vetor_numeros = eliminar_multiplos(vetor_numeros, n, m)
            print(vetor_numeros)

        clear_screen()
        opcoes = int(input(menu))
    
    bye()

def show_menu():
      menu_options = "===== MENU OPTIONS ====="
      menu_options += "\n-----------------------"
      menu_options += "\n1 - Gerar Vetor Padrão"
      menu_options += "\n2 - Preencher Vetor Manual"
      menu_options += "\n3 - Preencher Vetor Automático"
      menu_options += "\n4 - Mostrar Vetor"
      menu_options += "\n5 - Elevar a Potência de N"
      menu_options += "\n6 - Contar: Positivos, Ngegativos e Zeros"
      menu_options += "\n7 - Somatório: Positivos e Negativos"
      menu_options += "\n8 - Média e Mediana: Positivos e Negativos"
      menu_options += "\n9 - Maior e Menor Número"
      menu_options += "\n10 - Sortear Dois Números: Positivos e Negativos"
      menu_options += "\n11 - Gerar N grupos de T tamanhos."
      menu_options += "\n12 - Verificar se N está presente nos números do sistema"
      menu_options += "\n13 - Maiores Números do vetor"
      menu_options += "\n14 - Menores Numeros do vetor"
      menu_options += "\n15 - Valor médio, listar números maiores que a Média e Menores que a Média"
      menu_options += "\n16 - Somatório da Média de Positivos múltiplos dois com o Produto acumulado dos números negativos pares reduzidos à metade"
      menu_options += "\n17 - Ordenar os números em ordem crescente: Pares, Impares, Positivos, Negativos e Multiplos de N"
      menu_options += "\n18 - Ordenar os números em ordem decrescente: Pares, Impares, Positivos, Negativos e Multiplos de N"
      menu_options += "\n19 - Eliminar números múltiplos de N e M"
      menu_options += "\n0 - Sair"
      menu_options += "\n\n>> "

      return menu_options

main()
