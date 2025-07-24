# Type Conversion

'''Type conversion is the process of converting one data type to another.
It is also known as typecasting.'''

'''One type conversion Python's interpreter is doing it by itself, and the other one is we ourself is doing it forcfully which is called TypeCasting.'''

a = 20 # integer
b = 30.40 # float

print( a + b) # It will be 50.40 because the interpreter is doing it by itself. Which mean interpreter is taking 'a' value as 20.00.

print( type(a + b)) # It will be float because the interpreter is doing it by itself.

# No we forcefully convert the type of a variable.

# c = "10" wich is a string value we can change it like int("10") this and it become now an integer.

c = int("10") # here we converted the string value to integer.

c = float("10") #we can convert it into float also.

print(type(c)) # It will be int because we converted the string value to integer.
d = 20

print(c + d) # It will be 30 because we converted the string value to integer.

print(type(c + d))

