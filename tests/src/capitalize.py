def capitalize(text):
    if text == "":
        return ""
    first_char = text[0].upper()
    rest_subsring = text[1:]
    return first_char + rest_subsring