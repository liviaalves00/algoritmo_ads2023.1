import random

def clear_screen():
    input('press enter...')
    import os
    os.system('cls') 

clear_screen()

def bye():
    byebye = [
        "Arrivedercci", "Se divertiu ne? Pois agora vaza...", "Até nunca mais", "Não volte mais", "OH NO", "OH MY GOD", "Lembre-se: o que está ruim sempre pode piorar", "Beba água, cuidado com as pedras...", "VOCÊ OUVIU ISSO?", "TO BE CONTINUED -->"
    ]

    index = random.randint(0, len(byebye) - 1)

    print(byebye[index])