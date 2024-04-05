'''
João precisa de um dinheiro emprestado para comprar um Notebook para estudar programação.
Para isso, foi ao RSBank fazer uma simulação.
As taxas de empréstimo do banco obedecem à regra dos Juros Compostos Mensais,
ou seja, o valor é calculado cumulativamente mês a mês, ou seja,
aplica-se os juros sobre o valor total no primeiro mês e esse passa a ser a base para o segundo mês.

Porém a taxa de juros aplicada é calculada de acordo com o prazo de parcelamento (vide tabela) e à SELIC,
atualmente em 13,75% (abril/2023). O usuário só pode parcelar o empréstimo em até 24x (min. 2 parcelas).
Valor mínimo de empréstimo é de um salário mínimo. Valor máximo de parcela é 40% da Renda Mensal do Cliente.

Antes de calcular os juros é necessário calcular o IOF (Imposto sobre Operações Financeiras) pago ao Governo Federal antes de aplicar os Juros.
O IOF é calculado da seguinte forma: 0,38% sobre valor total (independente do prazo) + 0,0082% por cada dia do prazo do empréstimo.
Considere todos os meses com 30 dias. Os juros são aplicados sobre o valor a ser recebido pelo Cliente + IOF
---> Peça ao usuário Renda Mensal, Valor Empréstimo e Prazo desejados, valide os dados a serem recebidos.
---> Calcule e escreva na tela:
Valor Pedido
Valor do IOF
Valor dos Juros a pagar
Valor Total a pagar (ex.: "R$ 5148,00")
Valor da Parcela Mensal (ex.: "16x de R$ 321,75")
Comprometimento da Renda Mensal (%)
Se Empréstimo APROVADO ou NEGADO (se a renda mensal suporta a parcela)
'''

def main():
    print('='*10, 'empréstimo'.upper(), '='*10)
    #Entrada
    valor_emprestimo = float(input('Digite o valor do empréstimo: '))
    renda_mensal = float(input('Digite sua renda mensal: '))
    prazo = int(input('Digite o prazo: '))
    #Processamento
    taxa_selic = calcular_taxa_selic(prazo)
    montante = calcular_juros_compostos(valor_emprestimo, taxa_selic, prazo, retorno = 'montante')
    calculo_juros_compostos = montante - valor_emprestimo
    dias_meses = converter_dias_meses(prazo)
    iof = calcular_iof(montante, dias_meses)
    valor_parcela = montante / prazo
    valor_final = montante + iof
    
    verificacao_aprovado = verificar_aprovacao(valor_parcela, renda_mensal)
    parcela_aprovada = quantidade_parcela(prazo)
    while not quantidade_parcela(prazo):
        prazo = int(input('Digite o prazo novamente: '))
         
    if not verificar_aprovacao(valor_parcela, renda_mensal):
        print('Sua renda não é suficiente  para a aprovação!')
        renda_mensal = float(input('Digite sua renda mensal: '))
    
    compro_renda = comprometimento_renda(parcela_aprovada, renda_mensal)

    #Saída
    mostre_resultados = mostrar_resultados(valor_emprestimo, iof, calculo_juros_compostos, valor_parcela, valor_final, verificacao_aprovado, compro_renda)

def calcular_taxa_selic(prazo):
    selic = 13.75 / 100
    if prazo <= 6:
        return selic * 0.50
    elif prazo <= 12:
        return selic * 0.75
    elif prazo <= 18:
        return selic * 0.10
    elif prazo > 18:
        return selic * 0.13
    
def converter_dias_meses(prazo): #converter tudo para meses
    return prazo * 30

def calcular_juros_compostos(emprestimo, taxa, prazo, retorno = 'montante'):
    contador_meses = 0
    capital = emprestimo
    while contador_meses < prazo:
        juros = capital * taxa
        capital += juros 
        contador_meses += 1
    return capital - emprestimo 

#O IOF é calculado da seguinte forma: 0,38% sobre valor total (independente do prazo) + 0,0082% por cada dia do prazo do empréstimo.
def calcular_iof(valor_total, dias_meses):
     imposto_fixo = ((0.38/100) * valor_total)
     imposto_dia = ((0.0082/100) * valor_total)
     quantidade_dias = dias_meses
     iof = imposto_fixo * imposto_dia * quantidade_dias
     return iof

def comprometimento_renda(parcela, renda):
    comprometimento = (parcela / renda) * 100
    if comprometimento < 40:
        return comprometimento

def quantidade_parcela(prazo): #verificar se a parcela está dentro dos requisitos 
    return 2 <= prazo <= 24

def verificar_aprovacao(emprestimo, renda):
    a = emprestimo == renda
    a = 'APROVADA'
    return a

def verificar_parcela(parcela, renda): #verificar se a parcela é 40%
    return parcela <= renda * 0.40

def mostrar_resultados(valor_emprestimo, iof, calculo_juros_compostos, valor_parcela, valor_final, verificacao_aprovado, compro_renda): #'via' do joao
    print('=' * 50)
    print()
    print(f'Sua verificacao foi: {verificacao_aprovado}')
    print(f'Comprometimento de Renda: {compro_renda:.2f}')
    print(f'O valor do emprestimo foi de: R${valor_emprestimo}')
    print(f'Valor da parcela: R${valor_parcela:.2f}')
    print(f'O valor do IOF foi de: R${iof:.2f}')
    print(f'Os juros foram de: R${calculo_juros_compostos:.2f}')
    print(f'O valor final foi de: R${valor_final:.2f}')
    print()
    print('=' * 50)

main()