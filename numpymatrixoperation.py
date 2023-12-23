import numpy as np 

def input_matrix():
    rows = int(input("enter the number of rows: "))
    cols = int(input("enter the number of colomns: "))

    matrix = []
    print("enter elements row - wise: ")
    for i in range(rows):
       row = list(map(int, input().split()))
       matrix.append(row)

    return np.array(matrix)   


print("====matrix operation using NUMPY=========\n")
print("enter the elements of matrix 1: ")
matrix1 = input_matrix()

print("enter the elements foir matrix 2: ")
matrix2 = input_matrix()

while(1):
    print("1.MATRIX ADDIUTION \n 2. MATRIX SUBTRACTION \n 3 .MATRIX MULTIPLICATION \n 4. TRANSPOSE \n")
    choice = int(input("enter the choice(1-4)   to perform:  "))

    if choice == 1:
        print("matrix addition: \n",matrix1 + matrix2)
    elif choice ==2:
        print("matrix sub:\n ",matrix1 - matrix2)
    elif choice ==3:
        print("multiplication: \n", np.dot(matrix1, matrix2))
    elif choice == 4:
        print("transpose of matrix is :\n ", matrix1.T & matrix2.T)
        break
    else:
        print("enter the corect choice") 
    print("EXIT")           