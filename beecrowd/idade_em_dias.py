def main():
    idade_dias = int(input())

    anos = calcular_anos(idade_dias)
    meses = calcular_meses(idade_dias)
    dias = calcular_dias(idade_dias)

    print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')

def calcular_anos(idade):
    return idade // 365

def calcular_meses(idade):
    return (idade % 365) // 30

def calcular_dias(idade):
    return (idade % 365) % 30

main()