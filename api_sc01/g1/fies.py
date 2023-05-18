#G1 FIES
#Nova skill: usar if else em uma linha :)

def main():
    # Entrada
    valor_mensalidade = float(input('Mensalidade: '))
    duracao_anos = int(input('Duração do curso(anos): '))
    selic = float(input('Taxa SELIC: ')) / 100
    salario_minimo = float(input('Salário Mínimo: '))
    renda_familiar = float(input('Renda Familiar: '))
    quantidade_membros_familia = int(input('Quantidade de Membros Família: '))
    ano_inicio = int(input('Ano de início: '))
    semestre_inicio = int(input('Semestre  de início: '))

    duracao_meses = duracao_anos * 12

    # Processamento
    apto_fies = verificar_aptidao(renda_familiar, quantidade_membros_familia, salario_minimo)
    valor_financiado = calcular_valor_curso(duracao_anos, valor_mensalidade)
    juros_totais = calcular_juros_financiamento(valor_financiado, selic, renda_familiar, quantidade_membros_familia, duracao_anos, salario_minimo)
    total_a_pagar = valor_financiado + juros_totais
    taxas_durante_curso_carencia = calcular_taxa_curso(duracao_meses)
    valor_parcela = calcular_parcela(total_a_pagar, taxas_durante_curso_carencia, duracao_meses)
    renda_minima_pos_curso = valor_parcela * 10

    inicio_pagamento = calcular_inicio_pagamento(ano_inicio, semestre_inicio, duracao_meses)
    final_pagamento = calcular_final_pagamento(ano_inicio, semestre_inicio, duracao_meses)

    # Saída
    mostrar_resultados(apto_fies, valor_financiado, juros_totais, total_a_pagar, taxas_durante_curso_carencia,valor_parcela, duracao_meses, renda_minima_pos_curso, inicio_pagamento, final_pagamento)
    

def verificar_aptidao(renda_familiar, qtd_membros_familia, salario_minimo):
    renda_pessoa = renda_familiar / qtd_membros_familia
    return renda_pessoa <= (3 * salario_minimo)

def calcular_valor_curso(duracao, valor_mensalidade):
    duracao_em_meses = duracao * 12
    valor_curso = duracao_em_meses * valor_mensalidade
    return valor_curso

def calcular_juros_financiamento(valor_financiado, selic, renda_familiar, qtd_membros_familia, duracao, salario_minimo):
    renda_pessoa = renda_familiar / qtd_membros_familia
    taxa = calcular_taxa(renda_pessoa, selic, salario_minimo)
    juros = valor_financiado * taxa * duracao
    return juros

def calcular_taxa(renda_pessoa, selic, salario_minimo):
    if renda_pessoa <= (1.5 * salario_minimo):
        return 0.10 * selic
    elif renda_pessoa <= (2 * salario_minimo):
        return 0.15 * selic
    elif renda_pessoa <= (2.5 * salario_minimo):
        return selic * 0.20
    else:
        return selic * 0.25

def calcular_taxa_curso(duracao_meses):
    carencia_meses = 18
    valor_taxa_mes = 150 / 3
    return (duracao_meses + carencia_meses) * valor_taxa_mes

def calcular_parcela(total_a_pagar, taxas_durante_curso_e_carencia, duracao_meses):
    parcela = (total_a_pagar - taxas_durante_curso_e_carencia) / (duracao_meses * 4)
    return parcela

def calcular_inicio_pagamento(ano_inicio, semestre_inicio, duracao_meses):
    carencia_em_meses = 18
    meses_semestre_inicio = 0 if semestre_inicio == 1 else 6
    ano_inicio_em_meses = ano_inicio * 12

    inicio_em_meses = ano_inicio_em_meses + meses_semestre_inicio + duracao_meses + carencia_em_meses + 1
    ano_semestre = converter_meses_em_ano_semestre(inicio_em_meses)

    return ano_semestre

def calcular_final_pagamento(ano_inicio, semestre_inicio, duracao_meses):
    carencia_em_meses = 18
    meses_semestre_inicio = 0 if semestre_inicio == 1 else 6
    ano_inicio_em_meses = ano_inicio * 12

    final_em_meses = ano_inicio_em_meses + meses_semestre_inicio + duracao_meses + carencia_em_meses + 1 + (4 * duracao_meses)
    ano_semestre = converter_meses_em_ano_semestre(final_em_meses)
    return ano_semestre

def converter_meses_em_ano_semestre(meses):
    ano = meses // 12
    semestre = 1 if meses % 12 <= 6 else 2
    return f'{ano}/{semestre}'

def mostrar_resultados(apto_fies, valor_financiado, juros_totais, total_a_pagar, taxas_durante_curso_carencia,valor_parcela, duracao_meses, renda_minima_pos_curso, inicio_pagamento, final_pagamento):
    print(f'Verificação para aptidao: {"SIM" if apto_fies else "NÃO"}')
    print(f'Valor a ser Financiado: {valor_financiado:.2f} R$')
    print(f'Juros do Financiamento: {juros_totais:.2f} R$')
    print(f'Total a Pagar: {total_a_pagar:.2f} R$')
    print(f'Taxa: {taxas_durante_curso_carencia:.2f} R$')
    print(f'Parcelamento: {duracao_meses * 4} de R$ {valor_parcela:.2f}')
    print(f'Renda Mínimo: {renda_minima_pos_curso:.2f} R$')
    print(f'Início Pagamento: {inicio_pagamento}')
    print(f'Final Pagamento: {final_pagamento}')

main()