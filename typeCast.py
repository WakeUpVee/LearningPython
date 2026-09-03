#typecasting = The process of converting a value of data type to another
#              (string, interger, float, boolean)
#               Explicit vs Implicit

name = "Jacob"
age = 21
gpa = 3.7
student = True 

#This is explicit typecasting
age = float(age)
print(age)

student = str(student)
print(student)

#This is implicit typecasting 
x = 2
y = 1.0

x = x / y
print(x)