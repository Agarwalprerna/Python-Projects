#calculator 

while 1:
    print("what operation would like to perform: ")
    print(" 1. ADDITION \n 2. SUBSTRACTION \n 3. MULTIPLICATION \n 4.DIVISION:")

    choice =int( input("enter the choice that is mentioned above: "))

    if choice ==1:
        x ,y = map(int,input("enter two numbers: ").split())
        print("result: ", x+y)
    
    elif choice ==2:
        x ,y = map(int,input("enter two numbers: ").split())
        print("result: ", x-y)
    
    elif choice ==3:
        x ,y = map(int,input("enter two numbers: ").split())
        print("result: ", x*y)
    
    elif choice ==4:
        x ,y = map(int,input("enter two numbers: ").split())
        print("result: ", x/y)
        break
    else:
        print("enter ther correct choice")
print(" EXIT ")
    



