'''
COMP 125 - Programming Jam Session #1
November 9-10-11, 2020

-- Problem 2 --
You have to do your chemistry homework, but you hate looking up elements on the periodic table! Write a program that takes the name of an element (as a string, independent of case) from standard input and prints a double representing its atomic weight to standard output. Only implement the program for the first three elements, hydrogen, helium, and lithium, which have the respective atomic weights 1.008, 4.0026, and 6.94. If anything else is given as input, print the statement "Sorry, I don't recognize that element!"
'''

# define a dictionary to hold atomic weight values.
atomic_weights = {
    'hydrogen': 1.008,
    'helium':   4.0026,
    'lithium':  6.94,
    # ... can include other elements here
}

# take user input. Note that input type is string by default
user_query = input('Enter an element name: ')

# strip() method removes spaces at the beginning and end of string
# lower() method converts all letters to lowercase
# note that they do not modify the string in-place, they "return" the value
user_query = user_query.strip().lower()

# check if query is a key in dictionary
#   if so, print the corresponding value
#   if not, print the error message
if user_query in atomic_weights.keys():
    print(atomic_weights[user_query])
else:
    print('Sorry, I don\'t recognize that element!')

# alternatively, dictionaries in Python have a useful setdefault() method that lets us specify a default value if key is not in the dictionary. You don't have to know this though. I found about it while writing this solution :)
#   print(atomic_weights.setdefault(user_query, "Sorry, I don't recognize that element!"))
