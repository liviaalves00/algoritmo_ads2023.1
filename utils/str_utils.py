def obter_tamanho(texto: str) -> int:
    tamanho = 0
    for caracter in str(texto):
        tamanho += 1
    return tamanho

def quebrar(texto: str) -> list[str]:
    quebrado = []
    for char in texto:
        quebrado.append(char)
    return quebrado

def juntar(textos: list[str], sep:str = ' ') -> str:
    string = ''
    for texto in textos:
        string += texto + sep
    string = string[:-obter_tamanho(sep)]
    return string

def contar_caractere(texto:str, caractere:str, ignore_case: bool = False) -> int:
    if obter_tamanho(caractere) > 1:
        return 'Caracteres somente com 1 de tamanho!'
    cont_caractere = 0
    if ignore_case:
        for char in texto:
            if lowercase_char(caractere) == lowercase_char(char):
                cont_caractere += 1
        return cont_caractere
    
    for char in texto:
        if char == caractere:
            cont_caractere += 1
    return cont_caractere

def contem_caracter(texto: str, caracter_analisado: str, ignore_case: bool = False) -> bool:
    return contar_caractere(texto, caracter_analisado, ignore_case ) > 0

def substituir_caracter(texto:str, caracter_substituir: str, caracter_substituto: str, ignore_case:bool = False) -> str:
    nova_string = ''
    if ignore_case:
        for char in texto:
            if lowercase_char(char) == lowercase_char(caracter_substituir):
                nova_string += caracter_substituto
            else:
                nova_string += char
        return nova_string
    for char in texto:
        if char == caracter_substituir:
            nova_string += caracter_substituto
            continue
        nova_string += char
    return nova_string


def remover_caracter(texto: str, caracter_remover: str, ignore_case: bool = False) -> str:
    nova_string = ''
    for char in texto:
        if ignore_case:
            if lowercase_char(char) == lowercase_char(caracter_remover):
                continue
            nova_string += char
        else:
            if char == caracter_remover:
                continue
            nova_string += char      
    return nova_string

def lowercase_char(char: str) -> str:
    if not eh_lower_char(char):
        return chr(ord(char) + 32)
    return char

def uppercase_char(char: str) -> str:
    if not eh_upper_char(char):
        return chr(ord(char - 32))
    return char

def eh_upper_char(char: str) -> bool:
    return 65 <= ord(char) <= 90

def eh_lower_char(char: str) -> bool:
    return 97 <= ord(char)<= 122

def para_caixa_alta(texto:str) -> str:
    nova_string = ''
    for char in texto:
        if eh_upper_char(char):
            nova_string += char
        else:
            nova_string += uppercase_char(char)
    return nova_string
        
def para_caixa_baixa(texto:str) -> str:
    nova_sting = ''
    for char in texto:
        if eh_lower_char(char):
            nova_sting += char
        else:
            nova_sting += lowercase_char(char)
    return nova_sting

def substring_tamanho(texto:str, inicio:int, tamanho:int):
    if inicio > tamanho:
        return
    nova_string = ''
    final = inicio
    while final < tamanho:
        nova_string += texto[final]
        final += 1
    return nova_string