#stack  can be implemented using list 
# 1.---------- using list as stack -------------'''
"""
stack = []
stack.append(2)
stack.append(9)
stack.append(10)
            
print("initial stack: ", stack)

#pop operation
c = stack.pop()
print(f"popped element = {c}")
print("stack after pop operation: ", stack)

#top element
top_element = stack[-1]
print(f"peek top element= {top_element}")

is_empty = len(stack)==0
print(f"is stack empty? {is_empty}")

#The issue with using a list as a stack is that list uses dymanic array internally and 
# when it reaches its capacity it will reallocate a big chunk of memory somewhere else in memory area 
# and copy all the elements. 

#2.---------- using collections.deque as stack----------

from collections import deque

stack2 = deque()

stack2.append("y")
stack2.append("z")
stack2.append("w")

print("initial stack2: " , stack2)
popped = stack2.pop()
print("popped element = " , popped)
popped = stack2.pop()
print("popped element = ",popped)
stack2.pop()
print(stack2)

stack2.pop()
#stack2.pop()  # this will raise an error as stack is empty now

"""


#3.--------------using class -------------------------------
from collections import deque


class stack:
    def __init__(self):
        self.items = deque()

    def push(self, value):
        self.items.append(value)
        print(f"Pushed {value} -> Stack: {list(self.items)}")  #list mein converted
        return value

    def pop(self):
        if len(self.items) != 0:
            val = self.items.pop()
            print(f"Popped {val} -> Stack: {list(self.items)}")
            return val
        else:
            print("Pop attempted: stack is empty")
            return "stack is empty"
        
    def peek(self):
        if len(self.items) != 0:
            print(f"Peek: {self.items[-1]}")
            return self.items[-1]
        else:
            print("Peek attempted: stack is empty")
            return "stack is empty"                      

    def is_empty(self):
        result = len(self.items) == 0
        print(f"is_empty? {result}")
        return result
    
    def size(self):
        result = len(self.items)
        print(f"Size: {result}")
        return result


# object demo (methods print their own outputs)
def main():
    s = stack()
    s.push(10)
    s.push(20)
    s.push(200)
    s.peek()
    s.pop()
    s.is_empty()
    s.size()


if __name__ == "__main__":
    main()
