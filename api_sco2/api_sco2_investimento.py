'''
Mariana resolveu investir de parte de seu salário (um pedaço(R$) inferior a 30%) de forma fixa mensal;
O investimento escolhido rende mensalmente a uma taxa de juros de 0,01% até 1,00 % bre o saldo do mês.
Mariana tem um dado objetivo com este investimento.
Pergunte a ela qual o objetivo e de quanto ela precisa para realizá-lo. Além disso, peça o salário,
quanto(%) ela pretende investir mensalmente e qual a taxa de juros do investimento escolhido.
Em seguida mostre em quantos meses ela atingirá o objetivo.
Se for acima de 12 meses mostre-o em anos e meses.
A cada mês você deve atualizar o saldo primeiro com o aporte (depósito de valor do salário)
e depois aplicar os créditos dos juros sobre esse novo saldo.
Faça isso enquanto o objetivo não for alcançado, contando os meses para serem exibidos como se pede.
'''
def main():
    qual_objetivo = input('Olá, Mariana!\nInforme qual o seu objetivo com este investimento: ')
    valor_necessario_objetivo = float(input('Digite o valor necessário para realizar o objetivo: ' ))
    salario = float(input('Digite seu salário: '))
    quanto_investir = float(input('Informe quanto pretende investir: '))
    taxa_juros = float(input('Informe a taxa de juros para este investimento: '))
    saldo = (salario * quanto_investir) / 100
    contador_meses = 0

    parte_salario_porcento = parte_salario(salario)
    
    while saldo <= valor_necessario_objetivo:
        print('objetivo:', valor_necessario_objetivo)
        print('Dinheiro rendendo:', saldo)
        print(tempo)
        juros = saldo * taxa_juros / 100
        saldo += juros
        contador_meses += 1
        #return contador_meses
    tempo = mostrar_tempo(contador_meses)

    print(saldo)
    mostrar_resultado(parte_salario_porcento, tempo)
    
def parte_salario(salario):
    return (salario * 0.30)

def mostrar_tempo(contador):
    if contador < 12:
        return f'{contador} meses'
    else:
        anos = contador // 12
        meses = meses % 12
        return f'{anos} anos e {meses} meses'

def mostrar_resultado(parte_salario, tempo):
    print(f'O valor investido(30%) foi de: {parte_salario}')
    print(f'O tempo para concluir o objetivo é de: {tempo}')
  
main()