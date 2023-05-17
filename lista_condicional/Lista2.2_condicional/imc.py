'''
Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea (IMC = peso / altura2). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso (IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).
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