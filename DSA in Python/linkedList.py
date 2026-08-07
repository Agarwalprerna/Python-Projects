
class Node:
    def __init__(self,data=None , next=None):
        self.data = data
        self.next = next  #pointer which holds the address of next node


class LinkedList:

    def __init__(self):
        self.head = None #head is the first node of linked list

    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('linked list is empty')
        else:
            itr = self.head
            llstr = ""  #empty string to store the linked list elements
            while itr:
                llstr +=  str(itr.data) + '-->'
                itr = itr.next
            print(llstr)        

    def insert_at_end(self, data):
        if self.head is None:  #empty linked list
            self.head = Node(data,None)
            return 

        #if not empty
        ptr = self.head
        while ptr.next:  #traverse till the last node
            ptr = ptr.next

        ptr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)    


    def getlength(self):
        count =0
        ptr = self.head
        while ptr:
            count += 1
            ptr = ptr.next
        return count    

    def remove_at(self,index):
        if index < 0 or index >= self.getlength():
            raise Exception("invalid index")

        if index == 0:   #head itself to be deleted
            self.head = self.head.next
            return 

        count =0
        ptr = self.head
        while ptr:
            if count == index -1:
                ptr.next = ptr.next.next
                break
            ptr = ptr.next  #else move to next node
            count += 1

    def insert_at(self, index,data):
        if index < 0 or index >= self.getlength():
            raise Exception("invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count =0
        ptr = self.head
        while ptr:
            if count == index -1:
                node = Node(data,ptr.next)
                ptr.next = node
                break
            ptr = ptr.next
            count += 1
            


o1 = LinkedList()
 
o1.insert_values([1,2,3,4,5])
o1.insert_at_beginning(6)    
o1.insert_at_beginning(7)  
o1.insert_at_end(8) 
o1.print()
print("length of linked list is: ",o1.getlength())
o1.remove_at(0)
o1.print()
o1.insert_at(3,9)
o1.print()