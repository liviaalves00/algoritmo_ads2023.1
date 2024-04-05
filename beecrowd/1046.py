def main():
    # Entrada
    hora_inicial, hora_final = list(map(int, input().split()))

    # Processamento
    calcular_duracao = duracao_eh(hora_inicial, hora_final)
    
    # Saída
    print(calcular_duracao)

def duracao_eh(hora_inicial, hora_final):
    if (hora_inicial < hora_final):
        return f'O JOGO DUROU {hora_final - hora_inicial} HORA(S)'
    else:
         return f'O JOGO DUROU {(24 - hora_inicial) + hora_final} HORA(S)'

main()