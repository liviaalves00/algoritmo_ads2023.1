def main():
	numero = int(input('Digite um numero entre 0 e 100: '))
	
	numero_primo = calcular_num_primo(numero)

	print(numero_primo)
	
def calcular_num_primo(num):
	if (num + 2) % 2 == 0:
		return '{} nao é primo'.format(num)
	else:
	 return '{} é primo'.format(num)
	 
	 
	
main()