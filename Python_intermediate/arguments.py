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

# make a function that shortens words to 8 characters 

#length and loop through the args 
# the colon with brackets means it creates a substring up to the but not including the length
def truncate_sentence(length, *words):
    for word in words:
        print(word[:length])

truncate_sentence(8, "I love the park", "I love school so much") 

# Create a dictionary of tables 1 - 7 that holds the name, Vip_status, and order
tables = {
    1: {
        'name': 'Keelan',
        'vip_status': True,
        'order': 'Orange Juice'
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {}
}

# Create a function to assign tables
def assign_table(table_number, name, vip_status):

    # Check if the table_number exists in the tables dictionary
    if table_number in tables:
        # Assign the customer's name to a specific table
        tables[table_number]['name'] = name

        # Assign the customer's vip_status to the specific table
        tables[table_number]['vip_status'] = vip_status

        # Assign the customer's order for the specific table
        # It's initially blank so we can update it
        tables[table_number]['order'] = ''
    else:
        print(f"Table {table_number} does not exist.")

# Create a function that assigns and prints the order
def assign_and_print_order(table_number, *order_items):

    # Check if the table_number exists in the tables dictionary
    if table_number in tables:
        # Update the order attribute to hold multiple orders
        tables[table_number]['order'] = order_items

        # Loop and print each item from the multiple items
        print(f"Order for Table {table_number}:")
        for ordered_item in order_items:
            print(ordered_item)
    else:
        print(f"Table {table_number} does not exist.")

# Test 1
assign_table(12, 'Keelan', True)
assign_and_print_order(12, 'Lobster', 'Salmon', 'Salad')





