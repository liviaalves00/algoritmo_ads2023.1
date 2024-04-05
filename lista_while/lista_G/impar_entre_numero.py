'''
Leia LimiteSuperior e LimiteInferior e escreva todos os números ímpares entre os limites lidos.
'''
def main():
    #Entrada
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))
   
    #Processamento/Saída
    while limite_inferior <= limite_superior:
      if limite_inferior % 2 != 0:
            print(limite_inferior)
      limite_inferior += 1

main()