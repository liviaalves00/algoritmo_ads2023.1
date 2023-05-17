def main():
	numero1 = int(input('Digite um numero: '))
	numero2 = int(input('Digite mais um numero: '))
	numero3 = int(input('Digite outro numero: '))
	
	menor =  numero1
	meio = numero1
	maior = numero1
	
	if numero2 < numero1 and numero2 < numero3:
		menor = numero2
	elif numero2 > numero1 and numero2 > numero3:
		maior = numero2
	else:
		meio = numero2
		
	if numero3 < numero2 and numero3 < numero1:
		menor = numero3
	elif numero3 > numero2 and numero3 > numero1:
		maior = numero3
	else:
		meio = numero3
	
	print('Menor numero: ', menor)
	print('Numero do meio: ', meio)
	print('Numero maior: ', maior)

	
		
main()