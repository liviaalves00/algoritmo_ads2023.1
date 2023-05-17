def main():
	dia = int(input('Digite o dia desejado: '))
	mes = int(input('Digite o mes desejado: '))
	ano = int(input('Digite o ano desejado: '))
	
	verificacao_data = verificar_data(dia, mes,ano)
	print(verificacao_data)
	
def verificar_data(dia, mes, ano):
	if dia <=31 and mes <=12 and ano >0:
		return 'Data valida'
	else:
		return 'Dia/Mes/Ano invalidos'

main()