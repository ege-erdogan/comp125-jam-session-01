'''
COMP 125 - Programming Jam Session #1
November 9-10-11, 2020

-- Problem 2 --
You have to do your chemistry homework, but you hate looking up elements on the periodic table! Write a program that takes the name of an element (as a string, independent of case) from standard input and prints a double representing its atomic weight to standard output. Only implement the program for the first three elements, hydrogen, helium, and lithium, which have the respective atomic weights 1.008, 4.0026, and 6.94. If anything else is given as input, print the statement "Sorry, I don't recognize that element!"
'''
weights = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
}

user_query = input('Enter an element name: ').lower()

if user_query in weights.keys():
    print(weights[user_query])
else:
    print("Sorry, I don't recognize that element!")