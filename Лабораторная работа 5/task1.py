from pprint import pprint

def dict_number(number):
    dict_ = [({'bin': bin(number), 'dec': (number), 'hex': hex(number), 'oct': oct(number)}) for number in range(number)]
    return dict_
pprint(dict_number(16))

