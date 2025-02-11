#basic operations on lists
list1=[1,2,3,4,5,6,7,8,9,10]
sum=0

#sums up the integers in the list
for item in list1:
    sum+=item

#sum(list1) it will print the sum of the items, it works only
#for the numeric values

#Create the list
line="THis is the test string to assemble another string"

line2=[]
line3=""

for item in line:
    if item == "a" or item=="o" or item=="u" or item=="i" or item=="e":
        line2.append(item)
    else:
        continue #this statement will proceed to the next element in the loop

#the same as in lines 18 to 22 can be done for the string
for item in line:
    if item == "a" or item=="o" or item=="u" or item=="i" or item=="e":
        line3+=item
    else:
        continue #this statement will proceed to the next element in the loop

#To identify the size of the list or size of the string you need len(variable_name) function
for i in range(len(line)):
    print(i) #it will print integer numbers from 0 to the total number of characters in the line

#To sort the list of numericals in ascending order you can use sort() function
list1.sort()
#list1 will be sorted in ascending order - https://docs.python.org/3/howto/sorting.html


