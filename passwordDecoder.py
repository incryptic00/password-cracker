from termcolor import cprint
from colorama import init
from time import time
init()

db = 'hashed-passwords.txt'
passwordList = open(db, 'r', encoding='utf-8').readlines()

def crack(target):
    for x in passwordList:
        password = x.replace('\n', '').rsplit(',', 1)
        if target == password[1]:
            return password[0]

    return False


while True:
    target = input('Enter hash: ')

    start = time()
    pswd = crack(target)
    end = time() - start

    if pswd:
        cprint(pswd, 'green')
    else:
        cprint('password not found. :(', 'red')

    print(f'{end}s')