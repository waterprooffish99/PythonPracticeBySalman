# Changng Case Methods...

# upper() and lower():

text = "Hello, Python!" 
print(text.upper())

print(text.lower())

# title(): and captialize():....

text = "python is awesome"

print(text.title())

print(text.capitalize())

# Checking & Searching Methods
# 🔹 startswith() & endswith()  and the result is in Boolean... True/False.

text = "hello world"

print(text.startswith("hello"))

print(text.endswith("python"))

# 🔹 find() & index()

message = "I love python!"

print(message.find("python")) # find index of python.
print(message.index("o"))
print(message.index("p"))
print(message.index("l"))
print(message.replace("python", "Next.js"))

# 3️⃣ Checking String Content....

word = "python123"

print(word.isalpha()) # Checks if all characters are alphabetic.
print(word.isdigit()) # checks if all characters are numbers.
print(word.isalnum()) # checks if all characters are letters or numbers.
print(" ".isspace()) # checks if the string contains only spaces.


 #Splitting and Joining...

# fruits_list = "apple" , "orange" , "banana"

# fruits_list = fruits.split(",") #split a string to a list.
# print(fruits_list)


word = ["python" , "is" , "awesome"]

print("-".join(word))    #joins the list elements using "-"...! "-" , " " , "_" , "" are the sperators.
print("***".join(word))  #joins the list using "***".
print("".join(word))     #joins the list using "".
print("_".join(word))    #joins the list using "_".
print(" ".join(word))    #joins the list using " ".

# 5️⃣ String Formatting (Modern Method with f-strings)

name = "Salman"
age = 38 

print(f"My name is {name} and I am {age} years old.,!")

word = "banana"

print(word.count("a"))  # Counts occurrence of "a"...
print("Python is awesome" *5) # repeats 5 times in row formate...
print("Python is awesome\n" *5) # repeats 5 times in column formate...

# String Length...

message = "Once I was seven years old my mama told me go get yourself some friends or you'll be lonely" 
print(len(message))


'''🔥 Summary of Important Methods
Method	Description	Example
upper()	Convert to uppercase	"hello".upper() → "HELLO"
lower()	Convert to lowercase	"HELLO".lower() → "hello"
title()	Capitalize first letter of each word	"hello world".title() → "Hello World"
find()	Find substring position	"hello".find("e") → 1
replace()	Replace text	"hello world".replace("world", "Python") → "hello Python"
split()	Convert string to list	"a,b,c".split(",") → ['a', 'b', 'c']
join()	Convert list to string	"-".join(['a', 'b', 'c']) → "a-b-c"
count()	Count occurrences	"banana".count("a") → 3
len()	Find string length	len("hello") → 5'''