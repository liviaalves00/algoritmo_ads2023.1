def is_even(num):
    if num % 2 == 0:
        return True
    return False

def is_odd(num):
    if num % 2 == 1:
        return True
    return False

def is_integer(num):
    if (num) and (not float(num)):
        return True
    return False

def is_integer_type(num):
    return type(num) == int

def is_positive(num):
    return num > 0
