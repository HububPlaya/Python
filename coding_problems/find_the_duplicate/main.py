# this is the find the duplicate problem

# given an unsorted array array of positive integers -> nums
# such that the value is in the range [1 -> n -> n + 1] 
# find and return the duplicate in nums

# EX 1 3 3 4 2 5 
# output: 3

# EX 1 5 3 4 2 5
# output: 5 

# this is what I would do

# find the len(nums) -> loop through an array 1 - n
# loop through the array using some range
# Create the fast and slow pointer at the beginning index 
# 1 2 3 3 4 5 
# f,s
# increment f -> 2, and increment s -> 1
# 1 2 3 3 4 5 
#   s   f   
# 1 2 3 3 4 5 
# f   s
# 1 2 3 3 4 5 
#       f,s

# add the number in both from f and s

# 1 5 3 4 2 5
# f,s
# 1 5 3 4 2 5 
#   s   f
# 1 5 3 4 2 5
# f   s
# 1 5 3 4 2 5
#     f s
# 1 5 3 4 2 5
#         s f
# 1 5 3 4 2 5

# solution

def find_duplicate(nums):
    # fast and slow start at the beginning
    fast = slow = nums[0] 
    # detects the cycle
    while True:
        # fast -> 2 steps slow -> 1 step
        # if they meet we know there is a cycle 
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Find the entrance to the cycle (duplicate element)
    # we set slow back to 0 and keep fast the same 
    # we want to move both 1 step forward so that when they met we know which is the duplicate 
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast
