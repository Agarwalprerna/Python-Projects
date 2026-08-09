
class HashTable:
    def __init__(self):
        self.max = 20
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:   #key is a string here
            h += ord(char)  #ord gives the ascii value of the character    
        return h % self.max

    def __setitem__(self,key , value):
        h = self.get_hash(key)
        #self.arr[h] = value

        found = False
        for idex, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idex] = (key, value)
                found = True
                break
            if not found:
                self.arr[h].append((key,value))  #appending the key value pair to the list at that index 

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None


o1 = HashTable()        
print("index: ", o1.get_hash("march 9"))
o1["march 9"] = 130
o1["march 10"] = 20
print(o1.arr)
del o1["march 10"]
print(o1.arr)

o1["march 10"]= 38
o1["march 12"]= 67
print(o1.arr)