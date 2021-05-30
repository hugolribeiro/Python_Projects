import os

file_path = '/home/hleca/Desktop/pythonProject/praticas_sooII/ImportandoModulos/Pratica3/arquivo.txt'

# Usando o with open não precisamos dar comando para fechar o arquivo
with open(file_path, 'r') as reader:
    for line in reader:
        print(line)

# Usando o open precisamos dar o comando para fechar o arquivo
rd = open(file_path, 'r')
print(rd.read())
rd.close()
