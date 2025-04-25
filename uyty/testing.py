def capitilize(text):
    return text.capitalize()

if capitilize('hello') != 'Hello':
    raise Exception("функция работает неверно")

# Пустая строка None int

if capitilize('') != '':
    raise Exception("функция работает неверно")

print('ok')