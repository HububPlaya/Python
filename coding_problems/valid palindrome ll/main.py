"""
This is the valid palindrome problem part 2
A palindrome is a word that is spelt the same forwards and backwards
Write a function that that takes a stirng, check if its a palindrome by remove at most one character
"""

# Ex 1: a b c e b a

# check both sides 
# [0]a, [1]b, [2]c, [3]e, [4]b, [5]a
# [0] <-> [5] and [1] <-> [4]

# we need to remove the index at [3] or [4]
# [1], [2], [5]

#return new string 

# Ex 2: d e e a d 

# [0]d, [1]e, [2]e, [3]a, [4]d

# if I check both sides
# [0] <-> [4]
# [1] != 3
# check if [3] is = [4], then check if [3] is = [1]
# if true then remove the index before [3]
# if not remove [3]

# Ex 3: r a c e a c a t

# [0]r, [1]a, [2]c, [3]e, [4]a, [5]c, [6]a, [7]t
# raceacat = tacaecar output: false

# check both sides 
# [0] != [7] but they need to check more 
# [1] <-> [6], [2] <-> [5]

# what do I notice: 

# when is it usually not a palindrome:

# if the first and last letter don't match
# if the letter after first letter and before first letter 

# How do I solve this problem:

# string s = something 
# split string s in half 
# reverse the halfs 
# put them in a new string 
# if the new string = old string 

def valid_palindrome(string):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    
    left = 0
    right = len(cleaned_string) - 1

    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1

    return True

# Example usage:
input_string = "A man, a plan, a canal: Panama"
result = valid_palindrome(input_string)
print(result)  # Output: True

        
    








