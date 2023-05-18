#G2 MEU DINHEIRINHO
def main():
    # Entrada
    valor_hora = float(input('Valor hora: '))
    nome_professor = input('Digite o nome do Professor: ')
    horas_semanais = int(input('Quantidade Horas Semanais: '))
    print('Qualificação:\nE -> para Especialização\nM -> para Mestrado\nD -> para Doutorado\n')
    qualificacao = str(input('Digite a qualificação: '))
    experiencia_prof_meses = int(input('Tempo de Experiência (meses): '))
    quantidade_filhos = int(input('Quantidade filhos (menores de 6 anos): '))
    valor_plano_saude = float(input('Valor Plano de Saúde: '))

    # Processamento
    valor_hora_professor = calcular_hora_professor(valor_hora, qualificacao, experiencia_prof_meses)
    salario_semanal = valor_hora_professor * horas_semanais
    salario_base_mensal = calcular_salario_base(valor_hora_professor, horas_semanais)
    auxilio_creche = calcular_auxilio_creche(quantidade_filhos)
    ressarcimento_saude = calcular_ressarcimento_saude(valor_plano_saude)
    auxilio_combustivel = calcular_auxilio_combustivel(horas_semanais)
    salario_bruto = salario_base_mensal + auxilio_creche + ressarcimento_saude + auxilio_combustivel
    previdencia = calcular_previdencia(salario_base_mensal)
    imposto_renda = calcular_imposto_renda(salario_base_mensal, previdencia)
    descontos_totais = previdencia + imposto_renda
    salario_liquido = salario_bruto - descontos_totais

    # Saída
    mostrar_resultados(nome_professor, valor_hora_professor, salario_semanal, salario_base_mensal, auxilio_creche, ressarcimento_saude, auxilio_combustivel, salario_bruto, previdencia, imposto_renda, descontos_totais, salario_liquido)

def calcular_hora_professor(valor_hora, qualificacao, experiencia_meses):
    novo_valor = valor_hora
    acrescimo_qualificacao = novo_valor * 0.20
    if qualificacao == 'M':
        acrescimo_qualificacao = novo_valor * 0.30
    elif qualificacao == 'D':
        acrescimo_qualificacao = novo_valor * 0.50
    novo_valor += acrescimo_qualificacao
    anos_experiencia = experiencia_meses / 12
    anos_inteiros = int(anos_experiencia)
    meses_nao_inteiros = experiencia_meses % 12

    if meses_nao_inteiros > 6:
        anos_inteiros += 1
    percetual_experiencia = 5 * anos_inteiros
    acrescimo_experiencia = novo_valor * percetual_experiencia / 100
    novo_valor += acrescimo_experiencia
    return novo_valor

def calcular_salario_base(valor_hora_professor, horas_semanais):
    salario = (valor_hora_professor * horas_semanais) * 4.5
    return salario

def calcular_auxilio_creche(quantidade_filhos):
    return quantidade_filhos * 700

def calcular_ressarcimento_saude(valor_plano_saude):
    if valor_plano_saude <= 1000:
        return valor_plano_saude * 0.50
    else:
        return 500

def calcular_auxilio_combustivel(horas_semanais):
    blocos_aula = horas_semanais // 8
    valor = blocos_aula * 30
    return valor

def calcular_previdencia(salario):
    if salario <= 1302:
        return salario * (7.5 / 100)
    elif salario <= 2500:
        return salario * 0.09
    elif salario <= 3900:
        return salario * 0.12
    elif salario <= 7500:
        return salario * 0.14
    else:
        return salario * 0.16

def calcular_imposto_renda(salario, previdencia):
    valor = salario - previdencia
    parcela = valor - 5000
    imposto = 0
    if parcela > 0:
        imposto = parcela * (27.5 / 100)
    return imposto

def mostrar_resultados(nome_professor, valor_hora_professor, salario_semanal, salario_base_mensal, auxilio_creche, ressarcimento_saude, auxilio_combustivel, salario_bruto, previdencia, imposto_renda, total_descontos, salario_liquido):
    print(f"{nome_professor}")
    print(f"Valor/hora do Professor: {valor_hora_professor:.2f}")
    print(f"Salário Base Semanal: {salario_semanal:.2f}")
    print(f"Salário Base Mensal: {salario_base_mensal:.2f}")
    print(f"Auxílio Creche: {auxilio_creche:.2f}")
    print(f"Ressarcimento Saúde: {ressarcimento_saude:.2f}")
    print(f"Auxílio Combustível: {auxilio_combustivel:.2f}")
    print(f"Salário Bruto: {salario_bruto:.2f}")
    print(f"Previdência: {previdencia:.2f}")
    print(f"Imposto de Renda: {imposto_renda:.2f}")
    print(f"Total Descontos: {total_descontos:.2f}")
    print()
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

main()
