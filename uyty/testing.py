
def capitilize(text):
    return text.capitalize()

if capitilize('hello') != 'Hello':
    raise Exception("функция работает неверно")

# Пустая строка None int

if capitilize('') != '':
    raise Exception("функция работает неверно")

print('ok')

def capitalize(text):
    if text == '':
        return ''
        
    # return text.capitalize()
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'

assert capitalize('hello') == 'He2llo'

assert capitalize('') == ''

# пустая строка None int


print('test ok')

