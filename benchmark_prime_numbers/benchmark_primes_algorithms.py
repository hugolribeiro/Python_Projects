# Programmer: Hugo Leça Ribeiro
# Date: 07/17/2020

import time


# Generate prime numbers until the limit inputted - alg1
def infinite_prime(limit):
    number = 2
    while True:
        if verify_prime(number):
            yield number
        if number >= limit:
            break
        number += 1


# Verify if a number is prime or not (using root)
def verify_prime(num):
    if num % 2 == 0 and num > 2:
        return False
    root = int(num ** 0.5)
    for count in range(root, 3, -1):
        if num % count == 0:
            return False
    return True


# Verify if a number is prime or not (without root)
def verify_prime_noroot(num):
    for count in range(num - 1, 3, -1):
        if num % count == 0:
            return False
    return True


# Generate prime numbers until the limit inputted - alg2
def infinite_prime2(limit):
    number = 2
    while True:
        if verify_prime_noroot(number):
            yield number
        if number >= limit:
            break
        number += 1


# Calculate the duration of the first algorithm (with roots)
def duration_alg1(limit):
    t10 = time.time()
    for number in infinite_prime(limit):
        print(number)
    t11 = time.time()
    dif_time1 = t11 - t10
    print(f'Algorithm duration: {dif_time1} seconds')
    return dif_time1


# Count to separate tests
def regressive_count():
    for count in range(5):
        print(count, end="...", flush=True)
        time.sleep(1)
        print()


# Calculate the duration of the second algorithm (without roots)
def duration_alg2(limit):
    t20 = time.time()
    print('Starting the algorithm 2')
    for number in infinite_prime2(limit):
        print(number)
    t21 = time.time()
    dif_time2 = t21 - t20
    print(f'Algorithm duration: {dif_time2} seconds')
    return dif_time2


try:
    amount_primes = int(input('Input here how many prime numbers do you want to see: '))
    alg1 = duration_alg1(amount_primes)
    regressive_count()
    alg2 = duration_alg2(amount_primes)
    dif_algorithms = alg2 - alg1
    print(f'The difference between the algorithms is: {dif_algorithms} seconds')
except ValueError:
    print(f'Sorry, wrong value!')
except Exception as e:
    print(f'We got some error. {e}')