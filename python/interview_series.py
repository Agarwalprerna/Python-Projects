#1                                                             . converting an integer into decimals

# import decimal
# z = "12345.33"  #string of integers or any integer
# print(decimal.Decimal(z))
# print(type(decimal.Decimal(z)))

#                                                    2. reversing a string using slicing technique
# str = "python"
# print(str[::-1])

#                                                          3. counting vowels in a given word
# vowels = ['a' , 'e', 'i', 'o','u']
# word= "prernaagarwal"
# count=0
# for i in word:
#     if i in vowels:
#         count +=1
        
# print(count)        

#                                                4 counting no. of occurences of a charachter in a string
# str = "prernaagarwal"
# charachter = "a"
# count=0
# for i in str:
#     if i ==charachter:
#         count+=1

# print("charachter \'a\' in str", count)

#...........................................................fibonacci series.......................................................

# fib = [0 ,1]

# for i in range(5):
#     fib.append(fib[-1] + fib[-2])

# #converting list into string  
# print(',' .join(str(e) for e in fib))

#...................................................... middle element of list

# list = [2,4,7,19,30]
# z = int(len(list) / 2)
# print(list[z])

#.....................................................converting a list into string
list = ["p",'r','e','r','n','a']
string = "".join(list)
print(string)
print(type(string))

#.................................................adding 2 list elements togetherly
#kind of matrix addition 
list1 = [3, 4, 6]
list2 = [ 2, 1, 9]
result = []

for i in range(0 , len(list1)):
       result.append(list1[i] + list2[i])

print(result)       