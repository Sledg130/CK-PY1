from random import randint

def get_unique_list_numbers(min=-10, max=10, len_=15) -> list[int]:
    list_unique_numbers= []
    while len(list_unique_numbers) < len_: # Задаём ограничения для цикла
        number = randint(min, max) # присваиваем каждому числу своё значение
        if number not in list_unique_numbers: # Устанавливаем условие уникальности
            list_unique_numbers.append(number) # Добавляем уникальное число
    return list_unique_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
