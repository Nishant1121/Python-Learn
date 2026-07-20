#Variables
#Variables are containers for storing data values
x = 5 # x is of type int
y = "Nishant" # y is of type str
print(x)
print(y)

#Casting 
#If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

#type() function
#You can get the data type of a variable with the type() function.
x = str(3)    
y = int(3)    
z = float(3)
print(type(x))
print(type(y))
print(type(z))

#Single or Double Quotes?
#String variables can be declared either by using single or double quotes:
x="Nishant"
#is the same as 
x='Nishant'

#Case-Sensitive
#Variable names are case-sensitive.
a= "Nishant"
A = 22
print(a)
print(A)

#Variable Names
#Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Many Values to Multiple Variables
#Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", 'Cherry'
print(x)
print(y)
print(z)

#One Value to Multiple Variables
#And you can assign the same value to multiple variables in one line:
x = y = z = "Nishant"
print(x)
print(y)
print(z)