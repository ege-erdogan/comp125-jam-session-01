'''
COMP 125 - Programming Jam Session #1
November 9-10-11, 2020

-- Problem 8 --
You work for a bakery that sells two items: muffins and cupcakes. The number of muffins and cupcakes in your shop at any given time is stored in the variables muffins and cupcakes, which have been defined for you.
Write a program that takes strings from standard input indicating what your customers are buying ("muffin" for a muffin, "cupcake" for a cupcake). If they buy a muffin, decrease muffins by one, and if they buy a cupcake, decrease cupcakes by 1. If there is no more of that baked good left, print ("Out of stock").
Once you are done selling, input "0", and have the program print out the number of muffins and cupcakes remaining, in the form "muffins: 9 cupcakes: 3" (if there were 9 muffins and 3 cupcakes left, for example).
'''

muffins = 5
cupcakes = 2

bought_product = ''
while bought_product != '0':
    bought_product = input('Enter your order: ')
    if bought_product == 'muffin':
        if muffins == 0:
            print('Out of stock.')
        else:
            muffins -= 1
    if bought_product == 'cupcake':
        if cupcakes == 0:
            print('Out of stock.')
        else:
            cupcakes -= 1
    
print(f'muffins: {muffins}, cupcakes: {cupcakes}')
    