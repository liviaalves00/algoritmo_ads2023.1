'''
Leia N e escreva todos os números inteiros pares de 1 a N.
'''
def main():
    #Entrada
    numero = int(input('Digite um número: '))
    contador = 1
    
    #Processamaento/Saída
    while contador <= numero:
      if contador % 2 == 0:
        print(contador)
        
      contador += 1

main()