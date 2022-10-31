def get_count_char(main_str_):
    main_str_dict = {}
    main_str_ = "".join(main_str_.split())
    main_str_ = main_str_.lower()
    for symbul in main_str_:
        if symbul.isalpha():
            if symbul in main_str_dict:
                main_str_dict[symbul] += 1
            else:
                main_str_dict[symbul] = 1
    return main_str_dict

def get_call(dict_):
    sum_symbul = 0
    for symbul in dict_:
        sum_symbul += dict_[symbul]
    for symbul in dict_:
        dict_[symbul] = round(dict_[symbul] / sum_symbul * 100, 1)
    return dict_
main_str_ = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str_))
print(get_call(get_count_char(main_str_)))