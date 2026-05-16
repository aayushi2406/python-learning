#ARITHMETIC OPERATORS :
a = 10
b = 5
print("addition :",a + b) #addition
print("subtraction :",a - b) #subtraction
print("multiplication :",a * b) #multiplication
print("division :",a / b) #division
print("modulo :",a % b) #modulus (gives remainder)
print("exponention :",a**b)  #a raise to the power b
print("floor division :",a//b)  #floor division (gives answer in whole number)


#ASSIGNMENT OPERATORS:
x = 100
y = x
print("value of y is :",y)
x = x + 5 #increment(also we can write x+=5)
print("increment :",x)
x = x - 5 #decrement(also we can write x-=5)
print("decrement :",x)


#COMPARISON(RELATIONAL) OPERATORS : (return TRUE or FALSE)
c = 56
d = 25
print(c == d) #compare values
print(c!=d)   #check not equals to
print(c>d)    #check greater than or not
print(c<d)    #check less than or not
print(c>=d)   #check greater or equals than or not
print(c<=d)   #check less or equals than or not


#LOGICAL OPERATORS :
z = 34
w = 84
print(z==10 and z<w)  #AND operation (if all conditions TRUE gives output TRUE)
print(z==34 or z>w)  #OR operation (if any one condiiton is TRUE gives output TRUE)
print(not z)           #NOT operation (gives negation of output)


#MEMBERSHIP OPERATORS :
string = "hello"
print('h' in string)   #in operator check whether a value exist or not
print('a' not in string)


#IDENTIFY OPERATORS :
num1 = 92
num2 = 92
print(num1 is num2)  #is operator check whether two variables refer to the same object in memory or not
print(num1 is not num2)


#BITWISE OPERATORS :  (1 -> True , 0 -> False)
p = 83
q = 72
print("binary of p is :",bin(p))  # bin() function converts number into binary

print(p & q)   #AND operation (Returns 1 only if both bits are 1)
print(p | q)   #OR operation (Returns 1 if any one bit is 1)
print(~p)      #NOT operation (Flips all bits (1 → 0, 0 → 1))
print(p ^ q)   #XOR operation (1 → if bits are different,0 → if bits are same)
print(p >> 2)  #RIGHT SHIFT(Shifts bits to right (divides by 2))
print(p << 2)  #LEFT SHIFT(Shifts bits to left (multiplies by 2))


