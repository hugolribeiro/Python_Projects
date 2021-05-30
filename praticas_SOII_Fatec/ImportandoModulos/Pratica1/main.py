import os

file_path = '/home/hleca/arquivo_pratica_1.txt'

try:
    open(file_path, 'a').close()
except Exception as e:
    print(e)

try:
    os.system(f'chgrp -c adm {file_path}')
    os.chmod(file_path, 774)
except Exception as e:
    print(e)
