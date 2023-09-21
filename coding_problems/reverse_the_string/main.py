"""
This is the reverse the string problem
Given a sentence, reverse the order of the words without affecting the order of the letters
constraints: can be letters or digits upper and lower case and contain white space 
"""

# My solution: Wrong

# Ex 1: Hello world -> world Hello

# how would I accomplish this?

# the most obvious is to replace the letters until the middle 
# H <-> d

# the move foward in both directions
# if they are the same keep the letter dont swap and move forward
# e <-> l, case: 1 <-> 1 stays same, l <-> r, o <-> w
# ouput: d l r o w  o l l e H 

# when both sides equal each other make the string a list and use the reverse method

"""def reverse_string(s):
    left = 0
    right = len(s) - 1
    s = list(s)  # Convert the input string to a list to make it mutable

    while left < right:
        if s[left] != s[right]:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        else:
            left += 1
            right -= 1

    reversed_string = ''.join(s)  # Convert the list back to a string
    return reversed_string

print(reverse_string('Hello World'))"""

# correct solution:

def reverse_words(sentence):
    # split the sentence into words 
    words = sentence.split()

    # reverse the words 
    reversed_words = words[::-1]

    # put the words back into the sentence
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

# Example usage:
original_string = "hello world"
reversed_result = reverse_words(original_string)
print(reversed_result)  # Output: "world hello"




