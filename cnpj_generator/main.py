# version 0.0.2
import generator


def verify_generate(qtd_cnpj):
    try:
        qtd_cnpj = int(qtd_cnpj)
        if qtd_cnpj < 1 or qtd_cnpj > 100:
            print('Invalid number')
        else:
            for amount in range(0, qtd_cnpj):
                cnpj = generator.generate()
                print(f'{amount+1} - CNPJ: {cnpj}')
    except ValueError:
        print('Esse valor não é válido, tente novamente')


qtd_cnpj = input('Digite aqui a quantidade de cnpjs que gostaria de gerar. Entre 1 e 100. ')
verify_generate(qtd_cnpj)
