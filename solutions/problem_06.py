'''
COMP 125 - Programming Jam Session #1
November 9-10-11, 2020

-- Problem 6 --
Assume there are two variables, k and m, each already associated with a positive integer value and further assume that k's value is smaller than m's. Write the code necessary to compute the number of perfect squares between k and m. (A perfect square is an integer like 9, 16, 25, 36 that is equal to the square of another integer (in this case 3*3, 4*4, 5*5, 6*6 respectively).) Associate the number you compute with the variable q. For example, if k and m had the values 10 and 40 respectively, you would assign 3 to q because between 10 and 40 there are these perfect squares: 16, 25, and 36.
'''
import math

# k -> start
# m -> end
# q -> count
start = 10
end = 40
count = 0

# same logic as problem 5, except this time we give start and end points to range() and only count the number of perfect squares
for num in range(start, end):
    if math.sqrt(num) % 1 == 0:
        count += 1

print(count)

