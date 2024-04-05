from math_utils import*
from str_utils import*
import random

def get_text(label='Enter some text: '):
    text = input(label)
    if text == '':
        return get_text(label)
    return text

def get_length(text: str) -> int:
    length = 0
    for character in str(text):
        length += 1
    return length

def get_number(label='Enter a number: '):
    number = get_text(label)
    if not number:
        return get_number(label)
    return number

def get_integer(label='Enter an integer: '):
    number = get_number(label)
    if not is_integer_type(number):
        return get_integer(label)
    return number

def get_positive_integer(label='Enter a positive integer: '):
    number = get_number(label)
    if not (is_integer_type(number) and number > 0):
        return get_positive_integer(label)
    return number

def get_minimum_integer(minimum_size, label=''):
    if label == '':
        num = get_integer(f'Please enter a number greater than or equal to {minimum_size}: ')
    else:
        num = get_integer(label)
    if num < minimum_size:
        return get_minimum_integer(minimum_size, label)
    return num

def show_text(label=''):
    if label != '':
        return label

def show_array(vetor):
    print("Vetor:")
    for i, elemento in enumerate(vetor):
        return f'Posição {i}: {elemento}'

    
def ask_yes_or_no(label='Yes or No?'):
    question = string_to_uppercase(get_text(f'{label} (Y/N)\n>>>'))
    if question == 'Y' or question == 'YES':
        return True
    elif question == 'N' or question == 'NO':
        return False
    else:
        return ask_yes_or_no(label)

def bye():
    tchaus = [
        "Arrivedercci", "Se divertiu ne? Pois agora vaza...", "Até nunca mais", "Não volte mais", "OH NO", "OH MY GOD"
    ]

    index = random.randint(0, len(tchaus) - 1)

    print(tchaus[index])

def clear_screen():
    input('press enter...')
    import os
    os.system('cls') 

clear_screen()