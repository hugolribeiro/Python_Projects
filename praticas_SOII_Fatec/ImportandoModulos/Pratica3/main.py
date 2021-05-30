import os

file_path = '/home/hleca/Desktop/pythonProject/praticas_sooII/ImportandoModulos/Pratica3/arquivo.txt'

try:
    os.system(f'touch {file_path}')
    print('Arquivo criado com sucesso')
    fd = os.open('arquivo.txt', os.O_RDWR | os.O_CREAT)
    print('Arquivo aberto com sucesso')
    os.write(fd, str.encode("realizando pratica 3 sobre importacao de modulos"))
    print('Escrita feita com sucesso')
    os.close(fd)
except Exception as e:
    print(e)
