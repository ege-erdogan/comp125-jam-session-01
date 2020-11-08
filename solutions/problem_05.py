'''
COMP 125 - Programming Jam Session #1
November 9-10-11, 2020

-- Problem 5 --
Assume there is a variable, h already associated with a positive integer value. Write the code necessary to compute the sum of the perfect squares whose value is less than h, starting with 1. (A perfect square is an integer like 9, 16, 25, 36 that is equal to the square of another integer (in this case 3*3, 4*4, 5*5, 6*6 respectively).) Associate the sum you compute with the variable q. For example, if h is 19, you would assign 30 to q because the perfect squares (starting with 1) that are less than h are: 1, 4, 9, 16 and 30==1+4+9+16.
'''
import math

# I will use more explanatory names for h and q:
# h -> limit
# q -> total
limit = 26
total = 0

# iterate over all integer until the limit
#   add number to total if it is perfect square
# there are different ways to check if a number is a perfect square. Below, a number is considered a perfect square if its square root is a whole integer (i.e. has no remainder when divided by 1)
for num in range(limit):
    if math.sqrt(num) % 1 == 0:
        total += num

print(total)


