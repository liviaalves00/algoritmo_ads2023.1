# Calculadora de Água 
#Crie um programa que receba o peso e a #atividade física diária de uma pessoa 
#e calcule a quantidade de água que ela deve beber por dia. 
#A quantidade de água recomendada é de 35 ml por quilo de peso para pessoas com atividade física moderada, 
#e 45 ml por quilo de peso para pessoas com atividade física intensa. 
#O resultado do cálculo deve ser exibido na tela.

def main():
	#Entrada
	peso = int(input('digite o seu peso: '))
	atividade_fisica = str(input('digite o tipo de atividade fisica(moderada/intensa): '))
	atividade_moderada = calcular_agua_moderada(peso)
	atividade_intensa = calcular_agua_intensa(peso)
	
	#Processsamento/Saída
def calcular_agua_moderada(peso):
	qtd_agua_mod = (peso*100) // 35
	print('Agua para atividade moderada: ', qtd_agua_mod, 'ml')
	return qtd_agua_mod

def calcular_agua_intensa(peso):
	qtd_agua_intensa = (peso*100) // 45
	print('Agua para atividade intensa: ', qtd_agua_intensa, 'ml')
	return qtd_agua_intensa
	

main()