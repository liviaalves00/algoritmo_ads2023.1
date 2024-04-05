def main():
    #Entrada
    while True:
        try:
            D = input()
            S = input()
            
        except EOFError:
            return

        #Processamento
        verificar_bacteria = verificar(D, S)

        #Saída
        print(verificar_bacteria)

def verificar(D, S):
    if S in D:
        return 'Resistente'
    else:
        return 'Nao resistente'

main()