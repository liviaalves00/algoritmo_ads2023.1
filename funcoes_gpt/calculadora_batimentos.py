#"Calculadora de Batimentos Cardíacos"
#Crie um programa que receba a idade de uma pessoa e calcule a sua frequência cardíaca máxima, que é dada pela fórmula 220 menos a idade. O programa deve então calcular a faixa de batimentos cardiacos ideais para atividades físicas moderadas e intensas, que correspondem a 50-70% e 70-85% da frequência cardíaca máxima, respectivamente. Os resultados devem ser exibidos na tela. 

def main():
	#Entrada
	idade = int(input('Digite sua idade: '))
	
	#Processamento
	freq_cardiaca_max = calcular_freq_cardiaca_max(idade)
	
	freq_batimentos_cardiaco_mod_max = calcular_freq_batimentos_mod_max(idade)
	
	freq_batimentos_cardiaco_mod_min = calcular_freq_batimentos_mod_min(idade)
	
	freq_batimentos_cardiaco_intenso_max = calcular_freq_batimentos_intenso_max(idade)
	
	freq_batimentos_cardiaco_intenso_min = calcular_freq_batimentos_intenso_min(idade)
	
	#Saída
	print('Frequencia cardiaca maxima: ', freq_cardiaca_max, 'bpm')
	
	print('Frequencia Moderada Maxima: ', freq_batimentos_cardiaco_mod_max,'bpm')
	
	print('Frequencia Moderada Minima: ', freq_batimentos_cardiaco_mod_min,'bpm')
	
	print('Frequencia Intensa Maxima: ', freq_batimentos_cardiaco_intenso_max,'bpm')
	
	print('Freaquencia Intensa Minima: ', freq_batimentos_cardiaco_intenso_min, 'bpm')

def calcular_freq_cardiaca_max(idade):
	freq_car_max = 220 - idade
	return freq_car_max
	
def calcular_freq_batimentos_mod_max(idade):
	freq_car_mod_max = calcular_freq_cardiaca_max(idade)
	freq_bat_mod_max = 0.7 * freq_car_mod_max
	return freq_bat_mod_max
	
def calcular_freq_batimentos_mod_min(idade):
	freq_car_mod_min = calcular_freq_cardiaca_max(idade)
	freq_bat_mod_min = 0.5 * freq_car_mod_min
	return freq_bat_mod_min
	
def calcular_freq_batimentos_intenso_max(idade):
	freq_car_intenso_max = calcular_freq_cardiaca_max(idade)
	freq_bat_intenso_max = 0.85 * freq_car_intenso_max
	return freq_bat_intenso_max
	
def calcular_freq_batimentos_intenso_min(idade):
	 freq_car_intenso_min = calcular_freq_cardiaca_max(idade)
	 freq_bat_intenso_min = 0.70 * freq_car_intenso_min
	 return freq_bat_intenso_min
	
main()
	
#moderado maximo e intenso minimo terao os mesmos valores por ambos serem 0.70
	