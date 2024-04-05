'''
Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.
'''
def main():
    numero = int(input('Digite um número: '))
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))
    
    while limite_superior < limite_inferior or limite_inferior == limite_superior:
        limite_inferior = int(input('Digite o limite inferior: '))
        limite_superior = int(input('Digite o limite superior: '))
    
        
   
    candidato_a_multiplo = limite_inferior
    
   
    while candidato_a_multiplo <= limite_superior:
        if verificar_multiplo(candidato_a_multiplo, numero):
            print(f'> {candidato_a_multiplo}')
        
        candidato_a_multiplo += 1

def  verificar_multiplo(candidato, numero):
    return candidato % numero == 0


main()