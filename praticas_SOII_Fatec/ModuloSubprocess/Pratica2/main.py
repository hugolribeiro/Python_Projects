# Vamos chamar o script em shell a partir desse script python

import subprocess

p = subprocess.Popen(args=['/bin/bash', 'script_shell.sh'])

# O wait aguardará o processo filho rodar totalmente e armazenará o return code
return_code = p.wait()

if return_code == 0:
    print('Script shell rodado com sucesso')
else:
    print('Script shell falhou ao rodar')

