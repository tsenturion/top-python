from pathlib import Path

folder = Path('.')
deleted = 0

for tmp_file in folder.rglob('*.tmp'):
    if tmp_file.is_file():
        tmp_file.unlink()
        print(f'deleted {tmp_file}')
        deleted += 1

print(f'{deleted} deleted')