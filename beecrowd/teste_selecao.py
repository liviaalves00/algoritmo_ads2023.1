def main():
    a, b, c, d = list(map(int, input().split()))

    verificar_validacao = validacao(a, b, c, d)

    print(verificar_validacao)

def validacao(a, b, c, d):
    if b > c and d > a and c + d > a + b and  c > 0 and d > 0 and a % 2 == 0:
        return ('Valores aceitos')
    else:
        return ('Valores nao aceitos')

main()