'''
Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 –
'''
def main():
	#Entrada
	numero1 = int(input('Digite um número: '))
	numero2 = int(input('Digite outro número: '))
	pergunta_calculo = int(input('1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nDigite a operação desejada:  '))
	
	#Processamento
	calcular = calcular_operacoes(pergunta_calculo, numero1, numero2)
	
	#Saída
	print(calcular)

def calcular_operacoes(pergunta, num1, num2):
	if pergunta == 1:
		return (num1 + num2)
	if pergunta == 2:
		return (num1 - num2)
	if pergunta == 3:
		return (num1 * num2)
	if pergunta == 4:
		return (num1 / num2)
	
main()