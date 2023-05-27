import random

def calcular_necessidade_calorica(sexo, idade, peso, altura, paf):
    if sexo == 'M':
        if paf == 'S':
            return  662 - (9.53 * idade) + 1 * (15.91 * peso) + (539.6 * altura) //1000
        elif paf == 'PA':
            return 622 - (9.53 * idade) + 1.11 * (15.91 * peso) + (539.6 * altura) // 1000
        elif paf == 'A':
            return 622 - (9.53 * idade) + 1.25 * (15.91 * peso) + (539.6 * altura) // 1000
        elif paf == 'MA':
            return 622 - (9.53 * idade) + 1.48 * (15.91 * peso) + (539.6 * altura) // 1000
    else:
        if paf == 'S':
            return  354 - (6.91 * idade) + 1 * (15.91 * peso) + (726 * altura) // 1000
        elif paf == 'PA':
            return 354 - (6.91 * idade) + 1.12 * (15.91 * peso) + (726 * altura) // 1000
        elif paf == 'A':
            return 354 - (6.91 * idade) + 1.27 * (15.91 * peso) + (726 * altura) // 1000
        elif paf == 'MA':
            return 354 - (6.91 * idade) + 1.45 * (15.91 * peso) + (726 * altura) // 1000

def calcular_kg_semana(quilos, semanas):
    return quilos // semanas

def calcular_kcal_semana(quilo):
    return (quilo * 7700)

def calcular_gramas_dia(quilo):
    return (quilo * 1000) // 7

def calcular_necessidade_gramas(necessidade):
    return necessidade // 7700

def calcular_nova_dieta_ganhar(ganhar_perder, quilos_por_semana,semanas,  kcal_por_semana, gramas_por_dia, necessidade_gramas):
    if ganhar_perder == 'G':
        return f'Ingerir: {quilos_por_semana} Kg \nE: {kcal_por_semana:.1f} Kcal a mais.'
    dieta = gramas_por_dia + necessidade_gramas
    proteina = dieta * 0.4
    carboidrato = dieta * 0.4
    gorduras = dieta * 0.2
    return f'Dieta para proximass {semanas}semanas: \nProteina: {proteina}; \nCarboidrato: {carboidrato} \nGorduras: {gorduras}'
    
def calcular_nova_dieta_perder(ganhar_perder, quilos_por_semana, semanas, kcal_por_semana, gramas_por_dia, necessidade_gramas):
    if ganhar_perder == 'P':
        return f'Ingerir: {quilos_por_semana} Kg \nE: {kcal_por_semana} Kcal a mais.'
    dieta = gramas_por_dia - necessidade_gramas
    proteina = dieta * 0.4
    carboidrato = dieta * 0.4
    gorduras = dieta * 0.2
    return f'Dieta para proximass {semanas}semanas: \nProteina: {proteina}; \nCarboidrato: {carboidrato} \nGorduras: {gorduras}'

def motivacao(semanas):
    if semanas > 1:
       print("Cuidado para não perder a rotina")
    else:
        print("voce está indo muito bem", "continue assim")

#nao gostei deste código nao :/
#ja sao 02:06am