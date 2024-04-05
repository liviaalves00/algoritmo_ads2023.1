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

   #Moedas
    moeda_um_real = int(valor_pedido // 1)
    valor_pedido -= moeda_um_real * 1

    moeda_cinquenta = int(valor_pedido // 0.5)
    valor_pedido -= moeda_cinquenta * 0.5

    moeda_vinte_cinco = int(valor_pedido // 0.25)
    valor_pedido -= moeda_vinte_cinco * 0.25

    moeda_dez = int(valor_pedido // 0.1)
    valor_pedido -= moeda_dez * 0.1

    moeda_cinco = int(valor_pedido // 0.05)
    valor_pedido -= moeda_cinco * 0.05

    moeda_um_centavo = int(round(valor_pedido // 0.01))

    print('NOTAS:')
    print(f'{notas_cem} nota(s) de R$ 100.00')
    print(f'{notas_cinquneta} nota(s) de R$ 50.00')
    print(f'{notas_vinte} nota(s) de R$ 20.00')
    print(f'{notas_dez} nota(s) de R$ 10.00')
    print(f'{notas_cinco} nota(s) de R$ 5.00')
    print(f'{notas_dois} nota(s) de R$ 2.00')
    print('MOEDAS:')
    print(f'{moeda_um_real} moeda(s) de R$ 1.00')
    print(f'{moeda_cinquenta} moeda(s) de R$ 0.50')
    print(f'{moeda_vinte_cinco} moeda(s) de R$ 0.25')
    print(f'{moeda_dez} moeda(s) de R$ 0.10')
    print(f'{moeda_cinco} moeda(s) de R$ 0.05')
    print(f'{moeda_um_centavo} moeda(s) de R$ 0.01')
  
  
main()