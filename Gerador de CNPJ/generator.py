# version 0.0.2
def generate():
    from random import randint
    while True:
        actual_cnpj = str(randint(10000000, 99999999))
        if actual_cnpj[0] * 8 == actual_cnpj:
            continue
        else:
            break
    actual_cnpj += '0001'
    with1digit = actual_cnpj + str(calculate_1stdigit(actual_cnpj))
    with2digits = with1digit + str(calculate_2stdigit(with1digit))
    formated_cnpj = format_cnpj(with2digits)
    return formated_cnpj


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


def format_cnpj(cnpj):
    formated_cnpj = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return (formated_cnpj)
