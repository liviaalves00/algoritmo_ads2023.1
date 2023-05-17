def main():
	numero = int(input('Digite um numero de dois digitos: '))
	
	verificar_d = (numero % 100) // 10
	
	verificar_u = (numero% 100) % 10
	
	verificacao = verificar(verificar_d, verificar_u)
	
	print('Dezena:', verificar_d, 'Unidade:' ,verificar_u)
	print(verificacao)
	
def verificar(dezena, unidade):
	if dezena == unidade:
		return 'dezena igual a unidade'
	else:
		return 'dezena diferente da unidade'
		
main()