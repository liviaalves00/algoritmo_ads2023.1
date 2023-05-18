#G1 CONSÓRCIO

def main():
    #Entrada
    valor_produto = float(input('Digite o valor do produto do consórcio: '))
    prazo = int(input('Prazo: '))
    taxa_administracao = float(input('Taxa Administração: '))
    lance = float(input('Valor do Lance: '))
    manter_prazo_parcela = str(input('Digite sua escolha, manter o prazo ou parcela: '))
    renda_mensal = float(input('Digite sua renda: '))

    #Processamento
    valor_taxa_administracao = calcular_taxa_admin(valor_produto, taxa_administracao)
    valor_total_a_pagar = valor_produto + valor_taxa_administracao
    valor_parcela = calcular_parcela(valor_total_a_pagar, prazo)
    aprovado_consorcio = verificar_aprovacao(valor_parcela, renda_mensal)
    renda_minima = calcular_renda_minima(valor_parcela)
    nova_parcela = valor_parcela
    novo_prazo = prazo

    #Saída
    if lance > 0:
        verificar_prazo_ou_parcela(manter_prazo_parcela,valor_total_a_pagar, prazo, lance, valor_parcela ) #escolha de lance/parcela
        
    if lance > 0:
        mostrar_caso_lance(lance, manter_prazo_parcela, nova_parcela, novo_prazo) #se foi para o caso de lance
      
    mostrar_resultados(valor_total_a_pagar, valor_taxa_administracao, prazo, valor_parcela, aprovado_consorcio, renda_minima) #saída final

def calcular_parcela(valor_total, prazo):
    parcela = valor_total / prazo
    return parcela

def calcular_taxa_admin(valor_bem, taxa_admin):
    return valor_bem * (taxa_admin / 100)

def verificar_aprovacao(valor_parcela, renda_mensal):
    return valor_parcela <= renda_mensal * (30/100)

def calcular_renda_minima(valor_parcela):
    return (valor_parcela / 30) * 100

def calcular_parcela_apos_lance(valor_total, prazo_meses, lance):
    novo_valor_total = valor_total - lance
    nova_parcela = novo_valor_total / prazo_meses
    return nova_parcela

def calcular_prazo_apos_lance(valor_total, lance, valor_parcela):
    novo_valor_total = valor_total - lance
    novo_prazo = (novo_valor_total / valor_parcela)
    return novo_prazo

def mostrar_resultados(valor_total_a_pagar, valor_taxa_admin, prazo, valor_parcela, aprovado, renda_minima):
    print(f"Valor Total R$ {valor_total_a_pagar:.2f}")
    print(f"Valor Taxa de Administração R$: {valor_taxa_admin:.2f}")
    print(f"> {prazo} parcelas de R$ {valor_parcela:.2f}")
    print(f"> Situação Aprovação: {'sim' if aprovado else 'nao'}")
    print(f"> Renda Mínima R$ {renda_minima:.2f}")

def verificar_prazo_ou_parcela(manter_prazo_parcela,valor_total_a_pagar, prazo, lance, valor_parcela):
    if manter_prazo_parcela == "prazo":
        nova_parcela = calcular_parcela_apos_lance(valor_total_a_pagar, prazo, lance)
    elif manter_prazo_parcela == "parcela":
        novo_prazo = calcular_prazo_apos_lance(valor_total_a_pagar, lance, valor_parcela)

def mostrar_caso_lance(lance, manter_prazo_parcela, nova_parcela, novo_prazo):
    print()
    print('LANCE:')
    print(f"Seu lance foi no valor de R$ {lance:.2f}")
    print(f"Você escolheu manter: '{manter_prazo_parcela}'")
    print(f"Nova Parcela: R$ {nova_parcela:.2f}")
    print(f"Novo Prazo: {novo_prazo} meses")

main()
