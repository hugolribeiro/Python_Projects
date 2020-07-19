# Objetivo: Programar um gerador de CPF

# Programmer: Hugo Leça Ribeiro
# Date: 27/04/2020


def main():
    try:
        numbers_cpf = int(input('How many CPFs do you want to generate? '))
        for number in range(0, numbers_cpf):
            user_cpf = generate_cpf()
            complete_cpf = calculation_digits(user_cpf)
            print(f'We generated this CPF: {complete_cpf}')
    except ValueError:
        print('Sorry, wrong value inputed.')


def generate_cpf():
    from random import randint
    while True:
        future_user_cpf = str(randint(100000000, 999999998))
        if future_user_cpf == (future_user_cpf[0] * 9):
            continue
        return future_user_cpf


def calculation_digits(cpf_to_do_calculation):
    first_digit = calculation_first_digit(cpf_to_do_calculation)
    second_digit = calculation_second_digit(first_digit, cpf_to_do_calculation)
    cpf_complete = cpf_to_do_calculation + str(first_digit) + str(second_digit)
    return cpf_complete


def calculation_first_digit(cpf_to_calc):
    total_first_digit = 0
    for index, count in enumerate(range(10, 1, -1)):
        total_first_digit += int(cpf_to_calc[index]) * count
    module = total_first_digit % 11
    if module < 2:
        first_digit = 0
    else:
        first_digit = 11 - module
    return first_digit


def calculation_second_digit(first_digit, cpf_to_test):
    total_second_digit = 0
    for index, count in enumerate(range(11, 2, -1)):
        total_second_digit += int(cpf_to_test[index]) * count
    total_second_digit += first_digit * 2
    second_digit = 11 - (total_second_digit % 11)
    if second_digit > 9:
        second_digit = 0
    return second_digit


main()
