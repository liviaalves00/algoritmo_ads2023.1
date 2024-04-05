'''
Em 2021 o Brasil voltou a enfrentar crise na matriz energética devido ao baixo nível das águas nos reservatórios das hidrelétricas brasileiras.
Devido a isso os consumidores deverão arcar com custos extras (bandeira) para bancar outras matrizes energéticas, como usinas termoelétricas.
Neste mês de Junho a bandeira estabelecida pelo governo federal foi a Vermelha Patamar 2, que significa que a cada 100 KWh de consumo
será acrescido uma taxa extra de R$ 8,00.
O Cálculo da energia elétrica para o consumidor final é feito baseado em KWh e em faixas. 
Valores hipotéticos: 
    Consumo de até 30KWh isento de tarifa. 
    Até 100 KWh será cobrado R$ 0,59 por cada um cada de todo os KWh consumidos;
    acima de 100KWh o valor de R$ 0,75 por cada um de todos os KWh consumidos. 
Sobre o valor tarifado/apurado são 25% de ICMS e 15% de PIS/CONFIS. 
A taxa de iluminação pública é cobrada apenas para os consumidores que passarem de 80KWh por mês,
e custa 6% do valor tarifado (antes do impostos).
Considerando os dados acima construa um software que receba dois dados: 
Leitura Atual e Leitura Anterior do medidor de energia e faça todo o cálculo do "Talão de Energia" conforme detalhado acima. 
Como saída apresente os dados que compõem assim como o valor total a ser pago.
Exemplo: 
    Consumo 000 KWh
    Valor Faturado R$ 0,00
    Bandeira R$ 0,00 (x bandeiras)
    ICMS R$ 0,00
    PIS/CONFIS
    Taxa Iluminação R$ 0,00
'''
def main():
    print()
    print('=' * 15, 'LUX S.A', '=' * 15)
    print()

    #Entrada
    leitura_atual = int(input('Digite a quantidade de KWh atual: '))
    leitura_anterior = int(input('Digite a quantidade de KWh anterior: '))

    #Processamento
    consumo_atual = leitura_atual - leitura_anterior

    verificacao_tarifa = verificar_tarifa(consumo_atual)
    verificacao_bandeira = verificar_bandeira(consumo_atual)
    verificacao_icms = verificar_icms(verificacao_tarifa)
    verificacao_pis = verificar_pis(verificacao_tarifa)
    taxa_iluminacao = verificar_taxa_iluminacao(verificacao_tarifa)

    #Saída
    mostrar_resultados(consumo_atual, verificacao_tarifa, verificacao_bandeira, verificacao_icms, verificacao_pis, taxa_iluminacao)

def verificar_tarifa(consumo):
    if consumo <= 30:                             
        return 0
    elif consumo <= 100:                         
        return consumo * 0.59
    else:
        return consumo * 0.75                     
    
def verificar_bandeira(consumo):
    bandeira = 8   #significa que a cada 100 KWh de consumo será acrescido uma taxa extra de R$ 8,00.
    if consumo < 100:
        return 0
    return (consumo // 100) * bandeira
    
def verificar_icms(tarifa):                    
    return tarifa * 0.25

def verificar_pis(tarifa):
    return tarifa * 0.15

def verificar_taxa_iluminacao(consumo):
    if consumo <= 80:
        return 0
    return consumo * 0.06

def mostrar_resultados(consumo, tarifa, bandeira, icms, pis, iluminacao):
    valor_total = tarifa + bandeira + icms + pis
    print('=' * 40)
    print()
    print('-' * 15, 'LUX S.A', '-' * 15)
    print()
    print(f'Consumo Atual: {consumo} KWh.')
    print(f'Valor da Tarifa: R$ {tarifa}.')
    print(f'Bandeira: R$ {bandeira}.')
    print(f'ICMS: R$ {icms}.')
    print(f'PIS: R$ {pis}.')
    print(f'Taxa de Iluminação: R$ {iluminacao}.')
    print(f'Valor total: R$ {valor_total}.')
    print()
    print('=' * 40)

main()