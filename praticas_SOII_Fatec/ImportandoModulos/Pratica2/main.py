import os

directory_path = '/home/hleca/TEMPORARIO'
try:
    os.mkdir(directory_path)
    print('Diretório TEMPORARIO criado com sucesso')
    os.chdir(directory_path)
    print(f'Ponteiro para {directory_path} feito')
    os.system('pwd')
    new_path_splitted = directory_path.split('/')
    new_path = '/'.join(new_path_splitted[0:-1])
    os.chdir(new_path)
    print(f'Ponteiro para {new_path} feito')
    os.rmdir(new_path + '/TEMPORARIO')
    print('Diretório TEMPORARIO removido')
except Exception as e:
    print(e)
