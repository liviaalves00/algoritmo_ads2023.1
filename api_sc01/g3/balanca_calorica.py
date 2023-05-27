#BALANÇA CALORICA #G3
from balanca_calorica_features import *

def main():
    nome = str(input('Digite seu nome: '))
    sexo = str(input('Digite seu sexo\nM - Maculino \nF - Feminino \n>> ')).upper()
    idade = int(input('Digite sua idade: '))
    peso = int(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    perfil_atividade_fisica = str(input('S - Sedentário \nPA - Pouco Ativo \nA - Ativo \nMA - Muito Ativo \n>> ')).upper()

    necessidade_calorica = calcular_necessidade_calorica(sexo, idade, peso, altura, perfil_atividade_fisica)
    print(f'Necessidade Calórica: {necessidade_calorica}')

    ganhar_perder = str(input('Escolha Ganhar ou Perder peso \nG - Ganhar \nP - Perder \n>> ')).upper()
    quilos = float(input('Quantos quilos deseja ganhar/perder: '))
    semanas = int(input('Em quantas semanas: '))

    quilos_por_semana = calcular_kg_semana(quilos, semanas)
    kcal_por_semana = calcular_kcal_semana(quilos_por_semana)
    gramas_por_dia = calcular_gramas_dia(quilos_por_semana)
    necessidade_gramas = calcular_necessidade_gramas(necessidade_calorica)

    if ganhar_perder == 'G':
        definir_dieta = calcular_nova_dieta_ganhar(ganhar_perder, quilos_por_semana, semanas, kcal_por_semana, gramas_por_dia, necessidade_gramas)
        print(definir_dieta)
    if ganhar_perder == 'P':
        definir_dieta = calcular_nova_dieta_perder(ganhar_perder, quilos_por_semana, semanas, kcal_por_semana, gramas_por_dia, necessidade_gramas)
        print(definir_dieta)

    motivacao(semanas)
        
main()