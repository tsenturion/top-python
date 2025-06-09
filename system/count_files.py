# подсчет файлов с заданным расширением
from pathlib import Path
import sys

if len(sys.argv) != 3:
    print('Использование: python count_files.py <путь> <расширение>')
    sys.exit(1)

folder = Path(sys.argv[1])
ext = sys.argv[2]
print(folder, ext)
abs_path = folder.resolve() # абсолютный путь
print(abs_path)
if not folder.exists() or not folder.is_dir():
    print('путь не существует или не является каталогом')
    sys.exit(1)

count = sum(1 for f in folder.rglob(f'*{ext}') if f.is_file())

print(f'количество файлов с расширением {ext}: {count}')