'''
Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.
'''
def main():
    #Entrada 
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))
    
    #Processaemnto/Saída
    for i in range(limite_inferior, limite_superior):
        if i != 0 and i != 1:
            if i == 2 or i == 3 or i == 5 or i == 7:
                print(i)
            else:
                if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                    continue
                else:
                    print(i)

main()