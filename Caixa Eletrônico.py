# Caixa eletrônico desenvolvido no 1º semestre do curso de ADS
# Programador: Hugo Leça Ribeiro

import numpy as np

VNotas = [0] * 6  # Vetor(6) com a quantidade das notas disponíveis
VBackupNotas = [
                   0
               ] * 6  # Um vetor de backup para verificarmos a possibilidade de sacarmos
retiradas = 0  # Variável que irá contar quantas retiradas fizemos
saldo = 0  # Variável que armazenará o saldo bancário
saque = 0  # Variável que receberá o valor do saque desejado
opc = 0  # Armazena a escolha do cliente
banco = 0  # Armazena em qual banco estamos realizando a operação
saque1 = 0  # Um backup para a variável do saque
escolha = 0  # Variável para que o cliente possa escolher trocar 1 nota de 20 por 2 notas de 10

# Variáveis da Matriz para estatistica
Mestatistica = np.zeros((5, 4))  # Cria nossa matriz de estatística
contador = 0


# Opção 1 - Carregar Notas
def case1():
    global saldo
    quantiadecedulas = 10  # Armazena quantas cédulas serão carregadas
    for notas in range(0, 6, 1):
        VNotas[notas] += quantiadecedulas
    print("\nCada cédula foi carregada com a quantia de", quantiadecedulas,
          "unidades\n")
    saldo = (VNotas[5] * 100) + (VNotas[4] * 50) + (VNotas[3] * 20) + (
            VNotas[2] * 10) + (VNotas[1] * 5) + (VNotas[0] * 2)
    return ("\nAtualmente o caixa está com a quantia de R$", saldo)


# Verificação se é possível realizar aquele saque
def confere_possibilidade_saque(saque):
    # Variáveis de quantidades de notas que o cliente receberá:
    n100 = 0
    n50 = 0
    n20 = 0
    n10 = 0
    n5 = 0
    n2 = 0
    global saldo
    saque1 = saque
    if saque > saldo:
        return (2)
    else:
        if saque < 2:
            return (3)  # Erro por saque inferior a 2
        else:
            for notas in range(0, 6, 1):
                VBackupNotas[notas] = VNotas[
                    notas]  # Apenas realizando um backup do Vetor VNotas
            while saque1 % 5 != 0 and VBackupNotas[
                0] >= 1:  # Vamos sacar primeiro as notas de 2 reais, pois são as únicas que não são múltiplas de 5
                saque1 = saque1 - 2
                VBackupNotas[0] = VBackupNotas[0] - 1
                n2 = n2 + 1
            while saque1 >= 100 and VBackupNotas[5] >= 1:
                saque1 = saque1 - 100
                VBackupNotas[5] = VBackupNotas[5] - 1
                n100 = n100 + 1
            while saque1 >= 50 and VBackupNotas[4] >= 1:
                saque1 = saque1 - 50
                VBackupNotas[4] -= 1
                n50 += 1
            while saque1 >= 20 and VBackupNotas[3] >= 1:
                saque1 -= 20
                VBackupNotas[3] -= 1
                n20 += 1
            while saque1 >= 10 and VBackupNotas[2] >= 1:
                saque1 -= 10
                VBackupNotas[2] -= 1
                n10 += 1
            while saque1 >= 5 and VBackupNotas[1] >= 1:
                saque1 -= 5
                VBackupNotas[1] -= 1
                n5 += 1
            while saque1 >= 2 and VBackupNotas[0] >= 1:
                saque1 -= 2
                VBackupNotas[0] -= 1
                n2 += 1
            if saque1 != 0:
                return (0)
            else:
                return (1)


# Opção 2
def case2(Mestatistica):
    global saldo
    global retiradas
    if retiradas >= 100:
        print("Atingimos 100 retiradas, o caixa não realizará mais saques")
    elif (VNotas[0] == 0 and VNotas[1] == 0 and VNotas[2] == 0
          and VNotas[3] == 0 and VNotas[4] == 0 and VNotas[5] == 0):
        print(
            "\nNão há mais nenhuma nota no caixa, não será possível a realização de saques\nAguarde o carregamento do caixa\n"
        )
    else:
        print("\nNo momento o caixa possui as seguintes notas:\n", VNotas[5],
              "Notas de 100 reais\n", VNotas[4], "Notas de 50 reais\n",
              VNotas[3], "Notas de 20 reais\n", VNotas[2],
              "Notas de 10 reais\n", VNotas[1], "Notas de 05 reais\n",
              VNotas[0], "Notas de 02 reais\n")
        saque = int(input("Digite aqui o valor de saque desejado: "))
        banco = int(
            input(
                "Digite aqui qual é o seu banco. Sabendo que:\n 1 - Banco do Brasil\n 2 - Santander\n 3 - Itaú\n 4 - Caixa\n"
            ))
        banco = (
                banco - 1
        )  # Como nossa matriz inicia na posição 0, e vamos usar a variável banco como indíce, achei melhor subtrairmos aqui 1 do banco
        if (confere_possibilidade_saque(saque) == 2):
            print("EXCEDEU O LIMITE DO CAIXA\n")
        elif (confere_possibilidade_saque(saque) == 3):
            (print("O valor a ser sacado deve ser de, no mínimo, 2 reais\n"))
        elif (confere_possibilidade_saque(saque)) == 0:
            print('O caixa não possui notas suficientes para este saque.\n')
        elif (confere_possibilidade_saque(saque) == 1):
            n100 = 0
            n50 = 0
            n20 = 0
            n10 = 0
            n5 = 0
            n2 = 0
            saque1 = saque
            while saque1 % 5 != 0 and VNotas[0] >= 1:
                saque1 -= 2
                VNotas[0] -= 1
                n2 += 1
            while saque1 >= 100 and VNotas[5] >= 1:
                saque1 -= 100
                VNotas[5] -= 1
                n100 += 1
            while saque1 >= 50 and VNotas[4] >= 1:
                saque1 -= 50
                VNotas[4] -= 1
                n50 += 1
            while saque1 >= 20 and VNotas[3] >= 1:
                saque1 -= 20
                VNotas[3] -= 1
                n20 += 1
            while saque1 >= 10 and VNotas[2] >= 1:
                saque1 -= 10
                VNotas[2] -= 1
                n10 += 1
            while saque1 >= 5 and VNotas[1] >= 1:
                saque1 -= 5
                VNotas[1] -= 1
                n5 += 1
            while saque1 >= 2 and VNotas[0] >= 1:
                saque1 -= 2
                VNotas[0] -= 1
                n2 += 1
            print(f'Você sacou a quantia de: R$ {saque}')
            if n20 >= 1 and VNotas[2] >= 2:
                # Verificação para trocar 1 nota de 20 por duas notas de 10
                escolha = int(
                    input(
                        "Caso queira trocar 1 nota de 20 por duas notas de 10 reais, por favor, digite 1:\n"
                    ))
                if escolha == 1:
                    VNotas[3] = VNotas[3] + 1
                    n20 = n20 - 1
                    VNotas[2] = VNotas[2] - 2
                    n10 = n10 + 2
            print("\n", n100, "notas de 100\n", n50, "notas de 50\n", n20,
                  "notas de 20\n", n10, "notas de 10\n", n5, "notas de 5\n",
                  n2, "notas de 2\n")
            saldo = saldo - saque
            retiradas += 1
            print("Retirada de número: ", retiradas, "\n")
            Mestatistica[0, banco] = Mestatistica[
                                         0, banco] + 1  # Acrescenta 1 no contador da matriz
            if saque > Mestatistica[1, banco]:  # Maior saque
                Mestatistica[1, banco] = saque
            if saque < Mestatistica[2, banco] or Mestatistica[2, banco] == 0:
                Mestatistica[2, banco] = saque  # Menor saque
            Mestatistica[3, banco] = Mestatistica[
                                         3, banco] + saque  # Valor total dos saques


def case3(Mestatistica):
    global saldo
    global banco
    for banco in range(0, 4, 1):
        if Mestatistica[3, banco] != 0:
            Mestatistica[4, banco] = Mestatistica[3, banco] / Mestatistica[
                0, banco]  # Calculando a média de saques (Total / contador)
    print('\n' * 15 + 'Estatística:')
    print("\nBanco do Brasil:\nO maior valor sacado foi de: R$",
          Mestatistica[1, 0], "\nO menor valor sacado foi de: R$",
          Mestatistica[2, 0], "\nA média dos saques foi de: R$",
          Mestatistica[4, 0], "\nO valor total dos saques foi de: R$",
          Mestatistica[3, 0])
    print("\nSantander:\nO maior valor sacado foi de: R$", Mestatistica[1, 1],
          "\nO menor valor sacado foi de: R$", Mestatistica[2, 1],
          "\nA média dos saques foi de: R$", Mestatistica[4, 1],
          "\nO valor total dos saques foi de: R$", Mestatistica[3, 1])
    print("\nItaú:\nO maior valor sacado foi de: R$", Mestatistica[1, 2],
          "\nO menor valor sacado foi de: R$", Mestatistica[2, 2],
          "\nA média dos saques foi de: R$", Mestatistica[4, 2],
          "\nO valor total dos saques foi de: R$", Mestatistica[3, 2])
    print("\nCaixa:\nO maior valor sacado foi de: R$", Mestatistica[1, 3],
          "\nO menor valor sacado foi de: R$", Mestatistica[2, 3],
          "\nA média dos saques foi de: R$", Mestatistica[4, 3],
          "\nO valor total dos saques foi de: R$", Mestatistica[3, 3])
    print("\nO valor da sobra do caixa eletrônico é de: R$", saldo, "\n")


while opc != 9:  # Enquanto o usuário não digitar '9' (FIM) o programa rodará
    opc = (int(
        input(
            "Digite 1 para carregar notas\nDigite 2 para Retirar Notas\nDigite 3 para saber as estatísticas\nDigite 9 para encerrar o programa\n"
        )))
    if opc == 1:  # Opção 1 - Carregar Notas
        case1()
    elif opc == 2:  # Opção 2 - Sacar
        case2(Mestatistica)
    elif opc == 3:  # Opção 3 - Estatística
        case3(Mestatistica)
print("FIM!")
