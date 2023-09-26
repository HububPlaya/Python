# This is the linked list cycle problem 

# check whether or not the linked list contains a cycle 
# if the cycle exist, return true 
# else return false

# a cycle means that at least one node can be reached by a next pointer 

# Ex: 2 -> 4 -> 6 -> 8 -> 10 -> 4 // cycles back to 4
# Ex: 2 -> 4 -> 6 -> 8 -> 10 -> null // returns false

# steps to solve problem:

# intialize a fast and slow pointer 
# move the slow pointer once, the fast pointer twice 
# if they point to the same node -> true 
# else return false 

from linked_list import LinkedList
from print_list import *

def detect_cycle(head):
    if head is None:
        return False

    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

