'''
Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea 
'''
def main():
	#Entrada
	altura = float(input('Digite sua altura: '))
	peso = float(input('Digite seu peso: '))
	
	#Processamento
	imc = (peso / (altura ** 2))
	verificacao_imc = verificar_imc(imc)
	
	#Saída
	print(f'Seu IMC: {imc:.3f}')
	print(verificacao_imc)

def verificar_imc(imc):
	if imc <= 25:
		return 'Normal'
	elif imc <= 30:
		return 'Obeso'
	else:
		return 'Obesidade Mórbida'
		
main()