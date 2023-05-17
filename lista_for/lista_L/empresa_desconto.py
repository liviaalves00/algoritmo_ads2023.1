'''
Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de
horas trabalhadas e o seu no de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$
40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR.
Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N
funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada imposto e o salário
líquido do funcionário.
'''
def main():
    #Entrada
    ficha = int(input('Digite o numero de fichas: '))
    
    #Processamento
    for i in range(ficha):
        codigo = int(input('Digite o código: '))
        horas_trabalhadas = int(input('Digite o número de horas trabalhadas: '))
        numero_dependentes = int(input('Digite o número de depententes: '))

        pagamento_hora = horas_trabalhadas * 12
        pagamento_dependente = numero_dependentes * 40
        salario = pagamento_hora + pagamento_dependente
    
        imposto_renda = verificar_ir(salario)
        inss = verificar_inss(salario)

        #Saída
        print()
        print(f'Salario: {salario}')
        print(f'Desconto do IR: {imposto_renda}')
        print(f'Desconto do INSS: {inss}')

def verificar_ir(salario):
    return salario * (8.5 / 100)

def verificar_inss(salario):
    return salario * (5 / 100)


main()