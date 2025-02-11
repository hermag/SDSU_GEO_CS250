#Basic arithmetic operations
#+, -, *, /(regular division - 5/2 is 2.5), % (division by modulo 5%2 is 1), 
#// (division to get the integer part of the division 5//2 is 2),  
#powering of the numbers 25**2 is 625, 625 ** 0.5 is 25, 
#you can import math, and use math.pow(number to be operated, number of the operation),
#math.pow(625,0.5) is 25
#+=1, =+1, -=1, =-1 this also works
#>,<,>=,<= comparison operators

#Entire syntax of python is based on indentions:
#Example of if else statements
#if x>0:
#   print("x is a positive number")
#elif x<0:
#   print("x is a negative number")
#else:
#   print("x is zero")

#if x>0:
#   print("x is a positive number")
#   if x<0:                             #this statement will not be executed ever
#       print("x is a negative number") 

#Logical operations
#Boolean values, True/False 

#Checking if variable equals to certain value
# ==, a==5 returns True if a is 5, else, False
# logical and - and 
# logical or  - or 
# not operator !, and also keyword not works

#Loops - For loops and while loops
#You can run for loop on every "list" like variable
#example: the_line = "This is the test line to show that for loop can refer to each character of this string."
#for item in the_line:
#    print(item)
#to have different end character after the print statment, you can 
#write the following print(item,end=''), in this case the entire string
#will be printed as a single line.
# output will a single character from the_line string, each character on the new line
#=======
#example: run the loop from 1 to 10
#for i in range(10):
#   print(i)
#prints first 10 numbers, starting from 0
#for i in range(1,11):
#    print(i)
#it will print numbers from 1 to 10
#details about range() function can be seen here https://www.geeksforgeeks.org/python-range-function/
#regarding the while loops
#while (True statement):
#    write the statement 
#    change the statement that needs to be checked


