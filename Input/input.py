# # What is input()?
# ''' input() is used to take information from the user. Whatever the user types, Python saves it as a string (text).'''
# name = input("Enter Your Name:")

# print("SalamAlaikom" + name + "!")

# age = input("Enter Your Age:")

# print("you are " + age + " years old") # This works but python saves it as a string which can cause error so we fix it like that, see below.

age = int(input("Enter Your Age:"))

print("you are " + str(age) + " years old") # Now the result will be in integer that is fully correct.

# Or we can write it using f-string.

print(f"you are {age} years old")

# a = input("Enter a number:")

# b = input("Enter a number:")

# print(a + b) # It will be 2030 because python saves it as a string.


# c = int(input("Enter a number:"))

# d = int(input("Enter a number:"))

# print(c + d) # Now it will be 50 because we converted it to integer.







