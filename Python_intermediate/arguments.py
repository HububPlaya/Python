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
print_name(set_month="August", day='13', year="2003") #this gave me a type error

# Ex 3: default: regular arguments that don'care about order or initlialization
def print_name(firstName, lastName):
    print(firstName + lastName)
print_name()
