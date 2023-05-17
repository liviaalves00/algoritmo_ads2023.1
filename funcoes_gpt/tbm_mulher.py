#Cálculo da taxa metabólica basal (TMB)
#São fórmulas matemáticas que levam em consideração fatores como idade, sexo e nível de atividade física para estimar o gasto calórico.
#fórmula da TMB para mulheres: TMB = 447,6 + (9,2 x peso) + (3,1 x altura) - (4.3 x idade)

def main():
	#Entrada
	peso = int(input('Digite seu peso: '))
	altura = float(input('Digite sua altura: '))
	idade = int(input('Digite sua idade: '))
	
	#Processamento
	resultado_tbm = calcular_tbm(peso, altura, idade)
	
	#Saída
	print('Cálculo da taxa metabólica basal (TMB) Feminino: ',resultado_tbm, 'Kcal')

def calcular_tbm(peso, altura, idade):
	formula_tbm = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
	return formula_tbm

main()