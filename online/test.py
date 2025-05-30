"""def capitalize(text):
    first_char = text[0].upper()
    rest_subsring = text[1:].lower()
    return first_char + rest_subsring"""

"""def capitalize(text):
    first_char, *rest_chars = text
    rest_substring = ''.join(rest_chars)
    return first_char.upper() + rest_substring
"""

def capitalize(text):
    if text == "":
        return ""
    first_char = text[0].upper()
    rest_subsring = text[1:]
    return first_char + rest_subsring

capitalize("hello")  # 'Hello'
print(capitalize("hello"))

"""raise Exception("ошибка в программе")
print('никогда не выведется')"""

if capitalize("hello") != "Hello":
    raise Exception("функция работает неверно")

if capitalize("") != "":
    raise Exception("функция работает неверно")


def get_by_index(elemensts, index, default):
    return elemensts[index] if index < len(elemensts) else default

get_by_index([1, 2, 3], 0, 0)  # 1
get_by_index(['zero', 'one'], 2, 'value')  # 'ошибка'