# dynamic array can be implemented using list in python

exp = [2200,2350,2600,2130,2190]

#Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

print(f" In feb you spent extra {exp[1]-exp[0]} dollars compare to january")

z = exp[0] + exp[1] + exp[2]
print(f" Total expense in first quarter is {z} dollars")

for x in exp:
    if x== 2000:
        print(" You spent exactly 2000 dollars in a month")
        break
    else:
        print(" You did not spend exactly 2000 dollars in any month")
        break
        

    #___________another logic _______-
print("did i spent exactly 2000 dollars in any month? " , 2000 in exp)


exp.append(1980)
print(" Monthly expense after adding june month is : ", exp)

exp[3] = exp[3] - 200
print(" Monthly expense after refund in april is : ", exp)