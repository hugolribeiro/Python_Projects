import re


def verify(cnpj):
    clean_cnpj = remove_characters(cnpj)
    cnpj_withoutdigits = clean_cnpj[:-2]
    if not check_length(clean_cnpj):
        print('Seu CNPJ não possui o número de caracteres próprios de um CNPJ (14 número com dígitos)')
        print(f'\033[0;;41mCNPJ INVÁLIDO\033[m')
        return False
    elif is_sequence(cnpj_withoutdigits):
        print('É uma sequência')
        print(f'\033[0;;41mCNPJ INVÁLIDO\033[m')
        return False
    else:
        first_digit = calculate_1stdigit(cnpj_withoutdigits)
        cnpj_with1digit = cnpj_withoutdigits + str(first_digit)
        second_digit = calculate_2stdigit(cnpj_with1digit)
        cnpj_with2digits = cnpj_with1digit + str(second_digit)
        return check_cnpjs(clean_cnpj, cnpj_with2digits)



def remove_characters(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def check_length(clean_cnpj):
    if len(clean_cnpj) == 14:
        return True
    else:
        return False


def is_sequence(cnpj_withoutdigits):
    if cnpj_withoutdigits[0] * len(cnpj_withoutdigits) == cnpj_withoutdigits:
        return True
    else:
        return False


def calculate_1stdigit(clean_cnpj):
    sequence = '678923456789'
    total = 0
    for count in range(0, 12):
        total += int(clean_cnpj[count]) * int(sequence[count])
    first_digit = (total % 11)
    if first_digit > 9:
        first_digit = 0
    return first_digit


def calculate_2stdigit(cnpj_with1digit):
    sequence2 = '5678923456789'
    total = 0
    for count in range(0, 13):
        total += (int(cnpj_with1digit[count]) * (int(sequence2[count])))
    second_digit = (total % 11)
    if second_digit > 9:
        second_digit = 0
    return second_digit


def check_cnpjs(clean_cnpj, cnpj_with2digits):
    if clean_cnpj == cnpj_with2digits:
        print(f'CNPJ inserido: {clean_cnpj}\n'
             f'CNPJ correto: {cnpj_with2digits}\n'
             f'\033[0;;42mCNPJ VÁLIDO\033[m')
        return True
    else:
        print(f'CNPJ inserido: {clean_cnpj}\n'
             f'CNPJ correto: {cnpj_with2digits}\n'
             f'\033[0;;41mCNPJ INVÁLIDO\033[m')
        return False
