"""
1601_os
"""

import os

current_directory = os.getcwd()
print(current_directory)

os.chdir('..')
print(os.getcwd())

files = os.listdir()
print(files)

files = os.listdir('..')
print(files)

print(os.path.isfile('1601_os.py'))
print(os.path.isdir('1601_os.py'))
print(os.path.exists('1601_os.py'))

path = 'folder/file.txt'

path = os.path.join('folder', 'file.txt')
print(path)

