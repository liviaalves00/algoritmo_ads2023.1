''' 
Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior 
ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média 
final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve 
escreva “Reprovado”.
'''
def main():
	nota1 = float(input('Digite a primeira nota: '))
	nota2 = float(input('Digite a segunda nota: '))
	
	verificar_situacao = situacao(nota1, nota2)
	
	print(verificar_situacao)
	
def situacao(nota1, nota2):
	media = (nota1 + nota2) / 2
	if media >= 7:
		return 'Aprovado'
	else: 
		print('Você ficou de prova final hein....')
		print()
		nota_final = float(input('Digite a nota da prova final: '))
		if nota_final >= 5:
			return 'Aprovado'
		else:
			return 'Reprovado'
	
main()