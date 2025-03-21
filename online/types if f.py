my_variable: str = "str"

def greet(name: str) -> str:
    return f"hi, {name}"

print(greet(12))

def sum_numbers(a: int, b: int) -> int:
    return a + b

print(sum_numbers("1", "2"))


# isinstance()
data = 1
def process_data(data):
    if isinstance(data, (list, int)):
        print("обр list/int")
    elif isinstance(data, dict):
        print("обр dict")
    else:
        print('неверный тип данных')

process_data(data)

