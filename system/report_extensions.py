# пройтись по папкам, показать сколько файлов каждого типа + размер
from pathlib import Path
from collections import defaultdict

folder = Path('.')
stats = defaultdict(lambda: {'count': 0, 'size': 0})

for file in folder.rglob('*'):
    if file.is_file():
        ext = file.suffix.lower() if file.suffix else '[без расширения]'
        stats[ext]['count'] += 1
        stats[ext]['size'] += file.stat().st_size

for ext in sorted(stats.keys()):
    data = stats[ext]
    print(f'{ext} {data["count"]} {data["size"]}')