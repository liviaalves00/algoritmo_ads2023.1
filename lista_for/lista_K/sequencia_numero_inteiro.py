'''
Leia N e escreva todos os números inteiros de 1 a N.
'''
def main():
	numero = int(input('Digite um número qualquer(N): '))
	
	verificar_numero_int = verificar_int(numero)
		
def verificar_int(numero):
	if numero != float:				
		for numero in range(numero):
			print('>', numero)

main()