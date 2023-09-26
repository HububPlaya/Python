# create a function that takes the head of the linked list, and return the middle of the linked list
# if the linked list has an even amount of nodes, return the second middle node 

# create two pointers slow and fast at the head of the linked list 
# traverse the list: slow pointer -> moves 1 and fast pointer -> moves 2
# when the fast pointer reaches null -> slow pointer is at the middle 
# return the node at the slow pointer 

from linked_list import LinkedList

# create a function that takes the head of the linked list, and return the middle of the linked list
# if the linked list has an even amount of nodes, return the second middle node 

# create two pointers slow and fast at the head of the linked list 
# traverse the list: slow pointer -> moves 1 and fast pointer -> moves 2
# when the fast pointer reaches null -> slow pointer is at the middle 
# return the node at the slow pointer 

def get_middle_node(head):
    if head is None:
        return None

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

    # Replace this placeholder return statement with your code