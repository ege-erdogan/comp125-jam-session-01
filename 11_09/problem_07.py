'''
COMP 125 - Programming Jam Session #1
November 9-10-11, 2020

-- Problem 7 --
Given a positive integer n, assign True to is_prime if n has no factors other than 1 and itself. (Remember, m is a factor of n if m divides n evenly.)
'''
import math

n = 26
is_prime = True

if n > 2 and n % 2 == 0:
    is_prime = False
else:
    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            is_prime = False
            break

print(is_prime)