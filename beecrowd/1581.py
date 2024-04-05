def main():
    try:
        qtd_teste = int(input())
        for i in range(qtd_teste):
            qtd_idiomas = int(input())
            idiomas = []
            for i in range(qtd_idiomas):
                idioma = input()
                idiomas.append(idioma)
            idioma_falado = idioma_diferente(idiomas)
            print(idioma_falado)

    except EOFError:
        return 
    
def idioma_diferente(idiomas):
    idioma_anterior = idiomas[0]
    for i in range(1, len(idiomas)):
        if idioma_anterior == idiomas[i]:
            continue
        else:
            return 'ingles'
    return idiomas[0]

main()