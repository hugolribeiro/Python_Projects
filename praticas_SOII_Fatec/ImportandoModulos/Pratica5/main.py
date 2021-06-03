# Criando arquivo 1 com 10 linhas
with open('arquivo1.txt', 'w') as arq1:
    for line in range(1, 11):
        arq1.write(f'Linha {line} do arquivo 1\n')

# Criando arquivo 2 com 10 linhas
with open('arquivo2.txt', 'w') as arq1:
    for line in range(1, 11):
        arq1.write(f'Linha {line} do arquivo 2\n')

# Lendo ambos arquivos e intercalando
with open('arquivo1.txt', 'r') as arq1:
    with open('arquivo2.txt', 'r') as arq2:
        with open('arquivo3.txt', 'w') as arq3:
            for line in range(0, 20):
                arq3.write(arq1.readline())
                arq3.write(arq2.readline())
