"""
1603_pathlib
"""

from pathlib import Path

path = Path('data/file.txt')

print(path.name)
print(path.suffix)
print(path.stem)
print(path.parent)
print(path.exists())
print(path.is_file())
print(path.is_dir())

path = Path('data') / 'files' / 'subfile.txt'

path = Path('data/files/log')
# path.mkdir()
# path.mkdir(parents=True, exist_ok=True) 
# content = path.read_text()
# path.write_text('Hello, World!')

for file in path.glob('*.txt'):
    print(file)
    
for file in path.rglob('*.txt'):
    print(file)