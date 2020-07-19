# Objetivo: Programar um validador de CPF.
# O usuário poderá digitar um CPF com pontos e traço ou sem eles.
# No final o programa deverá checar e dizer se o CPF é válido ou inválido.
# O algoritmo APENAS VERIFICARÁ os números. Então não vão importar outros caracteres inseridos.

# Programmer: Hugo Leça Ribeiro
# Date: 27/04/2020


def main():
    backup_cpf = input_cpf()
    clean_cpf = clean_verify_cpf(backup_cpf)
    if clean_cpf:
        is_valid = verify_calculation(clean_cpf)
    else:
        is_valid = False
    if is_valid:
        print(f'Congrats, your CPF {backup_cpf} \033[0;;42mis valid!\033[m')
    else:
        print(f'Ow, no. We got some error here! \033[0;;41mInvalid CPF\033[m')


def input_cpf():
    user_cpf = input('Input here your CPF: ')
    return user_cpf


# This function will clean the cpf and let only numbers, will check the digits too
def clean_verify_cpf(possible_dirty_cpf):
    clean_cpf = ''
    for digit in possible_dirty_cpf:
        if digit.isnumeric():
            clean_cpf += digit
    if len(clean_cpf) != 11:                    # Check the length (a CPF have 11 digits)
        return False
    sequence = clean_cpf[0] * len(clean_cpf)
    if sequence == clean_cpf:                  # Check if the user don't input a sequence (like 11111111111)
        return False
    return clean_cpf


def verify_calculation(cpf_to_do_calculation):
    first_digit = calc_first_digit(cpf_to_do_calculation)
    second_digit = calc_second_digit(cpf_to_do_calculation, first_digit)
    if first_digit == int(cpf_to_do_calculation[-2]) and second_digit == int(cpf_to_do_calculation[-1]):
        return True
    else:
        return False


def calc_first_digit(cpf_to_calc):
    total_first_digit = 0
    for index, count in enumerate(range(10, 1, -1)):
        total_first_digit += int(cpf_to_calc[index]) * count
    module = total_first_digit % 11
    if module < 2:
        first_digit = 0
    else:
        first_digit = 11 - module
    return first_digit


def calc_second_digit(cpf_to_calc, first_digit):
    total_second_digit = 0
    for index, count in enumerate(range(11, 2, -1)):
        total_second_digit += int(cpf_to_calc[index]) * count
    total_second_digit += first_digit * 2
    second_digit = 11 - (total_second_digit % 11)
    if second_digit > 9:
        second_digit = 0
    return second_digit


###Testes automatizados

# def aut_test(cpfs):
#     from time import sleep
#     for index, cpf in enumerate(cpfs):
#         print(f'{index+1}º CPF - {cpf}')
#         print('Verifying the leght and structure...')
#         sleep(2)
#         clean_cpf = clean_verify_cpf(cpf)
#         if clean_cpf:
#             print(f'The cpf {cpf} \033[0;;42mpass to the leght and structure test\033[m')
#             if verify_calculation(clean_cpf):
#                 print(f'The cpf {cpf} \033[0;;42mpass to the calculation test, it is a valid cpf\033[m')
#             else:
#                 print(f'The cpf {cpf} \033[0;;41mdid not pass to the calculation test. It is not a valid cpf\033[m')
#         else:
#             print(f'The cpf {cpf} \033[0;;41mdid not pass to the test leght and structure test\033[m')
#         sleep(2)
#         print('-' * 20)


main()


#### TESTES AUTOMATIZADOS #####
#
# list_cpfs = ['2274563587455',
#              '1111111111111',
#              '3452',
#              'ABD3421',
#              '228.076.638-85',
#              '22807663885',
#              '22222222222',
#              '33333333333',
#              '75863215296',
#              '16899535009',
#              '168.995.350-09',
#              ]
# aut_test(list_cpfs)




