'''
Leia N e escreva todos os números inteiros pares de 1 a N
'''
def main():
	numero = int(input('Digite um número qualquer(N): '))
	try:
		print('Continuando...')
	except:
		print('Digite um número inteiro!!!')
		
	verificar_numero_int_par = verificar_int_par(numero)
	
def verificar_int_par(numero):
	 for numero in range(numero):
	 	 if numero % 2 == 0:
	 	 	print('>', numero)
	 	 	
			
	
main()