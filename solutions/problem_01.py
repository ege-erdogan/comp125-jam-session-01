'''
COMP 125 - Programming Jam Session #1
November 9-10-11, 2020

-- Problem 1 --
Write a program that assigns two integer values from standard input to the variables int1 and int2, then prints "True" if they are equal, "False" if they are not.
'''

# take two integer inputs (ask again if input not integer).
#   can also have two while loops so that if second int() call gives error, only the second input is repeated. 
#   I put them in same while loop to keep the code shorter.
while True:
    try:
        int1 = int(input('Enter the first integer: '))
        int2 = int(input('Enter the second integer: '))
        break
    except:
        print('You did not enter an integer. Starting again...\n')
    
# check if they are equal, then print the appropriate message
if int1 == int2:
    print(True)
else:
    print(False)

# alternatively, to print the output, we could simply say:
#   print(int1 == int2)
# the if-else version is easier to extend with different messages though, so I chose that. 