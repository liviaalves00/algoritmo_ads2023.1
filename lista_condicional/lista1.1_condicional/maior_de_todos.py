#Leia 3 (três) números,
#verifique e escreva o maior entre os números lidos.

def main():
    numero1 = float(input('Digite o primeiro numero: '))

    numero2 = float(input('Digite o segundo numero: '))

    numero3 = float(input('Digite o teceiro numero: '))

    verificacao_maior = verificar_maior_de_todos(numero1, numero2, numero3)

    print(verificacao_maior)

def verificar_maior_de_todos(num1, num2, num3):
    if num1 > num2 and num3:
        return 'numero {} é o maior de todos'.format(num1)
    elif num2 > num3 and num1:
        return 'numero {} é o maior de todos'.format(num2)
    else:
        return 'numero {} é o maior de todos'.format(num3)

main()