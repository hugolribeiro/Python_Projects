from subprocess import Popen, PIPE, STDOUT


p = Popen(['python3', 'filho.py'], stdout=PIPE, stderr=STDOUT, stdin=PIPE)
print(p.communicate('Hello?'.encode())[0].decode())

# p = subprocess.Popen(['python3', 'filho_testando.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# print(p.communicate()[0].decode())
#
# p1 = subprocess.Popen(['python3', 'filho_stdin.py'], stdin=subprocess.PIPE)
# print(p1.communicate('Hello?'.encode()))
