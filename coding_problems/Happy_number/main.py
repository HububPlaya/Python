
#This is the happy number problem

#instructions:
#Write an algorithm that determines if n is a happy number, use these steps:
#1. starting at n, replace it with the number that is the sum of the squares of its digits 
#2. if the number == 1, n is a happy number 
#3. else, not a happy number 


# Ex1: 
# 23 -> 2 ** 2 + 3 ** 2 = 13  
# 13 -> 1 ** 2 + 3 ** 3 = 10 
# 10 -> 1 ** 2 + 0 ** 2 = 1
# output: true

# Ex2:
# 2 -> 2 ** 2 = 4
# 4 -> 4 ** 2 = 16
# 16 = 1 ** 2 + 6 ** 2 = 37
# this keeps going output: false

 #first break down the number into digits
    # create a fast and slow pointer (start)
    # we want the fast pointer to go after the slow one 
    #   slow   fast
    # 1  2   3   4   5 
   # take the digits and square each one, then add those digits together 
   # if the sum ever equals 1 return true
   # else return false


  # This is a far as I could get lol
  # def is_Happy_Number(n):
  # fast = 0
 #  slow = 0
  # string_n = str(n)
  # for char in string_n:
   #   fast += slow
      #slow += 1
      #if 


# solution givem:

def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    
    return n == 1

print(is_happy(100))