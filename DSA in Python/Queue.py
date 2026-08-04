#1.
'''
from collections import deque

queue = deque()

queue.appendleft("a")
queue.appendleft("b")
print("poped element:  " ,queue.popleft())   #speed is  O(1) for popleft() and append() in deque
print("updated queue: ",queue)

print("length of queue: ",len(queue))

print(queue[0])  
'''

#2. using Class

from collections import deque

class Queue:

    def __init__(self):
        self.buffer = deque()  #empty queue

    def enqueue(self, val):
        self.buffer.appendleft(val)
        print(f" Enqueued {val} -> Queue: {list(self.buffer)}")  #list mein converted

    def dequeue(self):
        if len(self.buffer) != 0:
            val = self.buffer.popleft()   
            print(f"Dequeued {val} -> Queue: {list(self.buffer)}")
            return val
        else:
            print("Dequeue attempted: queue is empty")     

    def size(self):
        return len(self.buffer)



O1 = Queue()

O1.enqueue(5)
O1.enqueue(7)
O1.enqueue(9)
O1.dequeue() 
print("size of Queue: " , O1.size())


    
