This file will calculate the difference (in seconds) between two primes calculator/generator algorithms.

The first algorithm is the fastest algorithm to calculate if a number is prime or not. It use the root of the number and check if a number is even or not (all even numbers - except 2 - isn't a prime number)

    Example: If we want to know if 100 is a prime number or not, the algorithm will check if it is an even number and > 2, and done, it isn't a prime number.
    Now, if we want to know if 77 is a prime number or not, the algorithm will check doing divisors using the root until the number 3.
    Int root of 77 is: 8. Ok, now we need to divide 77 by 8, 77 by 7 ... and ops, an integer division (77 / 7 = 11), we got! So, 77 ins't a prime number.

The second algorithm is a slower algorithm to do that. It will runs starting at one number lowest of the number we want to check if it is prime or not.

    Example: If we want to know if 77 is a prime number or not, we need to do a lot of divisions.
    We start with 77 by 76, 77 by 75, 77 by 74 ... until we got a divisor that can do an integer division.

Here we have tested the fastest and the lowest methods. Of course that exists a lot of algorithms between these two methods (like using the half the number until number 3 and using even_check). 