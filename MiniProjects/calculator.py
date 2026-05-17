#BASIC CALCULATOR

num1 = eval(input("enter number 1 : "))
num2 = eval(input("enter number 2 : "))
opr = input("enter the operation(+,-,*,/,%) : ")

if (opr=="+"):
    print(num1 + num2)

elif(opr=="-"):
    print(num1 - num2)

elif(opr=="*"):
    print(num1 * num2)

elif(opr=="/"):
    print(num1 / num2)

elif(opr=="%"):
    print(num1%num2)

else:
    print("Invalid operator")