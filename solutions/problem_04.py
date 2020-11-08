'''
COMP 125 - Programming Jam Session #1
November 9-10-11, 2020

-- Problem 4 --
Assume that a variable hoursWorked has been initialized. Write a statement that assigns the value True to the variable workedOvertime if hoursWorked is greater than 40 and False otherwise.
'''

hours_worked = 400

# we could also write an if-else statement in a similar situation with problem 1. 
# I chose this method here since we only want the truth value and nothing else.
worked_overtime = hours_worked > 40

print(worked_overtime)