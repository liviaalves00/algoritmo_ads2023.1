def main():
    numero = int(input())

    for i in range(numero):
        numero = input()
        leds = calcular_leds(numero)
        print(leds, "leds")

def calcular_leds(numero):
    leds = 0
    for numero_led in numero:
        leds += calcular_leds_digito(numero_led)
    return leds

def calcular_leds_digito(numero_led):
    if numero_led == "1":
        return 2
    if numero_led == "2" or numero_led == "3" or numero_led == "5":
        return 5
    if numero_led == "4":
        return 4
    if numero_led == "6" or numero_led == "9" or numero_led == "0":
        return 6
    if numero_led == "7":
        return 3
    if numero_led == "8":
        return 7
    else:
        return 0
    
main()