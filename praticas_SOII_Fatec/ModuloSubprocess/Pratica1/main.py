import subprocess

subprocess.call(['ls', '-lah'])

print('__________________________________\n')
subprocess.run(["touch", "testando.txt"])
subprocess.call(['ls', '-lah'])

print('-----------------------------------\n')
result = subprocess.check_output(['ls', '-lah'])
# Transforma de bytes para string
print(result.decode())
