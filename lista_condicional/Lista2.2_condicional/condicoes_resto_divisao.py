'''
17. Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1 escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4 divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação escreva o quadrado dos números lidos
'''
def main():
	#Entrada
	numero1 = int(input('Digite um número: '))
	numero2 = int(input('Digite outro número: '))
	
	#Processamento 	
	verificar_condicoes = resto_divisao_condicoes(numero1, numero2)
	
	#Saída
	print(verificar_condicoes)
	
def resto_divisao_condicoes(num1, num2):
	resto = num1 % num2
	if resto == 0:
		return f'quadrados numero 1 e numero 2, respectivamente: {num1 ** 2} e {num2 ** 2}'
	if resto == 1:
		return f'Soma: {(num1 + num2 + resto)}'
	if resto == 2:
		if num1 % 2 == 0:
			return f'{num1} é par'
		else:
			return f'{num1} é impar'
		if num2% 2 == 0:
			return f'{num1} é par'
		else:
			return f'{num2} é impar'
	if resto == 3:
			return f'Soma multiplicada pelo numero1: {(num1 + num2) * num1}'
	if resto == 4:
			return f'Soma multiplicada pelo numero1: {(num1 + num2) / num2}'
			
main()
			