#CREDIARIO #G3
def main():
    valor_iphone = float(input('Digite o valor do Iphone (R$): '))
    forma_pagamento = menu_pagamento()
    forma_pagamento = int(input(forma_pagamento))

    if forma_pagamento == 4:
        entrada_credito = float(input('Digite a entrada: '))
        parcela_credito = int(input('Em quantas parcelas: '))

        c_credito = calcular_pagamento_credito(entrada_credito, valor_iphone, parcela_credito)
        print()
        print(c_credito)

    if forma_pagamento == 3:
        c_debito = calcular_pagamento_debito(valor_iphone)
        print()
        print(c_debito)
    
    if forma_pagamento == 2:
        especie = calcular_pagamento_especie_pix(valor_iphone)
        print()
        print(especie)
    
    if forma_pagamento == 1:
        pix = calcular_pagamento_especie_pix(valor_iphone)
        print()
        print(pix)
   
def menu_pagamento():
    opcao = 'Escolha a forma de pagamento'
    opcao += '\n1 - PIX'
    opcao += '\n2 - Espécie'
    opcao += '\n3 - Cartão de Débito'
    opcao += '\n4 - Cartão de Crédito'
    opcao += '\n>> '

    return opcao

def  calcular_pagamento_credito(entrada, iphone, parcela):
    valor_juros = (iphone - entrada) + (iphone * (0.0399)) + (0.015 * parcela) * parcela
    valor_total = iphone + valor_juros
    return f'Juros: {valor_juros}\nTotal a pagar: {valor_total}'

def calcular_pagamento_debito(iphone):
    valor_total = (iphone * 0.9)
    desconto = (iphone * 0.1)
    return f'Total a pagar: {valor_total} \nEconomia de (R$): {desconto}'

def calcular_pagamento_especie_pix(iphone):
    valor_total = (iphone * 0.85)
    desconto = (iphone * 0.15)
    return f'Total a pagar: {valor_total} \nEconomia de (R$): {desconto}'

main()