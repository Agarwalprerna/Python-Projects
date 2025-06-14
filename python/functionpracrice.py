#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ganesh Fashion
#
# Created:     11/07/2023
# Copyright:   (c) Ganesh Fashion 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#sum of all numbers

'''def sum(*numbers):
    total =0
    for x in numbers:
        total += x
    return total

#print("sum of numbers = ")
#sum(8,2,3,0,7)
#print(sum)

#multiply all the numbers in the list

def multiply(*numbers):
    total =1
    for x in numbers:
        total*= x
    return total
#print(multiply(8,2,3,-1,7))

#factorial of a number
def factorial(a):
    fact = 1
    for i in range(1,a+1):
        fact*=i
    return fact
#print(factorial(5))

#take a list and return a new list with no duplicate terms

def unique_list(L):
    a = []
    for x in L:
        if x not in a:
           a.append(x)
    return a
#unique_list([1,2,4,4,5,6,6])
#print(unique_list)

#check a number prime or not
def prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for x in range(2,n):
            if (n% x==0):
                return False
        return True
#print(prime(27))

#print even numbers from list
def newlist(l):
    a = []
    for x in l:
        if x %2 ==0:
            a.append(x)
    return a

#print("even no. are ")
#print(newlist([1,2,3,4,5,6,7,8,9]))


#perfect no, or  not
def perfect(n):
    sum =0
    for x in range(1,n):
        if n % x==0:
            sum+=x
    return sum ==n
#print(perfect(28))


#create a list which contain squares of numbers from 1 - 20
def newlist():
    a = []
    for x in range(1,21):
        a.append(x**2)
    return a
#print(newlist())


def func(n):
    return lambda a : a*n

#doubler = func(2)
#triple = func(3)
#quadruple = func(4)
#print(doubler(15));print(triple(15));print(quadruple(15)

##lambda function to sort the list of tuples
#list1 = [("english",67),("maths",89),("hindi",80)]
#print("list1 : ")
#print(list1)

#list1.sort(key = lambda x : x[1])
#print("\nsortening of list of tuples: ")
#print(list1)

#lamba function to sort dictionary of list
#info = [{'name':'ram',"age":5,"city":'surat'},{'name':'gunnu','age': 30,'city': "delhi"},{'name':'roy',"age":12,"city": "mumbai"}]
#print("original list: "); print(info)

#sorted_list = sorted(info,key= lambda x :x["age"])
#print("\nsorted list: ");print(sorted_list)

#to display current date and time
"""import datetime
now = datetime.datetime.now()
print("current time and date: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))"""

#user first name and last name in reverse order and space between them
"""fname = input("enter your first name: ")
lname = input("enter your last name: ")
print(lname + " "+ fname)"""

#accept comma seprator numbers from user and generate a list and tuple of numbers
"""values = input("enter few numbers by using comma to seperate them: ")
unique_list = values.split(",")
print(unique_list)
x = tuple(unique_list)
print(x)"""

#enter filename and output should be extension of the file
"""x = input("enter any filename using dot extension: ")
file_extension = x.split(".")
print("the extension of file : "+ file_extension[-1])"""

#print first and last element in list
"""colours = ['red','green','white','black']
x = colours[0] ; y = colours[-1]
print(x + " " + y)"""


"""exam_date = (11,12,2014)
print("the examination starts from: %i/%i/%i"%exam_date)"""

#string formating using %s operator
"""str1 = "hyy"
str2 = 'programmmer'
list = ""2 ,4,1]
final_str = "%s %s = %s"%(str1,str2,list)
print(final_str)"""


#reverse a sring by slicing
"""def reverse(a):
    return a[::-1 ]
print("reveerse of string: ")
print(reverse("prerna")) """

#count no of uppeer and lower cases in string
'''def countstring(str):
    dict = {"upper_case": 0,"lower_case": 0}
    for i in str:
        if i.isupper():
            dict["upper_case"] += 1
        elif i.islower():
            dict["lower_case"]+=1
        else:
            pass

    print("original string: ",str)
    print("no. of upper case: ",dict["upper_case"])
    print("no. of lower case: ",dict["lower_case"])

countstring("The Quick Brown Fox")'''

#{}
'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)'''

#arra quesion
"""from array import *
arr_num = array('i',[1,3,5,7,9])
print("original arr: "+str(arr_num))
arr_num.reverse()
print("new arr: "+str(arr_num)) """

#reverse of uple
"""a = (1,2,3,4,5)
print(a[::-1])"""

"""list =[1,2,4,6]
sum=0
for x in list:
    sum+=x
print("sum of elemens:%s" %sum)"""


#swap firs and las iems in lis
'''def swap_lis(unique_list):
    size = len(unique_list)
    c = unique_list[0]
    unique_list[0]= unique_list[size-1]
    unique_list[size-1] = c
    return unique_list

unique_list= [12,35,3,8,24]
print(swap_lis(unique_list))'''

#ieraion
'''class range:
    def __init__(self, n):
        self.i =0
        self.n = n
    def __iter__(self):
        return self

    def __next__(self):
        if self.i<self.n :
            i = self.i
            self.i+= 1
            return i
        else:
            raise StopIteration

N= range(3)
myiter  = iter(N)

print(next(myiter))
print(next(myiter))'''

#genraor que
"""def pow2gen(max=0):
    n=1
    while n<max :
        yield 2**n
        n+=1

for x in pow2gen(6):
    print(x)"""


#RegEX que
msg = "the programmer needs much practise to become a developer"


x = re.sub("\s","00",msg,3\)
print(x)'''

#pip
'''import camelcase
x = camelcase.CamelCase()
msg = "i am prerna"
print(x.hump(msg))'''

#(list) input
'''list = []
n = int(input("enter no. of elements: "))

for i in range(0 ,n):
   x = input()
   list.append(x)

list= [list.capitalize() for list in list]
print(list)'''

#reverse an ineger

'''a= 123
print(str(a)[::-1])'''

def fibonacci(n):
    # return a list of fibonacci numbers
    LIST= [0,1]

    SUM =0
    for x in range(2,n):
        sum +=1
        list.append(sum)
    return LIST

fibonacci(5)

















