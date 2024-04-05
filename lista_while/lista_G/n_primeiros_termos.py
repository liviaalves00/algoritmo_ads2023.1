'''
Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).
'''
def main():
    # Entrada
    numero_inicial = int(input('Digite um número: '))

    # Processamento
    verificar_sequencia = sequencia(numero_inicial)

    # Saída
    print(verificar_sequencia)

def sequencia(numero_inicial):
    numero = 0
    sequencia = []
    numero_a_somar = 1

    while numero_inicial >= 0:
        while numero_a_somar <= numero_inicial:
            numero = numero + numero_a_somar
            numero_a_somar += 1

            sequencia.append(numero)
        numero_inicial -= 1

    return sequencia

main()
