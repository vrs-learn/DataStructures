#
# Stack:
# We perform push/pop in Stacks. (LIFO - Last in first out)
# 
# Using array/linkedlist is not a good option. As everytime you need to access the last element, you would use O(n) complexity.
# In Stack, Push/Pop operation is O(1)
# & Search element by value is O(n)
#
# Use cases:
# Browser uses back button and forward button. Using back button we get the last page accessed. 
# Function calling in any programming language is managed using a stack.
# Undo (Ctrl + Z) functionality in any editor uses stack to track down last set of operations.
# 
# How to use stack in different languages:
# Python -> list, collections.deque, queue.LifoQueue
# Java -> Stack, Deque
# C++ -> std::stack
# 
# In python, using list is not recommended as the list is dynamic.
# As soon as the blocks in memory are exhausted, the list is copied to another location in memory, which is costly.
# ** IT IS RECOMMENDED TO USE collections.deque in python for using Stacks.
# As per the documentation, the deque is memory efficient with O(1) in both directions.
# 

from collections import deque

stack = deque()
stack.append("first element")
stack.append("second element")
stack.pop()

# A way of implementing a stack in literal terms:

class Stack:

    def __init__(self) -> None:
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container(-1)
    
    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


#
# Question: Implement a fucntion to reverse a string using stack data structure:
#

def reverse_string(text):
    s = Stack()
    for letter in text:
        s.push(letter)

    reversed_text = ""
    while s.size() > 0:
        reversed_text += s.pop()
    
    return reversed_text

user_string = "We will conquere COVI-19"
print(reverse_string(user_string))


    
