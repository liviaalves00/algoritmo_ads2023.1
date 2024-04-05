def main():
    while True:
        eixo_x_fiddlesticks,  eixo_y_fiddlesticks,  eixo_x_enemy,  eixo_y_enemy, speed_enemy, raio, fly_raio = list(map(float, input().split()))

        #distancia (similar a questao de distancia_pontos)
        delta_x = eixo_x_fiddlesticks - eixo_x_enemy
        delta_y = eixo_y_fiddlesticks - eixo_y_enemy
        conjuracao = 1.5
        maximo_alcance = raio + fly_raio
        distancia_ini = calcular_distancia_inicial(delta_x, delta_y)
        distancia_fin =  calcular_distancia_final(distancia_ini, speed_enemy, conjuracao)

        acertou_ou_nao_a_ult = acertar_ou_nao_ult(distancia_fin, maximo_alcance)

        print(acertou_ou_nao_a_ult)

def calcular_distancia_inicial(delta_x, delta_y):
    return ((delta_x ** 2) + (delta_y ** 2 )) ** 0.5 #raiz (calculo da distancia)

def calcular_distancia_final(distancia, speed_enemy, conjuracao):
    return distancia + (speed_enemy * conjuracao)

def acertar_ou_nao_ult(distancia_fin, maximo_alcance):
    if distancia_fin <= maximo_alcance:
        return 'Y'
    else:
        return 'N'
    
main()