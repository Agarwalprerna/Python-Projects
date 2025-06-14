#simple 
#print("hello")

#muliple inputs
# a ,b,c = input("ener 3 numbers: ").split() 
# print("numbers are: ",a )
 
# x = [int(x) for x in input("enter 3 numbers: ").split()]
# print("numbers are: ",x)

# z = list(map(int, input("name 3 animals : ").split()))


# #quotation 
# name = 'prerna'
# name2 = "prerna"
# para = '''  i am 22 , i am pursuing elecrical engineering from SVNI sura '''

# sum = 8+
# 9+
# 12
# print(sum)

#use curly braces to continue with statement
# sum2 = (3+
#         3)
# print(sum2)

# days = 'mon', 'wed'            #for python line ends here
# 'sat' , 'fri'
# print(days)

#z =-3
#print(abs(z))

#no need to declare data type of variables
         #x and X are differen such that case sensitive
# x = 2.34e8 
# X = 67/2
# print(x)
# print(X)

#--------------------------------------------#tuples --------------------------------------------

tuple = ("prerna",22, "EE", 2026 )

# for x in tuple:
#     print(x)

# for i in range(0,2):              # till 0 and 1 index  , 2 index ko exclude krdia
#     print(tuple[i])  


# i=0
# while i < len(tuple):
#     print(tuple[i])
#     i= i+1

# print(tuple[2])
# print(tuple)
# del tuple
# print(tuple[-1])     # i wont print the desired element as we have already deleted the tuple

# tuple = ("prerna",22, "EE", 2026 , 7.99 )
# print(tuple[-2])
# print(tuple[1: ])
# print(tuple[0:2])           #2 index is not involved 

# #tuples are not changeable so we have to convert it into  "" lists ""
# z = list(tuple)
# z[1] = 19                 #changing value
# z.append("agarwal")      #adding value 
#             
# print(z)

#tuple2 = ("name",)
#tuple += tuple2               #adding 2 tuples
#print(tuple)

#packing of a tuple means assiging variables to the tuple
# (name ,*age, batch) = tuple 
# print(name)
# print(age)

#multiple = tuple*3
#print(multiple)

#to search particular element in a tuple 
# print(tuple.index(22))      # indeX() passes the index no. of particular search element
# print(tuple.index("EE"))    #use inverted comma for string values 
# print(tuple.count(2026))

#..............................................LIST..............................................................

#list = [ 1 ,4,56, "my","you",'we',3.00]
# print(list[:4])          #it always starts from 0 index whether you mentioned it or not
# print(list[-4:-2])       #-2 excluded

# if 'I' in list:
#     print("ok")

# list[2:4] = ["ee",19]     #change at index 2 and 3

# #change last element with 2 different values
# list[-1:-2]= [99 ,7.99]
# print(list)

# list.insert(3,"prerna")   #inseritng  ,remember at 3rd index value would not change just inserted 
# list.append("agarwal")       #always add at the end
# print(list)

#list2 = [5 ,6,1]
# list.extend(list2)     #adding list2 in list1 
# print(list)

# list.remove(3.00)   #specific value shouble be entered
# list.pop(5)   #just specify index
# print(list)

# for x in list2:
#     print(x)

# for i in range(0,4):
#     print(list[i])

# i=0
# while i <len(list):
#     print(list[i])
#     i=i+1

#creating new lsit form existing lsit
# newlist=[] 
# newlist = [x for x in list2]
# newlist = ["hyy" for x in list2]  
# print(newlist)  
# newlist = [x for x in range(4)]     #print number 0-3
# print(newlist) 

# list = [34 ,56,12,87,90]
# print(list.sort(reverse =True))   

# mylist = list.copy()
# print(mylist)

# list3 = mylist+ list          #concatenating
# print(list3)


#....................................................looping..................................................

# 1
# 2 2
# 3 3 3
# 4 4 4  4

# for i in range(1,5):
#     for j in range(i):
#         print(i,end=" ")
#     print()            #new line   

# list = ["red" , "rose"]
# for x in list:
#     print(x)
#     for i in x:
#         print(i)

# 10 -> 7-> 4->1  
# for i in range(10 ,0,-3):
#     print(i)

#even values 
# for i in range(0,10,2):
#     print(i)

# *
# * * *
# * * * * *
# k=1
# for i in range(1,4):
#     for j in range(1,k+1):
#         print("*",end=" ")
#     k=k+2
#     print()

# p
# p r
# p r e
# p r e r
# p r e r n
# p r e r n a

# string = input("enter name")
# x = len(string)
# for i in range(x+1):
#     for j in range(0,i):
#         print(string[j] , end= " ")
#     print()    

# 1
# 2 3
# 4 5 6
# 7 8 9 10
 
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k+=1
#     print()    

# A
# B C 
# C D E 
# D E F G
# E F G H I

# k=64
# for i in range(1,6):
#     k =64+i
#     for j in range(1,i+1):
#         print(chr(k) ,end=" ")
#         k=k+1
#     print()    

# suppose list = ["prerna " ,"agarwal", 22age , "batch "] only print prerna and age 

# list = ["prerna " ,"agarwal", 22, "batch "]
# for x in list:
   
#     if x =="agarwal":
#      continue
#     print(x)


#................................................. SETS.............................................................
set ={ 6 ,8,"a","a",1 ,True }            #1 and True are duplicate #unordered always remember
# for x in set:
#     print(x)

# set.add("I")
# set.remove(6)
# set.pop()         #will remove any item
# print(set)

# list = [1,2,5]
# set2 = {"i","up"}
# # set.update(list)   #add on list items in set
# # print(set)
# set3 = set.union(set2)  #add on another set elements but must define in another variable "set3" otherwise it wont give desired result 
# print(set3)

set2 = {8,6,"i","you",2 ,3}
# set.intersection_update(set2)   # keep only common items
# print(set)

# set.symmetric_difference_update(set2)    #remove common items
# print(set)

# set3 = set2.copy()
# print(set3)

# set.difference(set2)        #return  items that exist only in set not in set2
# print(set)

# set.difference_update(set2)        #return items of set only but after removal of common itmes between set1 and set2 
# print(set)



#.................................................DICTIONARIES..............................................

#dict2 = dict(name="prena", age=22, DOB=19, domain="EE")
# print(dict2)
# print(dict2["domain"])          #accessing the key 
#
#  print(dict2.keys())
#
#  print(len(dict2))
#
#  print(dict2.values())
#
#  print(dict2.items())

# if "name" in dict2:
#     print("OK ")

# dict2["name"]="pinku"           #change key value
#
#  dict2.update({"live": "surat"})  #add item
# print(dict2)

# dict2.pop("age")
# print(dict2)

# for x in dict2.values():
#     print(x)
# for x in dict2.keys():
#     print(x)    
# for x,y in dict2.items():
#     print(x,y)    


#nested dictionary

# school = {

#     "student": { 
#         "name" : "yash" ,
#         "class": 4 ,
#         "gender" : "male"},

#     "teachers" :{
#         "name": "mulla",
#         "age" : 56,
#         "gender": "male"
#     },    
# }

# print(school)
# print(school["teachers"]["age"])


#..................................................... Strings...............................................................
# a = "i hate you"

# for x in a:
#     print(x)

# print(a[2:6])                #6 is excluded
# print(a.upper())
# print(a.strip())

# b="forever"
# print(a+b)                  #concatenation

# c = 4
# text =  "i have been hating you since {} years"
# print(text.format(c))

# #print  i am AI "gemini" developed by google  -------> use escape charahcters
# str = " i am AI \"gemini\" developed by google"
# print(str)

# str2 = "have you lost your password ? \n [yes\\no]"
# print(str2)

#split method

# info = " employee ramesh age 45"
# print(info.split(","))            #no comma  would present between each values
# print(info.split())                 #comma will present


#..............................................................Arrays..........................................
#python does not have arrays as a object so we would use list instead if it

# define an array of names 
# list =[ "prerna" , "ishika ","tejas"]


#.............................................................FUNCTIONS.....................................................

# x = [1 ,6,4,99,13]
# print(min(x))
# print(max(x))

# y = 5
# print(oct(y))
# print(bin(y))

# 1. using arbitratry  argument positional  (*)

# def add(*num):
#     sum =0
#     for i in num:
#         sum+= i
#     return sum
    
# print(add(2,5,6,7,1,9))         #calling the function

#2.  using arbitratry  keyword argument  ( **)

# def fn(**a):
#     dict = a.items()
#     for i in dict:
#         print(i)

# fn( fruit="mango" ,vegetables="brinjal" )        

# 3. default parameter value

# def fn( country="india"):
#     print("i am from "+ country)

# fn()                 #no arguments was passed  , will use default paramter value
# fn("america")          # argument is passed

#4. recursion function

# def factorial(num):
#     if(num==1):
#         return 1
#     elif(num>1):
#         return  num* factorial(num-1)
  

# print(factorial(4) )    #calling the efunction

    

#.................................................. iterators.........................................................................
# list = [1, 3 ,5] 

# #instead of applying looping to access the list use this
# myiterable  = iter(list)      #convert to iterators

# print(next(myiterable))
# print(next(myiterable))

# we can use any pyhton object like lists , tuples ,sttrings , sets  and converting them into iterable objects

#......................................................GENERATORS........................................................................

# generators are like function that returns iterator using yeild keyword
# they are more easy to implement compared to iterators

# 1. sequence of numbers 

# creating generators
# def generator_num(n):
#     i=0
#     while i<n:
#         yield i
#         i+=1
# for i in generator_num(5):
#     print(i)

# 2.

# square_generator = (i*i for i in range(5))
# for i in square_generator:
#     print(i)

# 3. power of 2

def power_generator(max=0):
    i =0
    while i<max:
        yield 2**i
        i+=1

for x in power_generator(5):
    print(x)        