
# Criando arquivo 1 com 10 linhas
with open('arquivo1.txt', 'w') as arq1:
    for line in range(1, 10):
        arq1.write(f'Linha {line} do arquivo 1\n')
    arq1.write(f'Linha {line+1} do arquivo 1')