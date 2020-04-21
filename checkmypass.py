"""
This is a program that will check how many times probably your password was exposed previously in data breaches.

Programmer: Hugo Leça Ribeiro
Date: 20/04/2020
"""

import requests
import hashlib
from time import sleep


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again.')
    return res


# This function will check how possibles times appears that password
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


# Response is ok if it is equal to 200.
def pwned_api_check(password):
    sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


# The main function here we will check each password inside the list of passwords.
def main(args):
    print('-' * 20)
    print(f'Ok. You inputted these passwords: {args}. \nLets begin the test.\n')
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... \033[1;31m you should probably change your password!\033[m')
        else:
            print(f'{password} was NOT found. \033[0;32mCarry on!\033[m')
        sleep(1)
    return '\nDone!'


# A function to capture each password and put it into a list (passwords)
def capture_passwords():
    passwords = list()
    affirmative = ['YES', 'Y']
    negative = ['NO', 'N']
    try:
        keep_going = True
        while keep_going:
            password = str(input('Input here a password: '))
            passwords.append(password)
            while True:
                going = str(input('Do you want to input another password? [Y/N] ')).upper()
                if going in affirmative:
                    break
                elif going in negative:
                    keep_going = False
                    break
                else:
                    print('Sorry, wrong key was inputted. Try again!')
        return passwords
    except:
        print('Ow no, something went wrong!')


# Main Program
list_passwords = capture_passwords()
print(main(list_passwords))
