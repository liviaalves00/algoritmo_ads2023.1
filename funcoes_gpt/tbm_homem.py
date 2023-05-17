#Cálculo da taxa metabólica basal (TMB)
#São fórmulas matemáticas que levam em consideração fatores como idade, sexo e nível de atividade física para estimar o gasto calórico.
#Fórmula da TMB para homens: TMB = 88,36 + (13.4 x peso) + (4,8 x altura) - (5,7 x idade)

def main():
	#Entrada
	peso = int(input('Digite seu peso: '))
	altura = float(input('Digite sua altura: '))
	idade = int(input('Digite sua idade: '))
	
	#Processamento
	resultado_tbm = calcular_tbm(peso, altura, idade)
	
	#Saída
	print('Cálculo da taxa metabólica basal (TMB) Homem: ',resultado_tbm, 'Kcal')

def calcular_tbm(peso, altura, idade):
	formula_tbm = 88.6 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
	return formula_tbm

main()