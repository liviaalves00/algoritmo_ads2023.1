#Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:
#D= R+S/ 2  R=(A+B)**2 onde S=(B+C)**2

def main():
	#Entrada
	numero_a = int(input('Digite o numero A:'))
	
	numero_b = int(input('Digite o numero B:'))
	
	numero_c = int(input('Digite o numero C:'))
	
	#Processamento
	calculo_formula_d = calcular_formula_d(numero_a, numero_b, numero_c)
	
	#Saída
	print('O resultado da operaçāo D=R+S/2:', calculo_formula_d)
	
def calcular_formula_d(a, b, c):
	formula_d = ((a + b)**2) + ((b + c)**2) / 2
	return formula_d
	
main()

