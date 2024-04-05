'''
Uma piscina é algo muito legal de ter (um amigo que tem uma). Para evitar transbordar
ao tomar banho na piscina é bom deixar o nível da água com no máximo 85% da capacidade.
Assim uma piscina que comporta 20 mil litros de água é bom botar só 17mil litros.
Considere uma piscina estilo quadrada.
Para encher a piscina ele usará água paga (o valor é cobrado por cada 1000 litros de água,
em partes inteiras. Ou seja, se usar 1 litro já paga por 1000, ao usar 1002 já paga 2 mil litros)
a)Calcule a capacidade máxima da piscina pedindo ao usuário as dimensões de largura,
comprimento e profundidade (em cm). 1 litro é igual a 1000 cm3 .
Uma piscina por exemplo de capacidade → L=100cm x C=100cm x P=100cm → 1000 litros,
e deve ser cheia até 850 litros apenas.
b)Informe até quantos litros é recomendado encher a piscina.
c)Peça ao usuário para informar o valor a ser pago por cada 1000 litros
na concessionária de água de sua cidade, e informe quanto ele gastará para encher sua piscina;
d)Mensalmente é necessário repor 10% da água devido a banho e evaporação,
informe ao usuário também o gasto mensal para manter a piscina no nível ideal.
'''

def main():
    #Entrada
    print('='*10, 'verificação piscina'.upper(), '='*10)
    print()
    largura_piscina = float(input('Digite a largura da psicina: '))
    comprimento_piscina = float(input('Digite o comprimento da psicina: '))
    profundidade_piscina = float(input('Digite o comprimento da psicina: '))

    #Processamento
    capacidade_maxima_piscina = calcular_capacidade_piscina(largura_piscina, comprimento_piscina, profundidade_piscina)

    capacidade_recomendavel = calcular_capacidade_recomendavel(capacidade_maxima_piscina)
    
    valor_a_ser_pago = float(input('Digite o valor valor a ser pago por cada litro: '))

    calculo_valor_a_pagar_por_l = valor_a_ser_pago_por_l(capacidade_recomendavel, valor_a_ser_pago)

    repor_mensalmente = calcular_reposicao_agua(capacidade_recomendavel)

    valor_a_pagar_reposicao = calcular_valor_reposicao(calculo_valor_a_pagar_por_l, repor_mensalmente)

    print()
    print('='*40)
    print(f'Capacidade Máxima da piscina: {capacidade_maxima_piscina} L')
    print(f'Capacidade Recomendável(85%): {capacidade_recomendavel}L')
    print(f'Valor a pagar por litro(R$): {calculo_valor_a_pagar_por_l:.2f}')
    print(f'Quantidade de água para a reposição da piscina: {repor_mensalmente}')
    print(f'Valor a pagar pela reposição de água da piscina: {valor_a_pagar_reposicao:.2f}')
    print('='*40)


def calcular_capacidade_piscina(larg, compri, profun):
    return (larg * compri * profun)

def calcular_capacidade_recomendavel(capacidade):
    return (capacidade * 0.85)

def valor_a_ser_pago_por_l(capacidade_recomendavel, valor_a_ser_pago):
    if valor_a_ser_pago <= 1000:
        return (capacidade_recomendavel * 1)
    else:
        return (capacidade_recomendavel * 2)
     
def calcular_reposicao_agua(agua):
    return agua * 0.10

def calcular_valor_reposicao(valor, repor):
    valor_repor = (repor // 1000) + 1 
    return valor * valor_repor

main()