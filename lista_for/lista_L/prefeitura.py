'''
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
escreva:
a) média de salário da população;
b) média de número de filhos;
c) percentual de pessoas com salário de até R$ 1.000,00.
'''
def main():
    #Entrada
    numero_habitante = int(input('Digite a quantidade de habitantes: '))
    
    for i in range(numero_habitante):
        salario = float(input('Digite seu sálario: '))
        qtd_filhos = int(input('Digite o número de filhos: '))
        
        #Processamento
        media_salario = calcular_media_salario(salario, numero_habitante)
        media_filhos = calcular_media_filhos(qtd_filhos, numero_habitante)
        percentual = calcular_percental(salario)
    #Saída
    mostrar_resultados(media_salario, media_filhos, percentual)


def calcular_media_salario(salario, habitante):
    return salario / habitante

def calcular_media_filhos(filhos, habitante):
    return filhos / habitante

def calcular_percental(salario):
    while salario <= 1000:
        return (salario * 40 * 0.15)
    
def mostrar_resultados(media_salario, media_filhos, percentual):
    print(f'Média Salarial: {media_salario}')
    print(f'Média de Filhos: {media_filhos:.1f}')
    print(f'Percentual: {percentual}')

main()