def main():
	print('-'*5, 'Soma triangulo: 180°', '-'*5)
	
	angulo1 = float(input('Digite o primeiro angulo: '))
	
	angulo2 = float(input('Digite o segundo angulo: '))
	
	angulo3 = float(input('Digite o terceiro angulo: '))

	verificacao_triangulo = verificar_triangulo(angulo1, angulo2, angulo3)

	print(verificacao_triangulo)

def verificar_triangulo(ang1, ang2, ang3):
		if ang1 or ang2 or ang3 == 0:
			return 'pelo menos um angulos invalido, triangulo inexistente'
		elif ang1 and ang2 and ang3 < 90:
			return ' TRIANGULO ACUTANGULO' 
		elif ang1 or ang2 or ang3 == 90:
			return 'TRIANGULO RETANGULO'
		else:
			return 'TRIANGULO ACUTANGULO'
		
		
main()