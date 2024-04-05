'''
Uma loja presenteia suas clientes com descontos (cashback) progressivos de acordo com suas compras.
Desta forma, para compras mensais de até R$ 250 reais, é feita a conversão (geração) de cashback de 5%; Para compras acima de R$ 250 até R$ 500, 7% de cashback;
De R$ 500 até R$ 750, 8% de cashback; E para compras acima de R$ 750 é aplicado primeiramente as regras anteriores até R$ 750 do valor em cada faixa, e 25% sobre o valor acima de R$ 750.
Operações de cashbacks progressivos têm o objetivo de incentivar as suas clientes a comprarem mais e ao mesmo tempo serem compensadas por isso.
a)Implemente um software para auxiliar no cálculo do cashback mensal de suas clientes
(devem ser lidos N compras Nome Cliente e Valor Compras).
b)Informe quanto foi o faturamento total (soma das vendas); Quanto foi distribuído em cashback;
Qual o valor em reais e percentual investido em cashback pela loja; Maior, menor e valor médio pago em cashback. 
'''

def main():
    print('='*10, 'simulador de cashback'.upper(), '='*10)
    
    #Variáveis globais
    cont_clientes = 0
    valor_total_compras = 0
    valor_total_cashback = 0
    valor_maior = float('-inf')
    valor_menor = float('inf')
    
    numero_cliente = int(input('Digite o número de clientes de hoje: '))
    while cont_clientes < numero_cliente:
        cont_clientes += 1
        nome_cliente = input('Digite o seu nome: ')
        numero_compras = float(input('Digite o número de compras: '))
        while numero_compras > 10: #Para fins criativos
            print('Valor inválido!')
            numero_compras = float(input('Digite o número de compras: '))
        
        #Variáveis para cada cliente
        total_cashback = 0
        contador_compra = 0
    
        
        while contador_compra < numero_compras:
            
            contador_compra += 1
            valor_compras = float(input('Digite o valor das suas compras: '))
            calculo_cashback = calcular_cashback(valor_compras)
            
            total_cashback += calculo_cashback 
            valor_total_compras += valor_compras
            
        valor_total_cashback += total_cashback
        
        if total_cashback > valor_maior:
                valor_maior = total_cashback
        if total_cashback < valor_menor:
            valor_menor = total_cashback
    
    
        #Saída
        label = f'CLIENTE: {nome_cliente}'
        print('=' * len(label))
        print(label)
        print('>', total_cashback, 'de cashback')
        print('=' * len(label))
    
    media_cashback = calcular_media(valor_total_cashback, numero_cliente)
    mostrarFaturamento(valor_total_compras, valor_total_cashback, valor_maior, valor_menor, media_cashback)
    

def calcular_media(somatorio, quantidade):
    return somatorio / quantidade
    
def calcular_cashback(valor):
    if valor <= 250:
        return (valor * 0.05)
    elif valor <= 500:
        return (valor * 0.07)
    elif valor <= 750:
        return (valor * 0.08)
    else:
        return ((valor - 750) * 0.25 + 750 *0.08)

def mostrarFaturamento(valor_compras, valor_cashback, maior, menor, media_cash):
    print('=' * 60)
    print(f'O Valor total de compras hoje foi de: R${valor_compras:.2f}')
    print(f'O maior valor de cashback por compra hoje foi: R${maior} ')
    print(f'O menor valor de cashback por compra hoje foi: R${menor}')
    print(f'A média de cashbacks foi de R${media_cash:.2f}')
    print(f'O total de cashbacks concedidos foi de R${valor_cashback:.2f} ')
    print(f'O valor perecentual dos cashbacks sobre o faturamento é de {(valor_cashback / valor_compras) * 100:.2f}')
    print(f'O faturamento total foi de : R${valor_compras:.2f}')
    print('=' * 60)
    
main()