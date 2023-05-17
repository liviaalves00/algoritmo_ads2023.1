#Cálculo do déficit calórico médio diário para alcançar meta de perda de peso Uma pessoa estabeleceu como meta perder X % do Peso #Corporal em Y semanas. Sabendo que 1 kg de gordura corresponde a cerca de 7700 kcal, calcule o déficit calórico médio diário necessário para alcançar essa meta.
#Pergunte ao usuário qual seu Peso atual, qual sua meta % de redução de Peso e em quantas semanas. Pergunte ainda quanto ele tá disposto a consumir de kcal diariamente.
#Seu objetivo é informar ao usuário qual deve ser seu deficit calórico diário médio e também quanto de exercícios diários ele deve fazer para alcançar esse deficit alvo
#considerando sua ingestão calórica informada.
#Faça simulações manuais para Elaborar o algoritmo. E então, após ter a solução. automatizar via software.

def main():
	#Entrada
	peso_inicial = int(input('Digite seu peso inicial: '))
	
	reducao_percentual = float(input('Valor de redução (%): '))
	
	semanas = float(input('Digite a quantidade de semanas desejada: '))
	
	#Processamento
	peso_reduzido_percentual = calcular_reducao_peso(peso_inicial, reducao_percentual)
	
	diminuir_calorias = calcular_peso_em_calorias(peso_reduzido_percentual)
	
	quantidade_dias = converter_semanas_em_dias(semanas)
	
	deficit_diario = diminuir_calorias / semanas
		
	consumo_diario = float(input('Digite o quanto deseja consumir diariamete(Kcal): '))
	
	gasto_por_dia = consumo_diario + deficit_diario
	
	#Saída
	print('Para atingir sua meta você devera gastar',deficit_diario, 'Kcal')
	print('Voce deverá gastar em atividade fisica: ', gasto_por_dia, 'Kcal')
	
def calcular_reducao_peso(peso_inicial, reducao_percentual):
	peso = peso_inicial * (reducao_percentual/100)
	return peso
	
def calcular_peso_em_calorias(peso_reduzido_percentual):
	calorias = peso_reduzido_percentual * 7700
	return calorias

def converter_semanas_em_dias(semanas):
	conversao = semanas * 7
	return conversao
	
main()	
	
	
	

