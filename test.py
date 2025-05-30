import os


def should_ignore(path, root_path):
    """Проверяет, нужно ли игнорировать данный путь."""
    # Игнорируем папку /build в корне
    if os.path.isdir(path) and os.path.normpath(path) == os.path.normpath(os.path.join(root_path, 'build')):
        return True
    # Игнорируем файлы CMakeLists.txt.user
    if os.path.isfile(path) and os.path.basename(path) == 'CMakeLists.txt.user':
        return True
    # Игнорируем файлы с расширением .рус
    if os.path.isfile(path) and path.endswith('.рус'):
        return True
    return False


def show_directory_structure(root_path, indent=0):
    """Рекурсивно выводит структуру каталога и содержимое всех файлов (кроме игнорируемых)."""
    try:
        entries = os.listdir(root_path)
    except PermissionError:
        print(" " * indent + f"[Ошибка доступа]: {root_path}")
        return
    except FileNotFoundError:
        print(" " * indent + f"[Папка не найдена]: {root_path}")
        return

    for entry in sorted(entries):
        full_path = os.path.join(root_path, entry)
        if should_ignore(full_path, root_path):
            continue

        if os.path.isdir(full_path):
            print(" " * indent + f"[Папка] {entry}/")
            show_directory_structure(full_path, indent + 4)
        elif os.path.isfile(full_path):
            print(" " * indent + f"- {entry}")
            show_file_content(full_path, indent + 4)


def show_file_content(file_path, indent=0):
    """Выводит содержимое файла с отступом."""
    print(" " * indent + f"[Содержимое файла: {os.path.basename(file_path)}]")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                print(" " * indent + line.rstrip())
    except UnicodeDecodeError:
        print(" " * indent + "[Бинарный файл или неизвестная кодировка]")
    except Exception as e:
        print(" " * indent + f"[Ошибка чтения файла: {e}]")


if __name__ == "__main__":
    import sys

    # Получаем путь из аргументов командной строки или просим ввести
    if len(sys.argv) > 1:
        start_path = sys.argv[1]
    else:
        start_path = input("Введите путь к папке: ").strip()

    if not os.path.isdir(start_path):
        print(f"Указанный путь не является папкой: {start_path}")
    else:
        print(f"Структура папки: {start_path}\n")
        show_directory_structure(start_path)