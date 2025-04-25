def capitalize(text):
    if text == '':
        return ''
        
    # return text.capitalize()
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'

if capitalize('hello') != 'Hello':
    raise Exception('test failed')

# пустая строка None int

if capitalize('') != '':
    raise Exception('test failed')

print('test ok')