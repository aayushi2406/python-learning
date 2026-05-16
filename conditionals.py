# 3 conditional statements : if , if-else , if-elif-else

"""
if statement syntax : 
if(condition):
    code to execute
"""

a = 10
if (a % 2 == 0):
    print("number is even")


"""
if-else statement syntax :
if(condition):
    code to execute
else:
    alternate statement
"""

b = int(input("enter number : "))
if(b % 2 == 0):
    print("number is even")
else:
    print("number is odd")


"""
if-else-elif statement syntax :
if(condition1):
    code to execute
elif(condition2):
    code to execute
else:
    alternate statement
"""

age = int(input("enter your age : "))
if(age < 0):
    print("Invalid age")
elif(age >= 18):
    print("You can Vote")
else:
    print("You cannot vote")