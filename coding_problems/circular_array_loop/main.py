# this is the circular array loop problem
# An array nums with non-zero integers is given 
# The value of the index represents the number of places to skip forward if the value is positive or backwards if negative
# when moving forwards and backwards, wrap around if you reach either end of the array

# determine if the circular array has a cycle
# same set of indices repeated when either side wraps around when it reaches the end of the array
# the length is atleast 2
# must go in a single direction 

# EX input: 1 3 -2 -4 1

# we enter the first spot -> 1 (move one spot) -> 3 (move three spots) -> 1 (value where we started)
# output: True

# EX input: 2 1 -1 -2 2

# the first spot -> 2 (move 2 spots) -> -1 (move 1 spot back) -> 1 (move 1 spot forward) -> infinite loop between 1 and -1
# output: False



def circular_array_loop(nums):
    size = len(nums)
    
    for i in range(size):
        slow = fast = i
        forward = nums[i] > 0
      
        while True:
            slow = next_step(slow, nums[slow], size) 
            if is_not_cycle(nums, forward, slow):
                break
        
            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break
            
            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break
        
            if slow == fast:
                return True
                
    return False


def next_step(pointer, value, size):
    result = (pointer + value) % size
    if result < 0:
        result += size
    return result


def is_not_cycle(nums, prev_direction, pointer):
    curr_direction = nums[pointer] >= 0
    if (prev_direction != curr_direction) or (abs(nums[pointer] % len(nums)) == 0):
        return True
    else:
        return False


