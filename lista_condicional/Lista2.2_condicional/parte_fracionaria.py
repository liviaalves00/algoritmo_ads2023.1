'''
Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso contrario, é arredondado para o inteiro imediatamente inferior.
'''
def main():
	#Entrada
	numero = float(input('Digite um número fracionado: '))
	
	#Processamento
	pegar_parte_fracao = numero -  int(numero) #Tirar a parte fracionaria do numero para poder tratar as condicoes
		
	verificar_parte_fracao = condicao_fracao(numero, pegar_parte_fracao)
	
	#Saída
	print(verificar_parte_fracao)


def condicao_fracao(numero, parte_fracao):
	if parte_fracao >= 0.5:
		return int(numero) + 1
	else:
		return int(numero) - 1
	
main()