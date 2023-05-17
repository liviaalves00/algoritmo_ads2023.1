'''
Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou quarto) em que o ângulo se localiza.
'''
def main():
	#Entrada
	angulo = float(input('Digite um angulo entre 0° e 360°: '))
	
	#Processamento
	verificacao_quadrante = verificar_quadrante(angulo)
	
	#Saída
	print(verificacao_quadrante)
		
def verificar_quadrante(angulo):
	if angulo <= 90 :
		return 'Primeiro Quatrante'
	if angulo <= 180:
		return 'Segundo Quadrante'
	if angulo <= 270:
		return 'Teceiro Quadrante'
	else:
		return 'Quarto Quadrante'
	
main()