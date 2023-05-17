'''
Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever
uma mensagem de permissão de acesso ou não.
'''

def main():
    #Entrada
    senha_a_pedir = int(input('Digite a senha: '))
    senha = int(1234)

    validacao_senha = validar_senha(senha_a_pedir, senha)

    print(validacao_senha)
    
def validar_senha(senha_a_pedir, senha):
    if senha_a_pedir >= 4:
        if senha_a_pedir == senha:
            return 'Bem-Vindo'
        else:
            print('Senha Inválida!')
            validar_senha(senha_a_pedir, senha)

main()