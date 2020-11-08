'''
COMP 125 - Programming Jam Session #1
November 9-10-11, 2020

-- Problem 7 --
Given a positive integer n, assign True to is_prime if n has no factors other than 1 and itself. (Remember, m is a factor of n if m divides n evenly.)
'''
import math

n = 5
is_prime = True

# There is a whole literature of primality tests. See this Wikipedia article if interested:
#       https://en.wikipedia.org/wiki/Primality_test
# We will do it the "dumb" way.

# filter out even numbers
if n % 2 == 0:
    is_prime = False

# check if any integer less than sqrt(n) divides n. If so, n is composite.  
for i in range(3, int(math.sqrt(n))):
    if n % i == 0:
        is_prime = False
        break # can exit loop since no need to check for larger numbers

print(is_prime)