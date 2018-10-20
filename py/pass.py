import time
from itertools import product

target = "pass"
chars = 'abcdefghijklmnopqrstuvwxyz'

def check(chars, repeat):
    pws = product(chars, repeat = repaet)

    for pw in pws:
        if ''.joim(pw) == target:
            return ''.join(pw)

pw = check(chars, 4)

if (pw is None):
    print('failure')
else:
    print(pw)
