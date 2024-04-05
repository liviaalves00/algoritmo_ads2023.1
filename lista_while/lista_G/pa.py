'''
Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
Aritmética que tem por valor inicial A0 e razão R.
'''
def main():
    #Entrada
    termo_pa = float(input('Digiteo termo da PA: '))
    limite_pa = float(input('Digite o limite da PA: '))
    razao_pa = float(input('Digite a razão da PA: '))

    #Processamento
    pa = calcular_pa(termo_pa, limite_pa, razao_pa)

    #Saída
    print(pa)
     
def calcular_pa(termo_pa, limite_pa, razao_pa):
    while termo_pa < limite_pa:
        return termo_pa
    termo_pa += razao_pa 
   
main()