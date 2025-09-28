import os

IGNORED_DIRS = {'.git', '.vscode', '__pycache__', '.idea', '.pytest_cache', '.venv'}
IGNORED_FILE_EXTENSIONS = {'.user'}

def save_directory_structure(root_path, output_file, indent=0):
    """Рекурсивно сохраняет структуру каталога и содержимое допустимых файлов."""
    try:
        entries = os.listdir(root_path)
    except PermissionError:
        output_file.write(" " * indent + f"[Ошибка доступа]: {root_path}\n")
        return
    except FileNotFoundError:
        output_file.write(" " * indent + f"[Папка не найдена]: {root_path}\n")
        return

    for entry in sorted(entries):
        full_path = os.path.join(root_path, entry)

        # Игнорировать скрытые папки и указанные игнорируемые директории
        if os.path.isdir(full_path):
            if entry.startswith('.') or entry in IGNORED_DIRS:
                continue
            output_file.write(" " * indent + f"[Папка] {entry}/\n")
            save_directory_structure(full_path, output_file, indent + 4)

        elif os.path.isfile(full_path):
            # Пропуск скрытых файлов и файлов с игнорируемыми расширениями
            _, ext = os.path.splitext(entry)
            if entry.startswith('.') or ext in IGNORED_FILE_EXTENSIONS:
                continue

            output_file.write(" " * indent + f"- {entry}\n")
            save_file_content(full_path, output_file, indent + 4)

def save_file_content(file_path, output_file, indent=0):
    """Сохраняет содержимое файла с отступом."""
    output_file.write(" " * indent + f"[Содержимое файла: {os.path.basename(file_path)}]\n")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                output_file.write(" " * indent + line.rstrip() + "\n")
    except Exception as e:
        output_file.write(" " * indent + f"[Ошибка чтения файла: {e}]\n")

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        start_path = sys.argv[1]
    else:
        start_path = input("Введите путь к папке: ").strip()

    if not os.path.isdir(start_path):
        print(f"Указанный путь не является папкой: {start_path}")
    else:
        output_filename = "directory_structure.txt"
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(f"Структура папки: {start_path}\n\n")
            save_directory_structure(start_path, output_file)
        
        print(f"Структура папки сохранена в файл: {output_filename}")