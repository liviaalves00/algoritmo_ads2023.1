def main():
    valor_pedido = int(input())

    notas_cem = int(valor_pedido // 100)
    valor_pedido -= notas_cem * 100

    notas_cinquneta = int(valor_pedido // 50)
    valor_pedido -= notas_cinquneta * 50

    notas_vinte = int(valor_pedido // 20)
    valor_pedido -= notas_vinte * 20
    
    notas_dez = int(valor_pedido // 100)
    valor_pedido -= notas_dez * 10

    notas_cinco = int(valor_pedido // 5)
    valor_pedido -= notas_cinco * 5

    notas_dois = int(valor_pedido // 2)
    valor_pedido -= notas_dois * 2

    notas_um = int(valor_pedido // 1)
    valor_pedido -= notas_um * 1
    

    print(f'{notas_cem} nota(s) de R$ 100,00')
    print(f'{notas_cinquneta} nota(s) de R$ 50,00')
    print(f'{notas_vinte} nota(s) de R$ 20,00')
    print(f'{notas_dez} nota(s) de R$ 10,00')
    print(f'{notas_cinco} nota(s) de R$ 5,00')
    print(f'{notas_dois} nota(s) de R$ 2,00')
    print(f'{notas_um} nota(s) de R$ 1,00')
    
    
main()