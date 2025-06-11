from pathlib import Path

project_root = Path('my_project')

(project_root / 'src').mkdir(parents=True, exist_ok=True)
(project_root / 'tests').mkdir(parents=True, exist_ok=True)

readme = project_root / 'README.md'
if not readme.exists():
    readme.write_text('Описание проекта')
    print('Файл README.md создан')
else:
    print('Файл README.md уже существует')
    