# Expolring String Further,,,

# Strings are immutable in Python, meaning they cannot be changed after they are created.
# There are several ways to create String Given Below:

# 1. Single Quotes: 'Hello World'
# 2. Double Quotes: 'hello world
# 3. Inverted Commas: """hello world"""
# 4  Single Inverted Commas: '''hello world'''

# name = "strings" # this is double quoted string.
# name = 'strings1'# this is single quoted string.


# introduction = '''I am Salman, 
#     I am a student of GIAIC,
#     I am currently learning Python. '''

# print(introduction)

# introduction = " I am Saman.\n I am a student of GIAIC.\n Currently learning Python." # \n changes the line which is another way of geting the next line,,,

# print(introduction)

# introduction1 = " I am Saman.\t I am a student of GIAIC.\t Currently learning Python." # \t adds 4 spaces in the line.
 
# print(introduction1)

# String Concatenation

name1 = "Zysha"
name2 = "Salman"

print(name1 + name2) # Concatenation adds 2 strings but without space. 

print(name1 + " " + name2) # It is the exampple of adding the space.

# To know any sentence length python gives a function that is called Len().

lengTheSentence = '''I am Salman, 
#     I am a student of GIAIC,
#     I am currently learning Python. '''

print(len(lengTheSentence))

#Indexing.... Python assigns every sentence index that can be accessed ... Here is how,

name = "Salman"
      # 012345

print(name[0]) # accessing the S 
print(name[1]) # accessing the a
print(name[2]) # accessing the l
print(name[3]) # accessing the m
print(name[4]) # accessing the a
print(name[5]) # accessing the n

name5 = name[0]

print(name5)

# Python has negative indexing , which starts at -1 . Example 

name6 = "Zyeshahuda"
      #10-9-8-7-6-5-4-3-2-1

print(name6[-1])
print(name6[-2])
print(name6[-3])
print(name6[-4])
print(name6[-5])
print(name6[-6])
print(name6[-7])
print(name6[-8])
print(name6[-9])
print(name6[-10])


#Slicing ....

name7 = "Salman"

print(name7[0:4]) # it means it only takes from 0 to 3 letters leaving the 4th.

print(name7[2:6]) # it means it only takes from "l" to "n" letters leaving the 6th.

print(name7[1:3:6]) #
