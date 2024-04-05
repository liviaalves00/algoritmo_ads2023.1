def main():
    valores = list(map(int, input().split()))
    valores_ordenados = sorted(valores)

    resultado_valores = verificar_valor(valores, valores_ordenados)
    
def verificar_valor(valores, valores_ordenados):
    for valor in valores_ordenados:
        print(valor)
    print()
    for valor in valores:
        print(valor)
main()