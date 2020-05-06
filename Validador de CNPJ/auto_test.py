# Testes automatizados para sabermos se o algoritmo está funcionando corretamente

import verificador_cnpj_0_0_2
from time import sleep

def test():
    corrects_cnpjs = ['45.997.418/0001-53',
                      '58.123.035-0001-06',
                      '60.316.817/0001-03',
                      '15.436.940/0001-03',
                      ]
    wrongs_cnpj = ['55555555555555',
                   '8569',
                   '43ABCF',
                   '++++++++++++++',
                   '--==++--++--++',
                   '105236',
                   '15.436.940/0001-65']
    print('\n-------------------------Iniciando testes--------------------------\n')
    sleep(1)
    try_cnpjs = corrects_cnpjs + wrongs_cnpj
    for business in try_cnpjs:
        print(f'Iniciando teste com {business}')
        clean_business = verificador_cnpj_0_0_2.remove_characters(business)
        business_withoutdigits = clean_business[:-2]
        if verificador_cnpj_0_0_2.check_length(clean_business):
            print('Lenght - valid')
        else:
            print('Lenght - invalid')
        try:
            if verificador_cnpj_0_0_2.is_sequence(business_withoutdigits):
                print('It is a sequence - invalid')
            else:
                print('Not a sequence - valid')
        except Exception:
            print('Only characters - invalid')
        if verificador_cnpj_0_0_2.verify(business):
            print('after all - valid')
        else:
            print('after all - invalid')
        sleep(1)
        print('-' * 50)
        sleep(1)
