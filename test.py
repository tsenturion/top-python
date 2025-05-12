import chardet

with open(r'C:\Program Files\PostgreSQL\17\data\log\postgresql-2025-04-30_202819.log', 'rb') as f:
    result = chardet.detect(f.read())
    print(result)
