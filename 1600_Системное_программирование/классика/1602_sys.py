"""
1602_sys
"""

import sys
print(sys.argv)
# python app.py test.txt
# filename = sys.argv[1]
# print(filename)

# if len(sys.argv) < 2:
#     print("No filename provided.")
#     sys.exit(1)

"""
exit
\q
Ctrl+C (возможно, 3 раза подряд)
stop
"""

print(sys.platform)

print(sys.path)

sys.path.append('..')