#G2 CDC OU CONSORCIO
def main():
    # Entrada
    fipe = float(input('Valor Venda: '))
    meses = int(input("Quantas parcelas: "))
    taxa_cdc = float(input("Taxa de Juros: "))
    taxa_administracao = float(input("Taxa de Administração Consórcio: "))

    # Processamento
    argo = 89000
    valor_produto = 185000
    valor_entrada_lance = calcular_entrada(fipe, argo)
    valor_parcelado = valor_produto - valor_entrada_lance
    juros_cdc = calcular_juros(valor_parcelado, taxa_cdc, meses)
    taxa_administracao = calcular_taxa_administracao(valor_produto, taxa_administracao)
    parcela_cdc = calcular_parcela_cdc(valor_parcelado, juros_cdc, meses)
    parcela_consorcio = calcular_parcela_consorcio(valor_parcelado, taxa_administracao, meses)
    melhor_escolha = ''
    escolha = escolher_cdc_consorcio(melhor_escolha, parcela_cdc, parcela_consorcio)
    
    # Saída
    mostrar_resultados(valor_produto, valor_entrada_lance, valor_parcelado, juros_cdc, taxa_administracao, meses, parcela_cdc, parcela_consorcio, escolha)
    
def escolher_cdc_consorcio(melhor_escolha, parcela_cdc, parcela_consorcio):
    if parcela_cdc < parcela_consorcio:
        melhor_escolha = 'CDC'
    elif parcela_consorcio < parcela_cdc:
        melhor_escolha = 'Consórcio'
    else:
        melhor_escolha = 'CDC ou Consórcio'

def calcular_entrada(percentual_fipe, valor):
    entrada = valor * (percentual_fipe/100)
    return entrada

def calcular_juros(valor_parcelado, taxa_cdc, meses):
    juros = valor_parcelado * (taxa_cdc/100) * meses
    return juros

def calcular_taxa_administracao(valor_bem, taxa_admin):
    taxa = valor_bem * (taxa_admin/100)
    return taxa

def calcular_parcela_cdc(valor,juros,  meses):
    novo_valor = valor + juros
    parcela = novo_valor / meses
    return parcela

def calcular_parcela_consorcio(valor,juros,  meses):
    novo_valor = valor + juros
    parcela = novo_valor / meses
    return parcela

def mostrar_resultados(valor_produto, valor_entrada_lance, valor_parcelado, juros_cdc, taxa_administracao, meses, parcela_cdc, parcela_consorcio, escolha):
    print(f"Valor do produto: {valor_produto:.2f}")
    print(f"Entrada/Lance: {valor_entrada_lance:.2f}")
    print(f"Valor a ser Parcelado: {valor_parcelado:.2f}")
    print(f"CDC Juros: {juros_cdc:.2f}")
    print(f"Consórcio Tx Admin: {taxa_administracao:.2f}")
    print(f"CDC: {meses} com parcelas de: {parcela_cdc:.2f}")
    print(f"Consórcio: {meses} com parcelas de: {parcela_consorcio:.2f}")
    print(f"Melhor Escolha: {escolha}")

main()