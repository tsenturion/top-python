from pathlib import Path

folder = Path('.')
max_file = None
max_size = 0

for file in folder.rglob('*'):
    if file.is_file():
        size = file.stat().st_size
        if size > max_size:
            max_size = size
            max_file = file

if max_file:
    print(f'The largest file is: {max_file}')
    print(f'File size: {max_size} bytes')
else:
    print('No files found in the folder.')
    