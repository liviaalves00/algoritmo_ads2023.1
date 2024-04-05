from random import randint

def count_character_occurrences(text, target_character, ignore_case=True):
    occurrences = 0
    if ignore_case:
        target_character = target_character.lower()
        text = text.lower()
    for char in text:
        if char == target_character:
            occurrences += 1
    return occurrences

def generate_random(minimum, maximum):
    return randint(minimum, maximum)

def char_to_uppercase(char):
    if 'a' <= char <= 'z':
        return chr(ord(char) - 32)
    return char

def char_to_lowercase(char):
    if 'A' <= char <= 'Z':
        return chr(ord(char) + 32)
    return char

def string_to_uppercase(string):
    uppercase = map(char_to_uppercase, string)
    return ''.join(uppercase)

def string_to_lowercase(string):
    lowercase = map(char_to_lowercase, string)
    return ''.join(lowercase)