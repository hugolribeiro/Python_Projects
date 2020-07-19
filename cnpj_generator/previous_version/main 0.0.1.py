import generator


def verify_amount(qtd_cnpj):
    try:
        qtd_cnpj = int(qtd_cnpj)
        if qtd_cnpj < 1 or qtd_cnpj > 100:
            print('Invalid number')
        else:
            for amount in range(0, qtd_cnpj):
                cnpj = generator.generate()
                formated_cnpj = format_cnpj(cnpj)
                print(f'{amount+1} - CNPJ: {formated_cnpj}')
    except ValueError:
        print('Esse valor não é válido, tente novamente')


def format_cnpj(cnpj):
    formated_cnpj = list(cnpj)
    formated_cnpj.insert(2, '.')
    formated_cnpj.insert(6, '.')
    formated_cnpj.insert(10, '/')
    formated_cnpj.insert(15, '-')
    formated_cnpj_string = ''
    for character in formated_cnpj:
        formated_cnpj_string += character
    return str(formated_cnpj_string)


qtd_cnpj = input('Digite aqui a quantidade de cnpjs que gostaria de gerar. Entre 1 e 100. ')
verify_amount(qtd_cnpj)
