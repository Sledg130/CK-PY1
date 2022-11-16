from random import sample
import string

def get_random_password(n=8, double = 5) -> str: # double - колиество возможных повторений для символа
    str_ = string.ascii_letters + string.digits # формирование списка используемых символов
    random_password = sample(population= str_, k = n, counts = [double for _ in str_]) # counts испольуем для того, чтобы не было уникальности символов
    return "".join(random_password)

print(get_random_password())
