"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0  4  2  5  2  0  1  1  0  0  0  1  x  x
5  4  3  2  9  8  7  6  5  4  3  2
0  16 6  10 18 0  7  6  0  0  0  2 =  65 ##
Fórmula -> (65 % 11) = 1
Primeiro dígito = 1 (Se o dígito for maior do que 9, ele se torna 0)

0  4  2  5  2  0  1  1  0  0  0  1  1  X
6  5  4  3  2  9  8  7  6  5  4  3  2
0  20 8  15 4  0  8  7  0  0  0  3  2  = 67 ##

Fórmula -> (67 % 11) = 11 (Como o resultado é maior que 9, então é 0)
Segundo dígito = 0

NOvo CNPJ + Dígitos = 04.252.011/0001-10
NPJ Original -        04.252.011/0001-10
Válido

Recapitulando
543298765432 -> Primeiro dígito
6543298765432 -> Segundo dígito
"""

import verificador_cnpj_0_0_2

cnpj = (input('Digite aqui o número do CNPJ: '))
verificador_cnpj_0_0_2.verify(cnpj)


######## TESTE AUTOMATIZADO ############
# Caso queira realizar um teste, rode o código abaixo
#
# import auto_test
# auto_test.test()
