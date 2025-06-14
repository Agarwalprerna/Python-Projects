#..................................................... create  a class -named "" car ""  and its object

# class car:
#     def __init__(self ,model ,color):
#         self.model = model
#         self.color = color

#     def __str__(self):
#         print(f"{self.model}{self.color} is starting")    


# #creating object
# car1 = car("BYD","black")  
# car2 = car("nexon","black")      
# print(car1.model)              #printing particular attribute
# car.color = "blue"     #chaging value of attribute


# ...............................................................................inheretance
# class person:
#     def __init__(self , fname , surname):
#         self.fname = fname
#         self.surname = surname
    
#     #printname is a method
#     def printname( self):
#         print(self.fname , self.surname)


# #child class
# class student(person):
#     def __init__(self, fname, surname):
#         super().__init__(fname, surname,)
#         self.age = 12  #adding property "age" 

#     #adding method 
#     def welcome(self):
#         print("welcome" , self.fname ,"to the class")  


# #object of childe class
# x = student("mike","olsen")           
# x.printname()
# print(x.age)
# x.welcome()

# #............................................................................ITERSTORS AS OBJECT    

# # to print numbers 1,2,3,.....20 create iterator

# #iterators are implemented as classes
# class num:
#     def __iter__(self):
#         self.a =1
#         return self
    
#     def __next__(self):
#         if self.a <=20:
#             x = self.a
#             self.a +=1
#             return x
#         else:
#             raise StopIteration
        
# #creat object  and convert objects into iterable
# z = num()        
# myiterable = iter(z)
# print(next(myiterable))

# for x in myiterable:
#     print(x)


#......................................................POLYMORPHISM.................................

# class car:
#     def __init__(self , brand , color):
#         self.brandname = brand
#         self.color = color

#     def move(self):
#         print("drive the vehicle")    

# class boat:
#     def __init__(self , brand,color):
#         self.brandname = brand
#         self.color = color

#     def move(self):
#         print("sail")   


# #objects of both classes

# car1 = car("ford" , "red")        
# boat1 = boat("ibiza" , "white")                

# car1.move()
# boat1.move()

#............................................ inheretance class in polymorphism

class vehicle:
    def __init__(self , brand , color):
        self.brandname = brand
        self.color = color

    def move(self):
        print("drive the vehicle")    

#child classes
class bike(vehicle):
     def move(self):
        print("fleet")

class boat(vehicle):
     pass

class auto(vehicle):
     def move(self):
          print("go ")
          

#objects

bike1 = vehicle("activa" ,"black")   
auto1 = vehicle("bajaj" ,"green")   
boat1 = vehicle("ibiza" ,"grey")    

boat1.move()