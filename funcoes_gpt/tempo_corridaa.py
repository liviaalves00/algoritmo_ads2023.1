#Cálculo de tempo de prova de corrida ou caminhada
#dada a distância da prova (em metros) e a velocidade média do atleta (em km/h), calcule o tempo da prova em minutos.
#Para resolver esse exercício, você pode utilizar a fórmula:
#tempo = (distância / (velocidade * 1000)) * 60
#Aqui, a distância está em metros e a velocidade está em km/h, então é necessário converter a velocidade para metros por minuto, multiplicando por 1000 e dividindo por 60.
#Para obter o resultado final em minutos, é necessário multiplicar o resultado da fórmula por 60.
#Lembre-se de utilizar as funções disponíveis (sqrt, pow, floor e %) e os operadores aritméticos (+, -, *, / e %) para realizar os cálculos

def main():
    #Entrada
    distancia = float(input('Digite a distancia da prova(m): '))
    
    velocidade_med_atleta = float(input('Digite a velocidade média do atleta(km/h): '))
    
    #Processamento
    conversao = calcular_conversao(velocidade_med_atleta)
    
    formula_tempo = calcular_tempo(distancia, velocidade_med_atleta) 
    
    #Saída
    print('A distancia:', distancia, 'm', 'com a velocidade media:', velocidade_med_atleta,'kh/m', 'é em minutos:', formula_tempo)
    #print('O tempo da prova durará: ', formula_tempo, 'minutos')

def calcular_conversao(velocidade_med_atleta):
    #km_para_metros_por_min = (velocidade_med_atleta * 1000) / 60
    km_para_metros_por_min = velocidade_med_atleta * 16.66
    return km_para_metros_por_min

def calcular_tempo(distancia, velocidade_med_atleta):
    resultado_conversao = calcular_conversao(velocidade_med_atleta)
    formula = distancia / resultado_conversao 
    return formula
main()