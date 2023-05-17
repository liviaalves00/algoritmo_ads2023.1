def main():
	lado1 = float(input('Digite o primeiro lado: '))
	
	lado2 = float(input('Digite o segundo lado: '))
	
	lado3 = float(input('Digite o terceiro lado: '))
	
	verificacao_lados = verificar_lado(lado1, lado2, lado3)
	verificacao_triangulo = verificar_triangulo(lado1, lado2, lado3)
	
	print(verificacao_lados)
	
	print(verificacao_triangulo)

def verificar_lado(l1, l2, l3):
	if l1 + l2 < l3:
		return 'LADOS VALIDOS'
	else:
		return 'LADOS INVALIDOS'
	
def verificar_triangulo(a, b, c):
	if a and b and c != 0:
		if a == b and a == c and b ==c:
			return 'EQUILATERO'
		elif a == b or a == c or b == c:
			return 'ISOCELES'
		else:
			return 'ESCALENO'
	
main()