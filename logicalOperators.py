#Logical Operators...!!!

'''There are 3 types of logical operators 

not, and, or'''

# and Operator!

'''and Operator is used to check if all the conditions are true.
if any one of the condition is false then the whole condition is false. AS shown below'''

x = 8

y = 4

print(x > y and y < x) # It will be true because given conditions are true.
print(x > y and y > x) # It will be false because one of the condition is false.

print(y > x and x < y ) # It will be false because one the condition is false.
# in and operator it is must that both the conditions should be true. to get true output...


#or Operator!

'''or Operator is used to check both conditions but gives result according to the first condition.
It means if the fist condition is true then it returns true , if the first condition is false then it returns false.'''

a = 20

b = 40

print(type( a > b or b < a)) # It will be false  because the first condition is false.

print( a < b or a > b) # It will be true because the first condition is true.


# not Operator!

'''not Operator is used to reverse the result.
It means if the condition is true then it returns false and if the condition is false then it returns true.'''

c = 10

d = 20

print(not c > d) # It will be True because the condition is False.

print(not c < d) # It will be False because the condition is True.










