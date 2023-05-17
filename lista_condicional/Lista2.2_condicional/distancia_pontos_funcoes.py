#Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano,
#pontol (x1,y1) e ponto2 (x2,y2), escreva a distância entre eles, conforme fórmula abaixo.
#d = raizq(x2-x1)**2 + (y1-y2)**2

def main():
	#Entrada
	x1 = int(input('Digite a coordenada x do primeiro ponto: ' ))
	
	y1 = int(input('Digite a coordenada y do primeiro ponto: ' ))

	x2 = int(input('Digite a coordenada x do primeiro ponto: ' ))

	y2 = int(input('Digite a coordenada do y do primeiro ponto: ' ))
	
	#Processamento
	calculo_distancia_pontos = calcular_distancia_pontos(x1, y1, x2, y2)
	
	#Saída
	print ( 'O resultado da  distância entre os pontos é:' , calculo_distancia_pontos)

def calcular_distancia_pontos(x2, x1, y2, y1):
	formula = (( x2  -  x1 ) **  2  + ( y2  -  y1 ) **  2 ) **  0,5
	return formula

main()
