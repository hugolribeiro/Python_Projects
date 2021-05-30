import sys

sys.stdout.write('Testing message to stdout\n')
sys.stderr.write('Testing message to stderr\n')
msg_inputted = sys.stdin.read()
sys.stdout.write(f'Received: {msg_inputted}')
