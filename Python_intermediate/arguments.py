"""
We're going to cover three types of arguments: positional, keyword, and default
"""

# Ex 1: positional: uses the first and last name as the order (order matters)
def print_name(firstName, lastName):
    print(firstName + lastName)
print_name("keelan", "moore")

# Ex 2: keyword: this is where we can redefine our arguments 
def print_birthday(set_month, day, year):
    print(set_month + day + year)
#print_name(set_month="August", day='13', year="2003") this gave me a type error

# Ex 3: default: regular arguments that don'care about order or initlialization
"""def print_name(firstName, lastName):
    print(firstName + lastName)
print_name()"""

"""
we can use the unpacking operator to use as many arguments as we want.
the print method in python uses the unpacking operator to use multiple arguments 
"""
# Ex 1: unpacking arguments 
def function_example(*args):
    print(args)

function_example("args", 12, False)

# Ex 2: unpacking arguments effciently 
def shout_strings(*args):
    for argument in args:
        print(argument.upper())

shout_strings('Working on', 'learning', 'argument unpacking!')

# ex 3: using mutiple arguments when unpacking 
# make a function that shortens words to 8 characters 

#length and loop through the args 
# the colon with brackets means it creates a substring up to the but not including the length
def truncate_sentence(length, *words):
    for word in words:
        print(word[:length])

truncate_sentence(8, "I love the park", "I love school so much")
