'''
COMP 125 - Programming Jam Session #1
November 9-10-11, 2020

-- Problem 3 --
Write an expression that evaluates to True if the int associated with number_of_prizes is divisible (with no remainder) by the int associated with number_of_participants. Assume that the latter is not zero.
'''

# initialize variables with values. could also ask for user input.
number_of_prizes = 40
number_of_participants = 10 

# parentheses are there to make the code easier to read. works fine without them
result = (number_of_participants != 0) and (number_of_prizes % number_of_participants == 0)

print(result)