from patrocars_features import*

def main():
    OUT = '0'
    APPEND_MONTADORA = '1'
    LIST_MONTADORA = '2'
    UPDATE_MONTADORA = '3'
    REMOVE_MONTADORA = '4'
    APPEND_MODELO = '6'
    LIST_MODELO = '7'


    montadoras = inicialization('montadoras')
    modelos = inicialization('modelos', montadoras)
    #veiculos = inicialization('veiculos')

    
    contador_montadora = lambda: f"{len(montadoras)} montadoras"

    menu = lambda: f"""======================== PATROCARS [{contador_montadora()}] ==========================
    1 = Adicionar Montadora
    2 = Listar Montadoras
    3 = Atualizar Montadora
    4 = Remover Montadora
    5 = Novo Modelo
    6 = Listar Modelos
    0 = Sair
    \n >> """

    opcao = input(menu())

    opcao = menu()
    while opcao != OUT:
        if opcao == APPEND_MONTADORA:
            nova_montadora = generate_montadora()
            montadoras.append(nova_montadora)
            print(f"{nova_montadora['nome']} adicionada!")
        elif opcao == LIST_MONTADORA:
            show_montadoras(montadoras)
        elif opcao == REMOVE_MONTADORA:
            remover_montadora(montadoras)
        elif opcao == UPDATE_MONTADORA:
            atualizar_montadora(montadoras)
        elif opcao == APPEND_MODELO:
            modelo = generate_modelo(montadoras)
            modelos.append(modelo)
        elif opcao == LIST_MODELO:
            show_modelos(modelos)

        clear_screen()

        opcao = input(menu())

    write_data(montadoras, modelos)

main()
