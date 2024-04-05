from math_utils import*

def mapmap(function, collection):
    if isinstance(collection, list):
        modified_list = []
        for item in collection:
            modified_list.append(function(item))
        return modified_list
    elif isinstance(collection, str):
        modified_string = ''
        for char in collection:
            modified_string += function(char)
        return modified_string
    return collection

def push(vector, item):
    return vector + [item]

def poppop(vector):
    x = []
    for i in range(len(vector) - 1):
        x = push(x, vector[i])
    return x

def delete(vector, index):
    new_list = []
    for i in range(len(vector)):
        if i != index:
            new_list = push(new_list, vector[i])
    return new_list

def search(list, item):
    for element in list:
        if item == element:
            return True
    return False

def filter(criteria_function, list):
    filtered_items = []
    for item in list:
        if criteria_function(item):
            filtered_items = push(filtered_items, item)
    return filtered_items

def sum_vector(vector):
    sum = 0
    for item in vector:
        if int(f'{item}') or float(f'{item}'):
            sum += item
    return sum

def bubble_sort(received_vector, reverse=False):
    vector = received_vector[:]
    has_swaps = False
    for i in range(len(vector) - 1):
        has_swaps = False
        for i in range(len(vector) - 1):
            if vector[i] > vector[i+1]:
                current = vector[i]
                next = vector[i+1]
                vector[i] = next
                vector[i+1] = current
                has_swaps = True
        if not has_swaps:
            break
    if reverse:
        return reverse_list(vector)
    return vector

def reverse_list(received_list):
    modified_list = received_list[:]
    for i in range(len(received_list)):
        modified_list[i] = received_list[-(i+1)]
    return modified_list

def median(received_list):
    list = bubble_sort(received_list)
    size = len(list)
    if size == 0:
        return None
    elif is_odd(size):
        median = list[int(((size + 1) / 2) - 1)]  # median formula
    elif is_even(size):
        median = ((list[int((size/2)-1)] + list[int((size/2))]) / 2)
    return median

def average(summation, quantity):
    if summation != 0 and quantity > 0:
        return summation / quantity
    elif summation == 0 and quantity > 0:
        return 0
    return None

def remove_duplicates(vector):
    verified = []
    for i in range(len(vector) - 1):
        if not search(verified, vector[i]):
            verified = push(verified, vector[i])

def reduce_product(vector):
    accumulated = 1
    for item in vector:
        accumulated *= item
    return accumulated
